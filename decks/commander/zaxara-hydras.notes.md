# Zaxara Hydras: Notes

## Goals

- Commander: Zaxara, the Exemplary (Sultai, {1}{B}{G}{U}).
- Archetype: X-spell pile. Every spell with {X} in its cost also makes a Hydra
  token with X +1/+1 counters, so each X spell is two threats.
- Hydra tribal with typical tribal support (lords, cost reducers, card draw).
- Fun over winning, but should hold its own at bracket 3.
- Pace: Zaxara on turn 4, wins or stabilizes around turns 8-10.

## Constraints

- Bracket 3 table. No infinite combos and nothing that wins at instant speed.
- Two Game Changers in the main list: Rhystic Study and Cyclonic Rift.
- No budget (user proxies), but every card must earn its slot.
- Existing collection is not a factor. No exclusions.

## Change Log

- 2026-10-09: First build. 35 lands, 13 mana rocks and ramp spells, 20
  X spells.
- 2026-10-21: Rebuilt the primer around role groups with a bullet per card,
  checked against cards/library.json.

## Primer

### Game Plan

Ramp into Zaxara on turn 4. Zaxara taps for two mana of one color, so the
next turn is a large X spell. Each X spell triggers Zaxara and makes a Hydra
with X counters. Counter doublers and Hydra tribal cards turn that board into
a lethal team around turns 8-10.

### Commander

- **Zaxara, the Exemplary:** a 2/3 deathtouch that taps for two mana of
  any one color. Whenever you cast a spell with {X} in its mana cost, it
  creates a 0/0 Hydra token with X +1/+1 counters. Every X spell below is
  therefore two threats, and Zaxara's own mana makes X bigger.

### Hydras With X

Each is a Hydra spell (for Herald's Horn, Urza's Incubator, Vanquisher's
Banner and Door of Destinies) and an X spell (for Zaxara).

- **Hydroid Krasis:** cast trigger draws half X and gains half X life,
  then a flying, trample X/X. The cast trigger (and Zaxara's) still
  resolves if the creature is countered.
- **Genesis Hydra:** cast trigger reveals the top X cards and puts a
  nonland permanent with mana value X or less onto the battlefield, then
  an X/X body.
- **Hooded Hydra:** an X/X that leaves a 1/1 Snake per counter when it
  dies. Board-wipe insurance.
- **Primordial Hydra:** doubles its own counters each upkeep, with trample
  at ten or more.
- **Benevolent Hydra:** your other creatures get one extra counter each
  time counters go on them, so every Zaxara token is one bigger. Taps to
  move its counters onto another creature.
- **Neverwinter Hydra:** costs {X}{X}{G}{G} and rolls X six-sided dice
  for its counters. Trample and ward {4}.
- **Steelbane Hydra:** remove a counter and pay {2}{G} to destroy an
  artifact or enchantment. Flexible removal.
- **Stumpsquall Hydra:** distributes X counters among itself and any
  commanders, so Zaxara can grow out of removal range.
- **Mistcutter Hydra:** can't be countered, has haste and protection from
  blue. Good against blue control tables.
- **Protean Hydra:** damage removes counters instead, and each counter
  removed comes back as two at the next end step. Hard to kill in combat.

### Other X Spells

These still trigger Zaxara for a Hydra token.

- **Walking Ballista:** costs {X}{X} for X counters; Zaxara's token also
  gets X. Ping creatures or players by removing counters, and {4} adds
  one. A mana sink and finisher.
- **Hangarback Walker:** costs {X}{X}, grows for {1}, and leaves flying
  Thopters equal to its counters when it dies.
- **Stonecoil Serpent:** X/X reach, trample, protection from multicolored.
- **Altered Ego:** can't be countered. Copies any creature with X extra
  counters; copy Kalonian Hydra or Vorinclex.
- **Finale of Devastation:** put a creature with mana value X or less from
  library or graveyard onto the battlefield. At X of 10 or more, your
  creatures get +X/+X and haste: a game-ending turn.
- **Genesis Wave:** reveal the top X cards and put every permanent with
  mana value X or less onto the battlefield.
- **Villainous Wealth:** exile the top X cards of an opponent's library
  and cast any spells with mana value X or less from them for free.
- **Mind Spring:** draw X.
- **Blue Sun's Zenith:** a target player draws X at instant speed, then it
  shuffles back into your library. Cast it at the end of an opponent's
  turn.
- **Exsanguinate:** each opponent loses X and you gain that much. The
  finisher after a big Zaxara turn.

### Hydras Without X

These are threats and Hydra tribal bodies but do not trigger Zaxara: their
{X} is in an activated ability, not their mana cost, or they have no X.

- **Kalonian Hydra:** a 4/4 trampler (with four counters) that doubles the
  +1/+1 counters on each of your creatures whenever it attacks. Zaxara
  tokens double too.
- **Managorger Hydra:** a three-drop trampler that grows whenever any
  player casts a spell.
- **Hydra Broodmaster:** a 7/7. {X}{X}{G} for monstrosity X adds X
  counters and makes X Hydra tokens that are X/X.
- **Polukranos, World Eater:** a 5/5. Monstrosity X splits X damage among
  opposing creatures.
- **Polukranos, Unchained:** enters with six counters, loses counters
  instead of taking damage, and fights for {1}{B}{G}. Escapes from the
  graveyard with twelve.

### Counter Doublers

- **Doubling Season:** doubles the counters on every Hydra and doubles
  Zaxara's tokens, so each X spell makes two Hydra tokens.
- **Vorinclex, Monstrous Raider:** a 6/6 trample, haste that doubles
  counters you put on anything and halves opponents' counters.
- **Branching Evolution:** doubles +1/+1 counters put on your creatures.
- **Hardened Scales:** one extra +1/+1 counter each time counters go on a
  creature you control.

### Hydra Tribal

Name Hydra for each of these. Zaxara's tokens are Hydras.

- **Herald's Horn:** Hydra spells cost {1} less, and an upkeep reveal puts
  a Hydra from the top of your library into your hand.
- **Urza's Incubator:** Hydra spells cost {2} less, so each X Hydra gets
  two more X for the same mana.
- **Vanquisher's Banner:** Hydras get +1/+1, and you draw whenever you
  cast a Hydra spell.
- **Door of Destinies:** a charge counter whenever you cast a Hydra spell;
  Hydras get +1/+1 per counter. Doubling Season and Vorinclex double the
  charge counters too.
- **Kindred Discovery:** draw whenever a Hydra enters or attacks. Each X
  spell that is a Hydra draws two: one for the spell, one for Zaxara's
  token.

### Clones

- **Clever Impersonator:** copy any nonland permanent, such as Doubling
  Season or your biggest Hydra.
- **Phyrexian Metamorph:** copy any artifact or creature for {3} and 2
  life.
- **Spark Double:** copy a creature you control, non-legendary and with
  one extra counter. Copy Zaxara for a second X-spell trigger and a
  second mana source.

### Card Advantage

- **Rhystic Study:** draws whenever an opponent casts a spell unless they
  pay {1}.
- **Sylvan Library:** see two extra cards each draw step; keep them for 4
  life each.
- **Phyrexian Arena:** an extra card each upkeep for 1 life.
- **Mulldrifter:** draw two, as a 2/2 flier or evoked for {2}{U}.
- **Eternal Witness:** return any card from your graveyard to hand.

### Ramp

Zaxara itself is the biggest ramp piece: it adds two mana a turn.

- **Sol Ring:** {C}{C} from turn one.
- **Arcane Signet:** any color in your identity.
- **Fellwar Stone:** a color an opponent's land could make.
- **Mind Stone:** {C}, and cash it in for a card later.
- **Talisman of Curiosity:** {G} or {U}.
- **Talisman of Dominance:** {U} or {B}.
- **Talisman of Resilience:** {B} or {G}.
- **Birds of Paradise:** turn-one flying dork of any color.
- **Sakura-Tribe Elder:** chump-block, then sacrifice it for a basic land.
- **Farseek:** an Island or Swamp card (including the shocks and Zagoth
  Triome) onto the battlefield tapped.
- **Nature's Lore:** a Forest card onto the battlefield untapped.
- **Cultivate:** one basic onto the battlefield tapped, one to hand.
- **Kodama's Reach:** a second copy of Cultivate.

### Protection

- **Lightning Greaves:** shroud and haste for {0} equip. Haste lets
  Zaxara tap for mana the turn it lands.
- **Swiftfoot Boots:** hexproof and haste; you can still target Zaxara
  yourself.
- **Heroic Intervention:** hexproof and indestructible for your
  permanents until end of turn.

### Interaction

- **Counterspell:** stop a board wipe. Tap Zaxara for {U}{U} on an
  opponent's turn if you have nothing to cast.
- **Cyclonic Rift:** bounce a nonland permanent, or overload for {6}{U}
  to bounce everything opponents control before your lethal attack.
- **Assassin's Trophy:** destroy any permanent an opponent controls.
- **Beast Within:** destroy any permanent; its controller gets a 3/3.
- **Putrefy:** destroy an artifact or creature at instant speed.
- **Toxic Deluge:** all creatures get -X/-X for X life. Kills your Hydras
  too; use it when behind.

### Mana Base

35 lands, 19 basic. Green is the main color. Fetch lands find Breeding
Pool, Watery Grave, Overgrown Tomb and Zagoth Triome. Cavern of Souls
(name Hydra) makes your Hydra spells uncounterable. Lair of the Hydra
turns into an X/X Hydra creature for {X}{G}, a late-game mana sink.

### Mulligan

Keep hands with 3 or more lands (or 2 lands plus a ramp piece) and a way
to reach four mana by turn 4. A hand with ramp and one X spell is a good
keep.

### Turn Guide

1. **Turns 1-2:** lands, then Sol Ring, Arcane Signet, a Talisman, Birds
   of Paradise, or a green ramp spell.
2. **Turn 3:** Rhystic Study, Sylvan Library, Managorger Hydra or a rock
   to reach Zaxara.
3. **Turn 4:** Zaxara, ideally with Heroic Intervention up or Lightning
   Greaves to tap it at once.
4. **Turns 5-7:** cast X spells with the extra mana. Each makes a Hydra
   token and resolves its own effect. Add doublers and tribal support.
5. **Turns 8-10:** a large X spell, then attack with the Hydra team. Close
   with Finale of Devastation at X of 10 or more, Exsanguinate, or
   Walking Ballista.

### Cautions

- Walking Ballista forms infinite combos with some cards (Heartstone is
  one). Do not add them, to keep the deck within the table rules.
- Toxic Deluge also kills your own Hydras. Use it only when behind.
- Zaxara is a 2/3. Protect it with Lightning Greaves, Swiftfoot Boots or
  Heroic Intervention.
