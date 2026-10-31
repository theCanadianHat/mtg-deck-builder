import sys
from datetime import date
from pathlib import Path
from typing import Any

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import mtg_cards  # noqa: E402

BOLT = {
    "name": "Lightning Bolt", "mana_cost": "{R}", "cmc": 1.0, "type_line": "Instant",
    "oracle_text": "Lightning Bolt deals 3 damage to any target.", "colors": ["R"],
    "legalities": {"modern": "legal", "standard": "not_legal"}, "set": "m10",
    "collector_number": "146", "rarity": "common", "prices": {"usd": "1.50"}, "image_uris": {"x": 1},
}
FIRE_ICE = {
    "name": "Fire // Ice", "cmc": 4.0, "type_line": "Instant // Instant", "set": "mh2",
    "collector_number": "290", "prices": {"usd": None}, "legalities": {"modern": "legal"},
    "card_faces": [
        {"name": "Fire", "mana_cost": "{1}{R}", "oracle_text": "Fire deals 2 damage...", "image_uris": {}},
        {"name": "Ice", "mana_cost": "{1}{U}", "oracle_text": "Tap target permanent..."},
    ],
}


def test_trim_card_keeps_deckbuilding_fields_and_drops_others() -> None:
    out = mtg_cards.trim_card(BOLT, "2026-10-01")
    assert out["oracle_text"] == BOLT["oracle_text"]
    assert out["usd"] == "1.50"
    assert out["cached"] == "2026-10-01"
    assert "image_uris" not in out and "prices" not in out


def test_add_to_library_aliases_front_face_of_multi_face_cards() -> None:
    lib: mtg_cards.Library = {}
    mtg_cards.add_to_library(lib, [FIRE_ICE], "2026-10-01")
    assert lib["fire // ice"] is lib["fire"]
    assert lib["fire"]["card_faces"][0] == {"name": "Fire", "mana_cost": "{1}{R}", "oracle_text": "Fire deals 2 damage..."}


def test_is_stale_respects_max_age() -> None:
    entry = {"cached": "2026-09-01"}
    assert mtg_cards.is_stale(entry, date(2026, 10, 1), 29)
    assert not mtg_cards.is_stale(entry, date(2026, 10, 1), 30)


def test_for_format_narrows_legalities() -> None:
    entry = mtg_cards.trim_card(BOLT, "2026-10-01")
    assert mtg_cards.for_format(entry, "modern")["legalities"] == {"modern": "legal"}
    assert mtg_cards.for_format(entry, "vintage")["legalities"] == {"vintage": "unknown"}
    assert mtg_cards.for_format(entry, None) is entry


def test_lookup_only_fetches_missing_or_stale_cards() -> None:
    lib: mtg_cards.Library = {}
    mtg_cards.add_to_library(lib, [BOLT], date.today().isoformat())
    calls: list[list[dict[str, str]]] = []

    def fake_fetch(ids: list[dict[str, str]]) -> dict[str, Any]:
        calls.append(ids)
        return {"data": [FIRE_ICE], "not_found": [{"name": "Fake Card"}]}

    found, not_found = mtg_cards.lookup(["Lightning Bolt", "Fire", "Fake Card"], lib, date.today(), fake_fetch)
    assert calls == [[{"name": "Fire"}, {"name": "Fake Card"}]]
    assert [c["name"] for c in found] == ["Lightning Bolt", "Fire // Ice"]
    assert not_found == ["Fake Card"]


def test_lookup_refresh_refetches_cached_cards() -> None:
    lib: mtg_cards.Library = {}
    mtg_cards.add_to_library(lib, [BOLT], date.today().isoformat())
    calls: list[list[dict[str, str]]] = []

    def fake_fetch(ids: list[dict[str, str]]) -> dict[str, Any]:
        calls.append(ids)
        return {"data": [BOLT], "not_found": []}

    mtg_cards.lookup(["Lightning Bolt"], lib, date.today(), fake_fetch, refresh=True)
    assert calls == [[{"name": "Lightning Bolt"}]]


def test_lookup_batches_requests_at_scryfall_limit() -> None:
    sizes: list[int] = []

    def fake_fetch(ids: list[dict[str, str]]) -> dict[str, Any]:
        sizes.append(len(ids))
        return {"data": [], "not_found": ids}

    mtg_cards.lookup([f"Card {i}" for i in range(80)], {}, date.today(), fake_fetch)
    assert sizes == [75, 5]


def test_moxfield_to_text_orders_sections_with_mainboard_first() -> None:
    def entry(name: str, qty: int = 1) -> dict[str, Any]:
        return {"quantity": qty, "card": {"name": name, "set": "eld", "cn": "1"}}

    deck = {"boards": {
        "commanders": {"cards": {"a": entry("Chulane, Teller of Tales")}},
        "mainboard": {"cards": {"b": entry("Sol Ring"), "c": entry("Forest", 30)}},
        "sideboard": {"cards": {}},
    }}
    assert mtg_cards.moxfield_to_text(deck) == (
        "30 Forest (ELD) 1\n1 Sol Ring (ELD) 1\n\nCOMMANDER:\n1 Chulane, Teller of Tales (ELD) 1"
    )


def test_moxfield_to_text_sorts_by_card_name_not_quantity() -> None:
    deck = {"boards": {"mainboard": {"cards": {
        "a": {"quantity": 1, "card": {"name": "Zuran Orb", "set": "ice", "cn": "1"}},
        "b": {"quantity": 20, "card": {"name": "Island", "set": "ice", "cn": "2"}},
    }}}}
    assert mtg_cards.moxfield_to_text(deck) == (
        "20 Island (ICE) 2\n1 Zuran Orb (ICE) 1"
    )


@pytest.mark.parametrize("value, expected", [
    ("https://moxfield.com/decks/oEWXWHM5eEGMmopExLWRCA", "oEWXWHM5eEGMmopExLWRCA"),
    ("https://www.moxfield.com/decks/abc_DEF-123/?tab=stats", "abc_DEF-123"),
    ("oEWXWHM5eEGMmopExLWRCA", "oEWXWHM5eEGMmopExLWRCA"),
])
def test_parse_moxfield_id_accepts_urls_and_ids(value: str, expected: str) -> None:
    assert mtg_cards.parse_moxfield_id(value) == expected


@pytest.mark.parametrize("value", ["../../etc", "a b", "x", "id;rm"])
def test_parse_moxfield_id_rejects_unsafe_values(value: str) -> None:
    with pytest.raises(ValueError):
        mtg_cards.parse_moxfield_id(value)


class _Proc:
    def __init__(self, stdout: str) -> None:
        self.stdout = stdout


def test_request_posts_json_via_stdin_without_shell(monkeypatch: pytest.MonkeyPatch) -> None:
    seen: dict[str, Any] = {}

    def fake_run(cmd: list[str], **kw: Any) -> _Proc:
        seen.update(cmd=cmd, **kw)
        return _Proc('{"data": []}\n200')

    monkeypatch.setattr(mtg_cards.subprocess, "run", fake_run)
    monkeypatch.setattr(mtg_cards, "REQUEST_DELAY_S", 0)
    assert mtg_cards._request("https://x.test/a", {"identifiers": []}) == {"data": []}
    assert seen["cmd"][0] == "curl" and seen["cmd"][-1] == "https://x.test/a"
    assert "--data-binary" in seen["cmd"] and seen["input"] == '{"identifiers": []}'
    assert "shell" not in seen


def test_request_raises_http_error_on_non_2xx(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(mtg_cards.subprocess, "run", lambda cmd, **kw: _Proc('{"err": 1}\n404'))
    monkeypatch.setattr(mtg_cards, "REQUEST_DELAY_S", 0)
    with pytest.raises(mtg_cards.HttpError) as exc:
        mtg_cards._request("https://x.test/b")
    assert exc.value.code == 404


def test_search_treats_404_as_no_results(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_request(url: str, payload: Any = None) -> dict[str, Any]:
        raise mtg_cards.HttpError(url, 404, "")

    monkeypatch.setattr(mtg_cards, "_request", fake_request)
    assert mtg_cards._search("t:nothing", 10) == []


def test_search_follows_pages_up_to_limit(monkeypatch: pytest.MonkeyPatch) -> None:
    pages = iter([
        {"data": [{"name": "A"}, {"name": "B"}], "has_more": True, "next_page": "p2"},
        {"data": [{"name": "C"}, {"name": "D"}], "has_more": False},
    ])
    monkeypatch.setattr(mtg_cards, "_request", lambda url, payload=None: next(pages))
    assert [c["name"] for c in mtg_cards._search("q", 3)] == ["A", "B", "C"]


def test_main_lookup_prints_cached_cards(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(mtg_cards, "LIBRARY_PATH", Path("cards/library.json"))
    monkeypatch.setattr(mtg_cards, "_fetch_collection", lambda ids: {"data": [BOLT], "not_found": []})
    assert mtg_cards.main(["lookup", "Lightning Bolt", "--format", "modern"]) == 0
    assert '"legalities":{"modern":"legal"}' in capsys.readouterr().out
    assert (tmp_path / "cards" / "library.json").exists()


def test_library_round_trip(tmp_path: Path) -> None:
    path = tmp_path / "cards" / "library.json"
    assert mtg_cards.load_library(path) == {}
    mtg_cards.save_library({"lightning bolt": {"name": "Lightning Bolt"}}, path)
    assert mtg_cards.load_library(path) == {"lightning bolt": {"name": "Lightning Bolt"}}


def test_image_url_prefers_png_and_falls_back_to_front_face() -> None:
    assert mtg_cards.image_url({"image_uris": {"png": "p", "large": "l"}}) == "p"
    assert mtg_cards.image_url({"card_faces": [{"image_uris": {"large": "f"}}, {}]}) == "f"
    assert mtg_cards.image_url({}) is None


def test_image_filename_is_a_safe_slug() -> None:
    assert mtg_cards.image_filename("Sheoldred, the Apocalypse", "dmu", "107") == "sheoldred-the-apocalypse-dmu-107.png"


def test_download_image_rejects_non_scryfall_hosts(tmp_path: Path) -> None:
    with pytest.raises(ValueError):
        mtg_cards.download_image("https://example.com/x.png", tmp_path / "x.png")
