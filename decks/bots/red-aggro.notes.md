# Red aggro bot: Notes

Rules: [BOT_RULES.md](BOT_RULES.md). Library: 31 cards, no lands.

## Purpose

Tests whether the Sigurd deck survives and builds a board before the engine
is online. Fast hasty creatures plus burn.

## Change Log

- 2026-10-05: Created for testing the Sigurd Saga counter burn deck.

## Primer

### Game Plan

The bot dumps cheap hasty creatures and burn every turn, then attacks with
everything. It has no lands and no hand, so it reveals cards until their
total mana value reaches `turn + 1` (Casual). Expect two or three cheap cards
per turn early and a 5-drop by turn 4 or 5. It never holds anything back and
never blocks unless a blocker kills the attacker and survives. Your job is to
stabilize the board and keep your life total above the burn.

### Key Synergies

- **Haste and Fervor:** Fervor gives the bot's creatures haste, so every
  creature it reveals attacks the same turn. The bot's hasty creatures do
  this already.
- **Hellrider:** each attacking creature pings you for 1, so a wide board
  hurts more than its combat damage.
- **Burn into your blockers:** damage spells that cannot kill a creature go
  at your face, so the bot clears blockers first and burns you with the rest.
- **Tokens:** Dragon Fodder, Hordeling Outburst, Krenko's Command, and
  Siege-Gang Commander widen the board for Hellrider and absorb removal.

### Cheap Creatures

- **Raging Goblin:** 1/1 haste for one mana. Chip damage on turn 1.
- **Zurgo Bellstriker:** 2/2 for one mana. It cannot block creatures with
  power 2 or greater. The bot ignores its dash cost.
- **Ash Zealot:** first strike and haste. Deals 3 damage to a player who
  casts a spell from a graveyard, which matters if you recur cards.
- **Goblin Piker:** a plain 2/1 body.
- **Boggart Brute:** menace, so it needs two blockers.
- **Brazen Scourge:** a hasty attacker.
- **Breakneck Berserker:** hasty attacker, usually 3 power.
- **Goblin Chainwhirler:** deals 1 damage to each creature and planeswalker
  you control when it enters, so it kills mana dorks, 1/1 tokens, and
  Avacyn's Pilgrim. It also has first strike.
- **Hill Giant:** a plain 3/3 body.

### Top-End Threats

- **Hellrider:** haste. Whenever a creature the bot controls attacks, it
  deals 1 damage to you.
- **Bloodcrusher of Khorne:** a trampler that gives its other creatures
  trample, so chump blocks leak damage.
- **Bloodsworn Steward:** a flyer. Its commander bonus does nothing in this
  deck, because the bot has no commander.
- **Furnace Whelp:** a flyer. The bot cannot pump it, so it is a small flyer.
- **Stormbreath Dragon:** flying and haste with protection from white.
  Block it with a flyer or take 4.
- **Thundermaw Hellkite:** flying and haste. When it enters, it deals 1
  damage to each flyer you control and taps them.
- **Charging Monstrosaur:** trample and haste. A hard hit on turn 5.
- **Fire Elemental:** a plain 5/4 body.
- **Siege-Gang Commander:** a 2/2 and three 1/1 Goblins. The bot cannot
  activate it.

### Burn Spells

The 3-damage spells all follow one rule: they kill your best creature
that 3 damage can kill, and otherwise hit your face.

- **Lightning Bolt:** {R} instant, 3 damage to any target.
- **Chain Lightning:** {R} sorcery, 3 damage. Whoever it hits may pay
  {R}{R} to copy it back at a new target.
- **Lightning Strike:** {1}{R} instant, 3 damage.
- **Searing Spear:** {1}{R} instant, 3 damage.
- **Incinerate:** {1}{R} instant, 3 damage, and the creature can't
  regenerate this turn.
- **Burst Lightning:** 2 damage to any target. The bot ignores kicker.
- **Flame Slash:** 4 damage to a creature only. Not cast if you have no
  creature, and it goes to the bottom of the library.
- **Roast:** 5 damage to a creature without flying. Same rule: no legal
  target means it is not cast.
- **Mizzium Mortars:** 4 damage to one of your creatures. Not cast without
  a target.

### Token Makers and Enablers

- **Fervor:** gives the bot's creatures haste.
- **Dragon Fodder:** two 1/1 Goblins.
- **Hordeling Outburst:** three 1/1 Goblins.
- **Krenko's Command:** two 1/1 Goblins.

### Mulligan

The bot never mulligans. As the human, keep a hand that plays a blocker on
turns 2 and 3 and holds protection for your best creature.

### Turn Guide

1. Turn 1: reveals about 2 mana value. Usually a 1-drop and maybe a second
   card. Expect 1 to 3 damage.
2. Turn 2: reveals about 3 mana value. Burn aims at any creature you played.
3. Turn 3: reveals about 4 mana value. Hasty 3-power creatures arrive.
4. Turns 4-5: reveals 5 to 6 mana value. The Dragons, Hellkite, or
   Monstrosaur land and attack at once. Thundermaw taps your flyers.
5. Turns 6-7: capped at 7 mana value. Your life total is the main resource.
   The bot attacks every turn with everything.

### Matchups and Cautions

- Burn deals 3, so Sigurd dies to a single bolt unless Swiftfoot Boots,
  Lightning Greaves, Heroic Intervention, or Teferi's Protection is ready.
- Goblin Chainwhirler kills Llanowar Elves, Birds of Paradise, and Avacyn's
  Pilgrim, so hold mana dorks until it is revealed or do not rely on them.
- Thundermaw Hellkite taps your flyers, so Norn's Choirmaster and other
  blockers cannot block that turn.
- Token makers test your early blockers and your Sagas that make bodies.
- Lifelink creatures (Sigurd, Garnet) are good here. Chump-blocking early
  with Saga tokens buys time to set up the engine.
