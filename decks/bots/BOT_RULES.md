# Bot opponent rules

A bot is a library with no hand, no lands, and no decisions. You shuffle it,
flip cards on its turn, and follow the rules below. It exists to give your
real deck something to play against.

## Setup

- Shuffle the bot library face down. Starting life is 40.
- The bot has no mulligan, no hand, and no commander.
- Count the bot's own turns: its first turn is turn 1.
- In a pod, the bot attacks you only. Use a die to pick if there are several
  real players.

## The bot's turn

1. Untap. The bot does not draw.
2. Reveal cards from the top until their total mana value is at least
   `turn + 1`, capped at 7. This replaces mana. The last card may overshoot.
3. Cast every revealed card, in the order revealed.
4. Attack with every creature that can attack.

Dials, for how hard the bot hits:

| Mode   | Reveal until total is at least | Cap |
|--------|--------------------------------|-----|
| Casual | `turn + 1`                     | 7   |
| Clock  | `turn + 3`                     | 9   |

Start on Casual. Move to Clock once your deck can stabilize against it.

## Resolving cards

- Creatures, artifacts, and enchantments enter the battlefield. Creatures
  with haste attack the turn they enter. Others attack next turn.
- Ignore every activated ability, because the bot has no mana. Also ignore
  morph, kicker, echo, evoke, delve cost reduction, monstrosity, exert,
  forecast, and any "may" effect that helps only the bot.
- Ignore card draw, scry, and library search the bot would do. Apply life
  gain, life loss, discard, counters, damage, and tokens.
- Static abilities and triggers always apply, including ones that hurt the
  bot.
- Instants and Auras are cast on the bot's turn only. The bot never responds
  on your turn.

### Targets

- Creature removal targets your creature with the highest mana value. Break
  ties by highest power, then your choice.
- Removal that can hit any nonland permanent targets your highest mana value
  nonland permanent.
- Damage to "any target" kills the best creature it can kill. If it can't kill
  one, it goes at your face.
- "Target opponent discards" or "puts a card from hand" means you choose which
  card.
- A card with no legal target is not cast. Put it on the bottom of the bot
  library and keep revealing. It does not count toward the total.
- Pacifism goes on your creature with the highest power.
- Anthems and static boosts apply to the bot's creatures.

## Combat

- Attacks: every creature that can attack does, at you.
- Blocks: the bot blocks an attacker when its blocker kills the attacker and
  survives. It chump blocks only to prevent lethal damage. Assign blockers to
  the biggest attackers first.
- Damage and abilities work as written.

## When the library runs out

The bot has no further turns that reveal cards. Its creatures keep attacking
and blocking.

## Logging

For each game, record the turn the bot's first threat appeared, the turn your
engine came online, and the turn the game ended. Compare across bots and
modes to see how fast your deck is.
