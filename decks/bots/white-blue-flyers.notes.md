# White-blue flyers bot: Notes

Rules: [BOT_RULES.md](BOT_RULES.md). Library: 29 cards, no lands.

## Purpose

Tests defense against evasive creatures, plus Aura and enchantment removal
aimed at your engine pieces.

## Change Log

- 2026-10-05: Created for testing the Sigurd Saga counter burn deck.

## Primer

### Game Plan

The bot fills the air with flyers, adds a few removal Auras and enchantments
for your best permanents, and attacks with everything every turn. Each turn
it reveals cards until their total mana value reaches `turn + 1`, so early
flyers come out one or two at a time and Angels arrive around turns 4 to 6.
It has no lands, so it never holds up a trick. Race it only if your damage
engine is faster than its flyers, and otherwise stop the flyers first.

### Key Synergies

- **Anthems:** Glorious Anthem, Favorable Winds, and Pride of the Clouds
  make every small flyer larger.
- **Lifelink Angels:** Archangel of Thune, Baneslayer Angel, and Lyra
  Dawnbringer stretch the race.
- **Hero of Bladehold:** battle cry plus two attacking Soldier tokens each
  attack grows the ground force fast.
- **Token fodder:** Raise the Alarm gives the anthems and Hero more bodies.

### Small Flyers

- **Healer's Hawk:** 1/1 flying lifelink.
- **Suntail Hawk:** 1/1 flyer.
- **Spectral Sailor:** 1/1 flyer. The bot ignores its activated ability.
- **Stormfront Pegasus:** 2/1 flyer.
- **Pride of the Clouds:** a flyer that gets +1/+1 for each other flyer on
  the battlefield, yours included. The bot ignores forecast.
- **Pegasus Courser:** when it attacks, another attacking creature gains
  flying, so a ground attacker also flies.
- **Warden of Evos Isle:** a 2/2 flyer. Its cost reduction does nothing
  for a bot that does not pay mana, so treat it as a plain flyer.
- **Cloudkin Seer:** a 2/1 flyer. The bot ignores its card draw.
- **Thieving Magpie:** a flyer. The bot ignores its card draw.
- **Aven Mindcensor:** a 2/1 flyer with flash. If you search your library, you only
  look at the top four cards, which hurts Eladamri's Call and the tutors.

### Large Flyers and Ground Threats

- **Resplendent Angel:** a 3/3 flyer. It makes a 4/4 Angel at end of turn
  if the bot gained 5 or more life that turn.
- **Angel of Mercy:** a 3/3 flyer. It gains the bot 3 life.
- **Serra Angel:** a 4/4 flyer with vigilance.
- **Archangel of Thune:** a flyer with lifelink. Whenever the bot gains
  life, its creatures get +1/+1 counters.
- **Baneslayer Angel:** a 5/5 flyer with first strike and lifelink.
- **Lyra Dawnbringer:** a 5/5 flyer with first strike and lifelink. Other
  Angels get +1/+1 and lifelink.
- **Air Elemental:** a 4/4 flyer.
- **Mulldrifter:** a 2/2 flyer. The bot ignores its card draw.
- **Windreader Sphinx:** a 3/7 flyer. The bot ignores its draw trigger.
- **Hero of Bladehold:** battle cry. Whenever it attacks, it makes two 1/1
  Soldiers that attack too. A priority target for your removal.
- **Sentinel of the Eternal Watch:** vigilance. At the beginning of combat
  on your turn, it taps a creature you control, which is usually your best
  blocker or attacker.

### Removal and Auras

- **Swords to Plowshares:** exiles your best creature. You gain life equal
  to its power.
- **Path to Exile:** exiles your best creature. You may search for a basic
  land.
- **Journey to Nowhere:** exiles your highest mana value creature while it
  stays on the battlefield.
- **Pacifism:** goes on your creature with the highest power. It cannot
  attack or block.
- **Oblivion Ring:** exiles your highest mana value nonland permanent, so
  an engine piece or Saga will go.

### Tokens and Anthems

- **Raise the Alarm:** two 1/1 Soldiers.
- **Glorious Anthem:** the bot's creatures get +1/+1.
- **Favorable Winds:** the bot's flyers get +1/+1.

### Mulligan

The bot never mulligans. As the human, keep a hand with early blockers that
fly or reach, or a plan to kill the first flyers.

### Turn Guide

1. Turns 1-2: reveals 2 to 3 mana value. Hawks, Pegasus, and Spectral
   Sailor start chipping for 1 or 2.
2. Turn 3: reveals about 4 mana value. Two flyers or a removal spell
   aimed at your first creature.
3. Turns 4-5: reveals 5 to 6 mana value. Serra Angel, Archangel of Thune,
   or Hero of Bladehold. Anthems begin to show.
4. Turns 6-7: capped at 7. Baneslayer Angel and Lyra Dawnbringer swing the
   race with lifelink.

### Matchups and Cautions

- Your list has few flyers to block with. Your answers are All Will Be One
  damage, Swords to Plowshares, and Boros Charm.
- Oblivion Ring hits your highest mana value nonland permanent, so an
  engine piece or Saga will go. Journey to Nowhere and Pacifism hit Sigurd
  or your best creature.
- Lifelink Angels make the race longer. Count how many turns your damage
  engine needs.
- Anthems and Hero of Bladehold make the board grow quickly if you stall.
- Aven Mindcensor shrinks your tutors, so tutor before it appears if you can.
