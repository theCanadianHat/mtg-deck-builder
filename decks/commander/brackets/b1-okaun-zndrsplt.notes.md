# B1 Okaun and Zndrsplt: Notes

## Goals

- Commanders: Okaun, Eye of Chaos and Zndrsplt, Eye of Wisdom (partner pair,
  Izzet).
- Part of a five-deck set, one per Commander bracket. This is Bracket 1
  (Exhibition).
- Archetype: coin-flip chaos. Fun and silliness over winning.

## Constraints

- Bracket 1: no Game Changers, no tutors, no infinite combos, no extra turns,
  no mass land destruction. Stitch in Time was left out for this reason.
- No budget (user proxies).
- Rest of the set: B2 Cosmic Spider-Man (tuned down), B3 Zaxara Hydras,
  B4 Super-Skrull (pushed up), B5 Kinnan (cEDH).

## Change Log

- 2026-10-15: First build. 35 lands, 6 mana rocks, 34 coin-flip cards.
  Checked for legality, color identity and Game Changers.
- 2026-10-21: Rebuilt the primer around role groups with a bullet per card,
  checked against cards/library.json.

## Primer

### Game Plan

Cast Okaun or Zndrsplt (Partner with fetches the other). At the beginning of
combat you flip coins until you lose. Each win doubles Okaun's size and draws
you a card, and both commanders trigger on every player's wins. Fill the
deck with other flip cards and enjoy the variance.

### Commanders

- **Okaun, Eye of Chaos:** a 3/3 for {4}{R}. At the beginning of combat on
  your turn, flip until you lose. Whenever any player wins a flip, double
  Okaun's power and toughness until end of turn. Three wins make him a
  24/24. Partner with fetches Zndrsplt from your library when he enters.
- **Zndrsplt, Eye of Wisdom:** a 1/4 for {4}{U} with the same combat
  flips. Whenever any player wins a flip, draw a card. Partner with
  fetches Okaun.

### Flip Enhancers

These make winning flips likelier or more common.

- **Krark's Thumb:** flip two coins and ignore one whenever you flip. "Flip
  until you lose" runs much longer. Top priority card.
- **Planar Chaos:** every player flips whenever they cast a spell and the
  spell is countered on a loss. Every player's wins trigger Okaun and
  Zndrsplt. It may leave on a lost upkeep flip.
- **Krark, the Thumbless:** flip whenever you cast an instant or sorcery.
  Win to copy it; lose and it returns to hand to recast (and flip again).
- **Ral, Monsoon Mage // Ral, Leyline Prodigy:** instants and sorceries
  cost {1} less, and each one you cast on your turn flips a coin. A win
  can transform him into a planeswalker whose −2 deals 2 damage divided
  and draws, and whose −8 casts free spells.
- **Breeches, the Blastmaker:** on your second spell each turn, sacrifice
  an artifact (a Treasure) and flip. Win to copy the spell; lose and it
  deals damage equal to the spell's mana value to any target.

### Flip Payoffs

These reward each win. They trigger on every flip from every other card.

- **Chance Encounter:** a luck counter whenever you win a flip. At ten or
  more at your upkeep, you win the game: the slow, silly win condition.
- **Tavern Scoundrel:** two Treasures whenever you win a flip. {1}, tap and
  sacrifice another permanent (a spare Treasure) to flip again.
- **Karplusan Minotaur:** 1 damage to any target on each win; on each loss
  an opponent aims 1 damage. Its cumulative upkeep is more flips.
- **Niv-Mizzet, Parun:** can't be countered. Pings for 1 whenever you draw,
  so every Zndrsplt draw is a ping. Also draws whenever anyone casts an
  instant or sorcery.

### Flip-Until-You-Lose Spells

High-variance swings. With Krark's Thumb, three or more wins are common.

- **Fiery Gambit:** flip until you lose or stop. One win deals 3 to a
  creature; two also deal 6 to each opponent; three also draw nine and
  untap your lands. Losing any flip fizzles it, so stop at a safe point.
- **Squee's Revenge:** pick a number and flip that many times. Win them
  all to draw two cards per flip.
- **Crazed Firecat:** a 4/4 that gets a +1/+1 counter per win on entry.
- **Mirror March:** whenever a nontoken creature enters, flip until you
  lose and make a hasty token copy per win, exiled at end step.
- **Game of Chaos:** you and an opponent flip with doubling life stakes.
  Stop after a win to keep the gain.

### Repeatable Flippers

Every activation is another chance at a commander trigger.

- **Goblin Artisans:** tap to flip; win to draw.
- **Goblin Bangchuckers:** tap to flip; win to deal 2 damage to any
  target, lose and it takes 2.
- **Goblin Festival:** {2} for 1 damage to any target and a flip. On a
  loss an opponent gains control of it, so use it while Krark's Thumb is
  out.
- **Frenetic Efreet:** a 2/1 flier. {0} to flip; win to phase out (dodge
  removal), lose and it is sacrificed.
- **Chaotic Goo:** enters with three counters and may flip each upkeep to
  gain or lose one.
- **Goblin Kaboomist:** a Land Mine token each upkeep, then a flip; on a
  loss it takes 2.
- **Skyclaw Thrash:** a 4/4 that flips on attack; win for +1/+1 and
  flying.
- **Goblin Psychopath:** a 5/5 that flips when it attacks or blocks; on a
  loss its combat damage hits you instead.
- **Mogg Assassin:** tap to flip; win to destroy your chosen opposing
  creature, lose to destroy the opponent's chosen one.
- **Molten Birth:** two 1/1 Elementals, and on a win it returns to hand to
  cast again.
- **Bottle of Suleiman:** {1} and sacrifice: win for a 5/5 flying Djinn,
  lose to take 5.
- **Sorcerer's Strongbox:** {2}, tap: win to sacrifice it and draw three.
- **Wirefly Hive:** {3}, tap: win for a 2/2 flying Wirefly, lose and every
  Wirefly is destroyed.
- **Crooked Scales:** {4}, tap: win to destroy an opposing creature; lose
  and pay {3} to try again or lose one of yours.
- **Goblin Lyre:** sacrifice: win to deal damage to an opponent equal to
  your creature count.

### Chaos Effects

Coin-themed cards that do not have win/lose flips. Mana Clash and Goblin
Assassin use heads and tails, so they do not count as winning a flip for
Okaun, Zndrsplt, Chance Encounter or Tavern Scoundrel.

- **Mana Clash:** you and an opponent flip until both come up heads; each
  tails deals 1 to its player.
- **Goblin Assassin:** whenever it or another Goblin enters, each player
  flips and each tails sacrifices a creature.
- **Puppet's Verdict:** a flip; win to destroy creatures with power 2 or
  less, lose to destroy power 3 or more. Cast it when the result helps
  either way.
- **Invert Polarity:** target a spell and flip; win to steal it, lose to
  counter it. Both outcomes stop an opponent's spell.
- **Boompile:** tap to flip; win to destroy all nonland permanents,
  including yours. A reset button when you are behind.

### Wizards and Spells

- **Goblin Electromancer:** instants and sorceries cost {1} less.
- **Young Pyromancer:** a 1/1 Elemental per instant or sorcery you cast.
- **Wizard's Lightning:** 3 damage to any target, {R} with a Wizard out
  (Krark, Ral, Niv-Mizzet or Goblin Electromancer).
- **Stormwing Entity:** a 3/3 prowess flier costing {2}{U} less after an
  instant or sorcery; scry 2.
- **Pestermite:** flash flier that taps or untaps a permanent.
- **Brazen Borrower // Petty Theft:** bounce an opposing nonland
  permanent, then cast the 3/1 flash flier later.
- **Shivan Dragon:** a 5/5 flier with firebreathing. Fair beats.
- **Air Elemental:** a 4/4 flier.
- **Mutalith Vortex Beast:** a 6/6 trampler that flips once per opponent
  on entry: draw on each win, 3 damage to that opponent on each loss.

### Card Advantage

- **Mulldrifter:** draw two, as a flier or evoked.
- **Fact or Fiction:** reveal five, an opponent splits them, you take a
  pile.
- **Divination:** draw two.
- **Wheel of Fortune:** everyone discards and draws seven. Refill after
  dumping your hand.
- **Jace Beleren:** +2 everyone draws; −1 you draw.
- **Chandra, Torch of Defiance:** +1 for a card or 2 damage to each
  opponent, +1 for {R}{R}, −3 for 4 damage to a creature.

### Mana

- **Sol Ring:** {C}{C} from turn one.
- **Arcane Signet:** {U} or {R}.
- **Izzet Signet:** {1} into {U}{R}.
- **Mind Stone:** {C}, and cash in for a card later.
- **Thought Vessel:** {C} and no maximum hand size for Zndrsplt draws.
- **Talisman of Creativity:** {U} or {R}.

### Interaction

- **Lightning Bolt:** 3 damage to any target for {R}.
- **Fire // Ice:** 2 damage split, or tap a permanent and draw.
- **Izzet Charm:** soft counter a noncreature spell, 2 damage to a
  creature, or loot two.
- **Abrade:** 3 damage to a creature or destroy an artifact.
- **Mizzium Mortars:** 4 damage to a creature, or overload for one-sided
  4 damage to each opposing creature.
- **Chaos Warp:** shuffle any permanent into its owner's library.
- **Counterspell:** counter any spell.
- **Negate:** counter a noncreature spell.

### Mana Base

35 lands, 23 basic. The Gold Saucer is another repeatable flipper
({2}, tap: win for a Treasure). Reliquary Tower removes the hand-size
limit for big Zndrsplt turns.

### Mulligan Guidance

Keep hands with 3 or more lands and either a mana rock or a cheap flip card.
A hand with Krark's Thumb is a keep. Do not keep hands that need both
commanders at once.

### Turn-by-Turn

- **Turns 1-2:** play a land and a rock (Sol Ring, Signet, Mind Stone).
- **Turn 3:** cheap flip creatures or enchantments, or Krark's Thumb.
- **Turn 4:** more flip permanents and card draw to find the commanders.
- **Turn 5+:** cast Okaun or Zndrsplt, fetch the other, and start flipping
  each combat.
- **Late game:** attack with a doubled Okaun, or race to ten luck counters
  with Chance Encounter. Expect to win around turns 9-12.
