"""Local Scryfall card library and Moxfield deck import for the MTG Deck Builder agent.

Usage:
    python3 scripts/mtg_cards.py lookup "Lightning Bolt" "Sol Ring" [--format modern] [--refresh]
    python3 scripts/mtg_cards.py search "t:goblin f:pauper cmc<=2" [--limit 40] [--format pauper]
    python3 scripts/mtg_cards.py moxfield <deck-url-or-id>
    python3 scripts/mtg_cards.py image "is:borderless !'Card Name'" [--out-dir cards/images]
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
import urllib.parse
from collections.abc import Callable, Iterable
from datetime import date
from pathlib import Path
from typing import Any

LIBRARY_PATH = Path("cards/library.json")
USER_AGENT = "mtg-deck-builder/1.0"
SCRYFALL_URL = "https://api.scryfall.com"
MOXFIELD_DECK_URL = "https://api2.moxfield.com/v3/decks/all/"
CARD_FIELDS = (
    "name", "mana_cost", "cmc", "type_line", "oracle_text", "power", "toughness",
    "loyalty", "colors", "color_identity", "keywords", "legalities", "set",
    "collector_number", "rarity",
)
FACE_FIELDS = ("name", "mana_cost", "type_line", "oracle_text", "power", "toughness", "loyalty")
BATCH_SIZE = 75
DEFAULT_MAX_AGE_DAYS = 30
REQUEST_DELAY_S = 0.1
MOXFIELD_SECTIONS = (
    ("mainboard", ""),
    ("commanders", "COMMANDER:"),
    ("companions", "COMPANION:"),
    ("sideboard", "SIDEBOARD:"),
    ("maybeboard", "MAYBEBOARD:"),
)
MOXFIELD_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{5,64}$")
IMAGE_HOST_PREFIX = "https://cards.scryfall.io/"
IMAGE_DIR = Path("cards/images")

Card = dict[str, Any]
Library = dict[str, Card]


class HttpError(RuntimeError):
    """Non-2xx HTTP response."""

    def __init__(self, url: str, code: int, body: str) -> None:
        super().__init__(f"HTTP {code} for {url}: {body[:300]}")
        self.code = code


def card_key(name: str) -> str:
    """Return the normalized library key for a card name."""
    return name.strip().lower()


def trim_card(card: Card, today: str) -> Card:
    """Reduce a Scryfall card object to the fields deck building needs."""
    out: Card = {k: card[k] for k in CARD_FIELDS if k in card}
    if "card_faces" in card:
        out["card_faces"] = [{k: f[k] for k in FACE_FIELDS if k in f} for f in card["card_faces"]]
    out["usd"] = card.get("prices", {}).get("usd")
    out["cached"] = today
    return out


def add_to_library(library: Library, cards: Iterable[Card], today: str) -> None:
    """Merge Scryfall cards into the library, aliasing multi-face cards by front-face name."""
    for card in cards:
        entry = trim_card(card, today)
        library[card_key(card["name"])] = entry
        if " // " in card["name"]:
            library[card_key(card["name"].split(" // ")[0])] = entry


def is_stale(entry: Card, today: date, max_age_days: int) -> bool:
    """Return True when a cached entry is older than max_age_days."""
    return (today - date.fromisoformat(entry["cached"])).days > max_age_days


def for_format(entry: Card, fmt: str | None) -> Card:
    """Return the entry with legalities narrowed to one format, if given."""
    if not fmt:
        return entry
    return {**entry, "legalities": {fmt: entry.get("legalities", {}).get(fmt, "unknown")}}


def lookup(
    names: list[str],
    library: Library,
    today: date,
    fetch_collection: Callable[[list[dict[str, str]]], dict[str, Any]],
    max_age_days: int = DEFAULT_MAX_AGE_DAYS,
    refresh: bool = False,
) -> tuple[list[Card], list[str]]:
    """Resolve names from the library, fetching only missing or stale cards from Scryfall."""
    missing = [
        n for n in dict.fromkeys(names)
        if refresh or card_key(n) not in library or is_stale(library[card_key(n)], today, max_age_days)
    ]
    not_found: list[str] = []
    for i in range(0, len(missing), BATCH_SIZE):
        resp = fetch_collection([{"name": n} for n in missing[i:i + BATCH_SIZE]])
        add_to_library(library, resp.get("data", []), today.isoformat())
        not_found.extend(x.get("name", "") for x in resp.get("not_found", []))
    found = [library[card_key(n)] for n in dict.fromkeys(names) if card_key(n) in library]
    return found, not_found


def moxfield_to_text(deck: dict[str, Any]) -> str:
    """Render a Moxfield v3 deck JSON as Moxfield import text."""
    blocks: list[str] = []
    for board, header in MOXFIELD_SECTIONS:
        cards = deck.get("boards", {}).get(board, {}).get("cards", {})
        if not cards:
            continue
        lines = [
            f'{c["quantity"]} {c["card"]["name"]} ({c["card"]["set"].upper()}) {c["card"]["cn"]}'
            for c in sorted(cards.values(), key=lambda c: c["card"]["name"])
        ]
        blocks.append("\n".join(([header] if header else []) + lines))
    return "\n\n".join(blocks)


def parse_moxfield_id(value: str) -> str:
    """Extract and validate a Moxfield public deck ID from a URL or bare ID."""
    deck_id = value.split("?")[0].split("#")[0].rstrip("/").split("/")[-1]
    if not MOXFIELD_ID_PATTERN.match(deck_id):
        raise ValueError(f"Not a valid Moxfield deck ID: {value!r}")
    return deck_id


def load_library(path: Path = LIBRARY_PATH) -> Library:
    """Load the card library, or an empty one if it does not exist."""
    return json.loads(path.read_text()) if path.exists() else {}


def save_library(library: Library, path: Path = LIBRARY_PATH) -> None:
    """Persist the card library with stable ordering for readable diffs."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(library, indent=1, sort_keys=True) + "\n")


def _request(url: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    # curl uses the OS trust store, which works behind TLS-inspecting proxies where Python's does not.
    cmd = ["curl", "-sS", "--max-time", "30", "-w", "\n%{http_code}",
           "-H", f"User-Agent: {USER_AGENT}", "-H", "Accept: application/json"]
    stdin = None
    if payload is not None:
        cmd += ["-X", "POST", "-H", "Content-Type: application/json", "--data-binary", "@-"]
        stdin = json.dumps(payload)
    try:
        proc = subprocess.run([*cmd, url], input=stdin, capture_output=True, text=True, check=True)
    finally:
        time.sleep(REQUEST_DELAY_S)
    body, _, code = proc.stdout.rpartition("\n")
    if not code.isdigit() or not 200 <= int(code) < 300:
        raise HttpError(url, int(code) if code.isdigit() else 0, body)
    return json.loads(body)


def image_url(card: Card) -> str | None:
    """Return the best image URL for a Scryfall card, using the front face for multi-face cards."""
    uris = card.get("image_uris") or (card.get("card_faces") or [{}])[0].get("image_uris") or {}
    return uris.get("png") or uris.get("large")


def image_filename(name: str, set_code: str, collector_number: str) -> str:
    """Return a filesystem-safe PNG name for one printing."""
    slug = re.sub(r"[^a-z0-9]+", "-", f"{name} {set_code} {collector_number}".lower()).strip("-")
    return f"{slug}.png"


def download_image(url: str, dest: Path) -> None:
    """Download a Scryfall card image to dest. Only Scryfall's image host is allowed."""
    if not url.startswith(IMAGE_HOST_PREFIX):
        raise ValueError(f"Refusing to download from {url!r}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(["curl", "-sS", "-f", "--max-time", "60", "-H", f"User-Agent: {USER_AGENT}",
                        "-o", str(dest), url], check=True)
    finally:
        time.sleep(REQUEST_DELAY_S)


def _fetch_first_print(query: str) -> Card | None:
    url = f"{SCRYFALL_URL}/cards/search?" + urllib.parse.urlencode({"q": query, "unique": "prints"})
    try:
        data = _request(url).get("data", [])
    except HttpError as err:
        if err.code == 404:
            return None
        raise
    return data[0] if data else None


def _fetch_collection(identifiers: list[dict[str, str]]) -> dict[str, Any]:
    return _request(f"{SCRYFALL_URL}/cards/collection", {"identifiers": identifiers})


def _search(query: str, limit: int) -> list[Card]:
    url: str | None = f"{SCRYFALL_URL}/cards/search?" + urllib.parse.urlencode({"q": query})
    cards: list[Card] = []
    while url and len(cards) < limit:
        try:
            resp = _request(url)
        except HttpError as err:
            if err.code == 404:
                break
            raise
        cards.extend(resp.get("data", []))
        url = resp.get("next_page") if resp.get("has_more") else None
    return cards[:limit]


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_lookup = sub.add_parser("lookup", help="Get cards by exact name, using the local library first")
    p_lookup.add_argument("names", nargs="+")
    p_lookup.add_argument("--format", dest="fmt")
    p_lookup.add_argument("--refresh", action="store_true")
    p_lookup.add_argument("--max-age", type=int, default=DEFAULT_MAX_AGE_DAYS)
    p_search = sub.add_parser("search", help="Scryfall full-text search; results are cached")
    p_search.add_argument("query")
    p_search.add_argument("--limit", type=int, default=40)
    p_search.add_argument("--format", dest="fmt")
    p_mox = sub.add_parser("moxfield", help="Import a public Moxfield deck as Moxfield text")
    p_mox.add_argument("deck")
    p_img = sub.add_parser("image", help="Download the card image for the first printing matching a query")
    p_img.add_argument("query")
    p_img.add_argument("--out-dir", type=Path, default=IMAGE_DIR)
    args = parser.parse_args(argv)

    if args.cmd == "image":
        card = _fetch_first_print(args.query)
        url = image_url(card) if card else None
        if not card or not url:
            print(json.dumps({"not_found": [args.query]}), file=sys.stderr)
            return 1
        dest = args.out_dir / image_filename(card["name"], card["set"], card["collector_number"])
        download_image(url, dest)
        print(dest)
        return 0

    if args.cmd == "moxfield":
        deck = _request(MOXFIELD_DECK_URL + parse_moxfield_id(args.deck))
        print(f"# {deck.get('name')} | format: {deck.get('format')}")
        print(moxfield_to_text(deck))
        return 0

    library = load_library()
    today = date.today()
    if args.cmd == "lookup":
        found, not_found = lookup(args.names, library, today, _fetch_collection, args.max_age, args.refresh)
    else:
        results = _search(args.query, args.limit)
        add_to_library(library, results, today.isoformat())
        found, not_found = [library[card_key(c["name"])] for c in results], []
    save_library(library)
    for card in found:
        print(json.dumps(for_format(card, args.fmt), separators=(",", ":")))
    if not_found:
        print(json.dumps({"not_found": not_found}), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
