# Super-Skrull: Notes

## Goals

- Commander: Super-Skrull (Five-Color, BBB commander at 4 mana).
- Archetype: mana sinks. Ramp and fix, then spend every turn's mana on
  Super-Skrull's five abilities.
- Fun over winning, but should hold its own at bracket 3.
- Likes tokens and counters. Clones of permanents with lasting or stacking
  effects are welcome.
- Pace: wins or stabilizes around turns 8-10, with pressure on turn 4.

## Constraints

- Bracket 3 table. Stax and combos are fine as long as nothing wins at
  instant speed.
- No budget (user proxies), but every card must earn its slot and make sense
  in the deck.
- Existing collection is not a factor.

## Change Log

- 2026-10-09: First build. 36 lands, 13 mana rocks and ramp spells.
- 2026-10-21: Rebuilt the primer around role groups with a bullet per card,
  checked against cards/library.json.

## Primer

### Game Plan

Ramp and fix into Super-Skrull on turn 4, then spend spare mana every turn
on his abilities. Each ability uses a different color, so the deck is built
to make all five.

| Ability | Cost | Use it to |
|---------|------|-----------|
| Create a 0/4 Wall | {2}{W} | Block, feed Arcades and Assault Formation |
| +4/+4 until end of turn | {3}{G} | Win combat or push damage |
| 4 damage to target creature | {4}{R} | Remove blockers or threats |
| Target player draws four | {5}{U} | Refill your hand (target yourself) |

Two activations stand out. Target an opponent with the draw-four while
Sheoldred, the Apocalypse is out and they lose 8 life (Smothering Tithe
also triggers four times). With a token doubler, each {2}{W} makes two or
more Walls, and with Arcades, the Strategist each Wall draws a card and
attacks for 4.

### Commander

- **Super-Skrull:** a 4/5 flier for {1}{B}{B}{B} with the four abilities
  above. Every other card in the deck either makes the mana to activate
  him, multiplies what his abilities produce, or copies him.

### Doublers

These multiply Wall tokens, other tokens and counters.

- **Doubling Season:** doubles tokens and every counter placed on your
  permanents. Planeswalkers enter with double loyalty, so Elspeth, Sun's
  Champion enters with 8 and can use her −7 at once.
- **Parallel Lives:** doubles tokens you create.
- **Anointed Procession:** doubles tokens you create.
- **Mondrak, Glory Dominus:** doubles tokens. Sacrifice two other
  artifacts or creatures (spare tokens) for an indestructible counter.
- **Vorinclex, Monstrous Raider:** a 6/6 trample, haste body that doubles
  every counter you put on permanents (including loyalty) and halves
  opponents' counters.
- **Branching Evolution:** doubles +1/+1 counters put on your creatures.
- **Hardened Scales:** one extra +1/+1 counter each time counters go on a
  creature you control.

### Clones

Copy Super-Skrull for a second set of abilities, or copy a doubler.

- **Spark Double:** copy Super-Skrull or another creature or planeswalker
  you control. The copy is not legendary and gets an extra +1/+1 (or
  loyalty) counter, so you keep both.
- **Sakashima of a Thousand Faces:** copy another creature you control.
  The legend rule no longer applies to your permanents, so copying
  Super-Skrull gives you two.
- **Clever Impersonator:** copy any nonland permanent. Copy Doubling
  Season, Smothering Tithe or the best creature on the table.
- **Phyrexian Metamorph:** copy any artifact or creature for {3} and 2
  life.
- **Altered Ego:** cannot be countered. Copy any creature with X extra
  +1/+1 counters.

### Walls and Toughness Damage

Super-Skrull's 0/4 Walls are defenders. These let them attack and draw.

- **Arcades, the Strategist:** draw a card whenever a creature with
  defender enters. Defenders deal combat damage equal to toughness and
  can attack.
- **Assault Formation:** every creature you control deals combat damage
  equal to its toughness. {G} lets one defender attack, and {2}{G} gives
  your team +0/+1.

### Token and Counter Makers

- **Bitterblossom:** a 1/1 flying Faerie each upkeep for 1 life.
  Skullclamp fodder.
- **Krenko, Tin Street Kingpin:** gets a +1/+1 counter whenever it
  attacks, then makes Goblins equal to its power. Doublers grow both.
- **Esika's Chariot:** two 2/2 Cats, and each attack copies a token you
  control. Crew 4 with a Wall.
- **Grave Titan:** a 6/6 deathtouch that makes two 2/2 Zombies on enter
  and attack.
- **Hornet Queen:** five flying, deathtouch bodies in one card.
- **Elspeth, Sun's Champion:** +1 makes three Soldiers. −3 destroys
  creatures with power 4 or greater, which spares your Walls and tokens.
- **Martial Coup:** X Soldiers. At X of 5 or more, destroy all other
  creatures: a one-sided wipe that leaves you a doubled army.
- **Hangarback Walker:** enters with X counters, grows for {1}, and leaves
  that many flying Thopters when it dies.
- **Walking Ballista:** enters with X counters, {4} adds one, and each
  counter removed deals 1 damage. A mana sink and a finisher.
- **Mikaeus, the Lunarch:** taps to grow itself, or to move a counter onto
  each other creature you control.
- **Cathars' Crusade:** whenever a creature enters, put a +1/+1 counter on
  each creature you control. Every Wall makes your whole team bigger.

### Finishers

- **Mirror Entity:** {X} sets your creatures' base power and toughness
  to X/X. Late, a wide board of Walls and tokens becomes lethal.
- **Chameleon Colossus:** a 4/4 with protection from black that doubles
  its power for {2}{G}{G}, repeatably.
- **Kalitas, Traitor of Ghet:** opposing nontoken creatures that would
  die are exiled, and you get a 2/2 Zombie. Pairs with Super-Skrull's
  4-damage ability.

### Card Advantage

- **Rhystic Study:** draws whenever an opponent casts a spell unless they
  pay {1}.
- **Phyrexian Arena:** an extra card each upkeep for 1 life.
- **Sylvan Library:** see two extra cards each draw step; keep them for
  4 life each.
- **Skullclamp:** equip a 1/1 token and it dies, drawing two. Walls
  survive it (they become 1/3).
- **Mulldrifter:** draw two, either as a 2/2 flier or evoked for {2}{U}.
- **Sheoldred, the Apocalypse:** gain 2 life per card you draw; opponents
  lose 2 per card they draw. Aim the draw-four ability at an opponent.
- **Smothering Tithe:** a Treasure each time an opponent draws unless they
  pay {2}.
- **Eternal Witness:** return any card from your graveyard to hand.
- **Sun Titan:** a 6/6 vigilance that returns a permanent card with mana
  value 3 or less from your graveyard on enter and attack.

### Ramp and Fixing

Super-Skrull needs {B}{B}{B}, and his abilities need all five colors.

- **Sol Ring:** {C}{C} from turn one.
- **Arcane Signet:** any color in your identity.
- **Fellwar Stone:** a color an opponent's land could make.
- **Mind Stone:** {C}, and cash it in for a card later.
- **Talisman of Hierarchy:** {W} or {B}.
- **Talisman of Resilience:** {B} or {G}.
- **Chromatic Lantern:** your lands tap for any color.
- **Coalition Relic:** any color, or store a charge counter for a burst
  of two the next turn (more with Doubling Season or Vorinclex).
- **Birds of Paradise:** turn-one flying mana dork of any color.
- **Undercover Skrull:** a mana dork of any color that becomes a 3/3 of
  all creature types once two creature cards are in your graveyard.
- **Farseek:** a Plains, Island, Swamp or Mountain card onto the
  battlefield tapped. Finds the shocks and Triomes, which all have Swamp.
- **Cultivate:** one basic onto the battlefield tapped, one to hand.
- **Kodama's Reach:** a second copy of Cultivate.

### Protection

- **Lightning Greaves:** shroud and haste for {0} equip. Super-Skrull can
  activate abilities the turn he lands.
- **Swiftfoot Boots:** hexproof and haste; unlike Greaves, you can still
  target your own creature.
- **Heroic Intervention:** hexproof and indestructible for your permanents
  until end of turn.
- **Teferi's Protection:** phase out everything you control and gain
  protection from everything until your next turn.

### Interaction

- **Swords to Plowshares:** exile a creature for {W}.
- **Anguished Unmaking:** exile a nonland permanent for 3 life.
- **Utter End:** exile a nonland permanent.
- **Vindicate:** destroy any permanent at sorcery speed.
- **Beast Within:** destroy any permanent; its controller gets a 3/3.
- **Chaos Warp:** shuffle any permanent into its owner's library.
- **Toxic Deluge:** all creatures get -X/-X for X life. Pick X to kill
  their creatures while your 0/4 Walls survive.
- **Damnation:** destroy all creatures. Use it when behind.
- **Blasphemous Act:** 13 damage to each creature, cheaper for each
  creature on the battlefield. Use it when behind.

### Mana Base

36 lands, 11 basic. Urborg, Tomb of Yawgmoth makes every land a Swamp,
which fixes {B}{B}{B} and makes Cabal Coffers add {B} per land. Fetch
lands, Farseek and Prismatic Vista find shocks and Triomes, all of which
have the Swamp type.

### Mulligan

Keep hands with 3 or more lands (or 2 lands plus a rock or Birds of
Paradise) and at least one black source. A ramp spell or rock is worth
keeping over a clunky 5-drop.

### Turn Guide

1. **Turns 1-2:** lands, then Sol Ring, Arcane Signet, a Talisman, Birds
   of Paradise, or a ramp spell.
2. **Turn 3:** Rhystic Study, Skullclamp, Bitterblossom, or another setup
   piece.
3. **Turn 4:** Super-Skrull, ideally with Lightning Greaves, Swiftfoot
   Boots, or Heroic Intervention available.
4. **Turns 5-7:** spend spare mana on Walls or the draw-four. Deploy
   doublers and clones, and use the 4-damage ability to clear blockers.
5. **Turns 8-10:** win with +4/+4 attacks, Walls through Arcades or
   Assault Formation, Mirror Entity, or Walking Ballista.

### Cautions

- Toxic Deluge, Damnation and Blasphemous Act also kill your own tokens.
  Use them when behind.
- Red has the fewest sources. Keep one for the 4-damage ability.
- The draw-four can target anyone. Don't deck yourself late in a long
  game; aim it at an opponent when Sheoldred is out.
