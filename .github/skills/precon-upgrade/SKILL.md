---
name: precon-upgrade
description: "Upgrade a Commander precon to a target bracket while keeping it playing the way its designers intended. Use when: upgrading a precon, giving a precon an upgrade path, making a preconstructed Commander deck better, 'help my precon', tuning a precon to bracket 2, 3 or 4, fixing a precon's weak spots, or improving an out-of-the-box Commander deck without changing its archetype."
argument-hint: "A precon decklist or Moxfield URL, plus a target bracket (optional)"
---

# Precon Upgrade

Take a Commander precon and produce a tiered upgrade path. The deck must still play the game its designers built it for, only more consistently and at the target bracket. No budget cap unless the user states one.

## Constraints

- Work only inside the precon's plan. Do not turn it into a different archetype. If a swap does not serve the plan the precon's commander and theme point to, do not make it.
- Colors stay inside the commander's color identity. Off-theme staples (Sol Ring, Arcane Signet, removal, fixing, draw) are allowed when they serve the plan.
- Every card you add or cite must come from `python3 scripts/mtg_cards.py` (`lookup` or `search`). Never use card text, legality, or Game Changer status from memory. Do not hand-edit `cards/library.json`.
- Respect the target bracket. Check Game Changer status with `search "is:gamechanger !\"Card Name\"" --format commander`, and never exceed the bracket's limit.
- Keep the deck at exactly 100 cards, including the commander. Swaps are one-for-one.
- Never change the saved original list. Write the upgraded list to a new file.

## Bracket limits

Confirm the target with the user if they did not give one. Default to one bracket above the precon's current level (most precons are bracket 2).

| Bracket | Game Changers | Also |
|---|---|---|
| 1 Exhibition | none | no tutors, infinite combos, extra turns or mass land destruction |
| 2 Core | none | no mass land destruction; no chained extra turns; no two-card infinite combos |
| 3 Upgraded | up to 3 | no mass land destruction; no early two-card infinite combos |
| 4 Optimized | unlimited | no restriction |
| 5 cEDH | unlimited | metagame-driven |

<!-- UNVERIFIED: bracket limits above come from the published Commander bracket guidelines recalled by the authoring agent, not probed from a source in this workspace. Confirm against the current official bracket text before relying on them. -->

## Approach

1. **Intake.**
   - From a Moxfield URL, run `python3 scripts/mtg_cards.py moxfield <url>`. From pasted text, use it as given. If the import fails or returns no cards, report the exact error, ask for the pasted list, and create no files.
   - Save the original to `decks/commander/precons/<precon-name>.txt` (lowercase kebab-case).
   - Look up every card so its text is in the library.
2. **Read the deck.**
   - Identify the commander and the plan the precon is built around, from the oracle text of the commander and the cards that repeat its theme. State the plan in one or two sentences.
   - Count lands, ramp, card draw, targeted removal, sweepers, counterspells or protection, and win conditions. List the cards that do not support the plan.
3. **Find the weak spots.** Compare against Commander norms for the target bracket: about 36 lands plus 8-12 ramp pieces, 10 or more card draw sources, 8-10 interaction pieces, a clear way to close the game, and fixing that matches the colors. Name each gap.
4. **Propose swaps.** Choose the weakest plan-irrelevant cards to cut, and the best plan-supporting cards to add. Search by color identity and role, for example `id<=<identity> f:commander o:"..."`. Tier them:
   - **Tier 1, fixes:** land base, fixing, mana rocks, and cuts of cards that do nothing.
   - **Tier 2, main upgrade:** better versions of the plan's engines, payoffs, draw and interaction.
   - **Tier 3, stretch:** the strongest plan cards the bracket allows, including Game Changers up to the limit.
   Each tier is a table of Cut, Add and Why (one line, tied to the plan). Give a running Game Changer count.
5. **Verify.** Before presenting, confirm for every add: legal in Commander, inside color identity, not a duplicate, and Game Changer count within the bracket. Confirm the final list totals 100.
6. **Save.** Do this only after the user picks which tiers to apply (default to Tier 1 and 2 if they say "do it"):
   - Write the upgraded list to `decks/commander/precons/<precon-name>-upgraded.txt` in Moxfield format with a `COMMANDER:` section.
   - Write `decks/commander/precons/<precon-name>-upgraded.notes.md` with Goals, Constraints, an `## Upgrade Path` section (the cut and add tables, and why), a Change Log, and a `## Primer` built the way the agent file's step 6(c) describes: role-group sections, an intro sentence for each, and one bullet per nonland card from library text.

## Output

Reply with: the plan in a sentence, the gaps found, the three tier tables, the Game Changer count, and which tiers you recommend. Keep it short, and offer to apply the swaps.
