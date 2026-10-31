# Black removal bot: Notes

Rules: [BOT_RULES.md](BOT_RULES.md). Library: 30 cards, no lands.

## Purpose

Tests protection. The bot kills your best creature almost every turn, so an
engine with no backup shows up immediately.

## Change Log

- 2026-10-05: Created for testing the Sigurd Saga counter burn deck.

## Primer

### Game Plan

The bot kills your best creature on almost every turn and backs it with
deathtouch and lifelink bodies. Each turn it reveals cards until their total
mana value reaches `turn + 1`, then casts them all. Removal with no legal
target is not cast, so it goes to the bottom, which means the bot's removal
only shows up once you have something to hit. Plan to lose your first
threat, and keep a protection spell for the next one.

### Key Synergies

- **Enter-the-battlefield removal:** Skinrender, Ravenous Chupacabra,
  Nekrataal, and Shriekmaw kill a creature and leave a body behind.
- **Targets:** removal picks your highest mana value creature, then highest
  power. Keep a cheap decoy only when you want it to take the hit.
- **Lifelink and drain:** Vampire Nighthawk, Gifted Aetherborn, Kalitas,
  and Gray Merchant gain life, so a long race favors the bot.
- **Deathtouch blockers:** they trade with any attacker, so one big creature
  cannot attack through them.

### Cheap Creatures

- **Typhoid Rats:** 1/1 deathtouch. It trades with your biggest attacker.
- **Vampire of the Dire Moon:** 1/1 deathtouch and lifelink.
- **Gifted Aetherborn:** 2/3 deathtouch and lifelink.
- **Black Knight:** 2/2 first strike with protection from white, so your
  white creatures cannot block it.
- **Vampire Nighthawk:** flying, deathtouch, and lifelink.
- **Hypnotic Specter:** a flyer. When it deals damage to you, you discard a
  card at random.
- **Rotting Regisaur:** a very large body for three mana. Its upkeep
  discard does nothing to a bot with no hand.
- **Liliana's Specter:** a flyer. When it enters, you discard a card of your
  choice.
- **Chittering Rats:** when it enters, you put a card from your hand on top
  of your library. You choose the card.

### Creature Removal on a Body

- **Skinrender:** puts three -1/-1 counters on your creature when it
  enters. Kills most things you cast early.
- **Ravenous Chupacabra:** destroys a creature you control when it enters.
- **Nekrataal:** destroys a nonartifact, nonblack creature of yours when it
  enters. It has first strike. An indestructible creature survives it.
- **Shriekmaw:** destroys a nonartifact, nonblack creature of yours when it
  enters, and it has fear. The bot ignores evoke.
- **Massacre Wurm:** your creatures get -2/-2. You lose 2 life for each
  creature that dies. It wipes small mana creatures and tokens.

### Big Threats

- **Sheoldred, the Apocalypse:** deathtouch. You lose 2 life each time you
  draw a card. The bot never draws, so its lifegain never triggers.
- **Phyrexian Obliterator:** you sacrifice a permanent for each point of
  damage dealt to it. All Will Be One damage counts, so do not target it.
- **Kalitas, Traitor of Ghet:** lifelink. Your nontoken creatures that die
  are exiled instead, and the bot gets a 2/2 Zombie. Recursion with Sun
  Titan does not work on them.
- **Gray Merchant of Asphodel:** drains you for the bot's devotion to black.
  It is stronger the more black permanents the bot has.
- **Sengir Vampire:** a flyer that grows when creatures die.
- **Grave Titan:** deathtouch, plus two Zombies when it enters and again
  each time it attacks.
- **Gurmag Angler:** a large body. The bot ignores delve, so it simply
  counts as a card to reveal.

### Removal Spells

- **Doom Blade:** destroys a nonblack creature. Hits Sigurd.
- **Go for the Throat:** destroys a nonartifact creature.
- **Murder:** destroys any creature.
- **Terror:** destroys a nonartifact, nonblack creature.
- **Hero's Downfall:** destroys a creature or planeswalker.
- **Dismember:** gives a creature -5/-5. It targets, so Swiftfoot Boots or
  Lightning Greaves stops it, but it kills most creatures otherwise.
- **Feed the Swarm:** destroys a creature or enchantment you control, and
  it can hit a Saga or All Will Be One.
- **Vraska's Contempt:** exiles a creature or planeswalker you control, so
  The Ozolith does not help.

### Discard

- **Mind Rot:** you discard two cards. You choose them.

### Mulligan

The bot never mulligans. As the human, keep hands with a threat and a
protection piece, plus a cheap creature to bait removal.

### Turn Guide

1. Turns 1-2: reveals 2 to 3 mana value. Usually a deathtouch body or a
   removal spell with no target, which goes to the bottom.
2. Turn 3: reveals about 4 mana value. A flyer or a Skinrender-style
   creature. Your best creature starts dying.
3. Turns 4-5: reveals 5 to 6 mana value. Sheoldred, Kalitas, Grave Titan,
   or Massacre Wurm may appear. Lifelink starts to swing the race.
4. Turns 6-7: capped at 7. Gray Merchant and Obliterator land. The bot
   attacks with everything each turn.

### Matchups and Cautions

- Sigurd is legendary and a high mana value target, so he is the first
  thing removal hits. Track how often Boots, Greaves, Heroic Intervention,
  and Teferi's Protection save him.
- Hexproof from Boots or shroud from Greaves stops targeted removal and
  Dismember, but not Massacre Wurm or Gray Merchant. Heroic Intervention
  and Teferi's Protection cover the wider cases.
- Do not attack into Phyrexian Obliterator with damage sources you rely on.
- Spread the engine across several permanents, because each removal spell
  kills one thing.
