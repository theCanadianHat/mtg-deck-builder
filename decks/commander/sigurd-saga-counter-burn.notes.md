# Sigurd Saga Counter Burn: Notes

Source: <https://moxfield.com/decks/SfegAQReqXu6lNYMAvBJoA>

## Goals

- Commander: Sigurd, Jarl of Ravensthorpe (Naya).
- Engine: Sagas generate lore counters. Sigurd turns each lore counter into a
  +1/+1 counter. Power Conduit (and similar) converts saga counters into
  +1/+1 counters. All Will Be One turns every counter placed into damage.
- Wants more Sagas.

## Constraints

- Heads-down engine deck. Prioritize protection over interaction.
- A little removal is fine (keep Swords to Plowshares); Saga-stapled removal preferred.
- Redesign is acceptable if needed, but keep the saga counter burn identity.
- No budget (user proxies), but every card must earn its slot.
- Casual table with some bracket 4 decks; power level is not a constraint.

## Change Log

- 2026-10-01: Cut Path to Exile, Beast Within, Generous Gift, Return to Nature,
  Heliod's Intervention, Farewell, Aura Shards, Touch the Spirit Realm,
  Esper Sentinel, Champion of Lambholt, Kodama of the West Tree, Sunhome.
  Added Garnet, Long List of the Ents, The First Iroan Games, Fall of the
  Impostor, Showdown of the Skalds, Song of Freyalise, Triumph of Gerrard,
  Kumano Faces Kakkazan, Arni Slays the Troll, Norn's Choirmaster,
  Clash of the Eikons, Karn's Bastion.
- 2026-10-01: Cut Herald of the Pantheon, Forgotten Ancient, Triumph of Gerrard,
  Rogue's Passage, Myriad Landscape. Added Casey Jones, Back Alley Brute (second
  damage payoff), Metastatic Evangel, Pollenbright Druid, Storyweave,
  Unbounded Potential. Lands 36 -> 34.
- 2026-10-21: Split the mana primer into a bullet per card and added Delighted
  Halfling, checked against cards/library.json.
- 2026-10-01: Cut Jeska's Will, Smothering Tithe. Added Eladamri's Call
  (creature tutor), Huatli's Raptor (proliferate).

## Primer

### Game Plan

Sagas put lore counters on the table, and Sigurd turns each lore counter into
a +1/+1 counter on another creature. Counter doublers (Hardened Scales,
Branching Evolution, Conclave Mentor, Kami of Whispered Hopes, Ozolith, the
Shattered Spire) make every counter bigger. A payoff (All Will Be One,
Shalai and Hallar, Casey Jones) turns each counter into damage to an
opponent. Heads down: protect Sigurd, set up the engine, then deploy a payoff
when you can hold up protection or the table is tapped out.

### Key Synergies

- **Engine priority:** Sigurd plus protection, then a counter doubler, then
  cheap Sagas to keep lore counters flowing, then a payoff.
- **How the damage adds up:** All Will Be One triggers once per permanent or
  player you put counters on, including lore counters. One Saga chapter with
  Sigurd, Hardened Scales, and all three payoffs: the lore counter (1 from
  All Will Be One), then Sigurd adds 1+1 = 2 +1/+1 counters (2 from All Will
  Be One, 2 from Shalai and Hallar, 2 from Casey).
- **Proliferate:** hits every Saga and every creature with counters at once,
  and each lore counter added triggers Sigurd again. You choose what gets
  counters, so skip opponents' permanents.
- **The Saga loop:** a Saga is sacrificed only after its final chapter
  ability has left the stack and it still has lore counters at or above its
  final chapter number.
  - With the final chapter trigger on the stack, tap Power Conduit to remove
    a lore counter. The Saga survives, and Conduit puts a +1/+1 counter on a
    creature.
  - Next turn's lore counter (or Sigurd's Boast, Storyweave, or Satsuki)
    triggers the final chapter again.
  - Clash of the Eikons: choose "remove" and "put" together to replay the
    current chapter at sorcery speed.
  - Garnet: on attack, remove lore counters from Sagas you want to replay and
    get a +1/+1 counter for each one.
  - Weaver of Harmony copies a chapter trigger, since Sagas are enchantments.
- **Counter shuffling:** The Ozolith keeps counters from creatures that die,
  and Nesting Grounds moves counters between permanents at sorcery speed.

### Commander

- **Sigurd, Jarl of Ravensthorpe:** vigilance, trample, and lifelink. Boast
  ({1}) adds or removes a lore counter on a Saga after he attacks. Whenever
  you put a lore counter on a Saga you control, put a +1/+1 counter on up to
  one other target creature.

### Sagas

- **Arni Slays the Troll:** I fights, II adds {R} and puts two +1/+1
  counters on a creature, III gains life equal to your greatest power.
- **Battle for Bretagard:** I and II make a 1/1 Human Warrior and a 1/1 Elf
  Warrior, and III copies tokens with different names. Cheap bodies for
  counters.
- **Elspeth Conquers Death:** I exiles an opponent's permanent with mana
  value 3 or more, II taxes noncreature spells, and III returns a creature or
  planeswalker from your graveyard.
- **Fable of the Mirror-Breaker:** I makes a 2/2 Goblin Shaman that makes
  Treasure, II loots up to two cards, and III transforms into Reflection of
  Kiki-Jiki.
- **Fall of the Impostor:** I and II put a +1/+1 counter on a creature, and
  III exiles an opponent's creature with the greatest power.
- **Kumano Faces Kakkazan:** I pings each opponent for 1, II gives your next
  creature spell an extra +1/+1 counter, and III transforms into Etching of
  Kumano.
- **Long List of the Ents:** six chapters, each noting a creature type so
  your next creature spell of that type enters with an extra +1/+1 counter.
  It stays on the battlefield the longest, so it feeds Sigurd for many turns.
- **Showdown of the Skalds:** I exiles the top four cards you may play, and
  II and III put a +1/+1 counter on a creature whenever you cast a spell.
- **Song of Freyalise:** I and II let your creatures tap for mana, and III
  puts a +1/+1 counter on each creature you control.
- **Teachings of the Kirin:** I mills three and makes a 1/1 Spirit, II puts a
  +1/+1 counter on a creature, and III transforms into Kirin-Touched Orochi.
- **The Akroan War:** I steals a creature while the Saga stays, II forces
  opposing creatures to attack, and III makes tapped creatures damage
  themselves.
- **The Elder Dragon War:** I deals 2 to each creature and each opponent, II
  rummages, and III makes a 4/4 flying Dragon. Use read ahead to skip
  chapter I when you have mana creatures.
- **The First Iroan Games:** I makes a 1/1 Soldier, II puts three +1/+1
  counters on a creature, III draws two with a power 4 creature, and IV makes
  a Gold token.
- **The Restoration of Eiganjo:** I fetches a Plains, II discards a card to
  return a permanent with mana value 2 or less, and III transforms into
  Architect of Restoration.
- **There and Back Again:** I stops a creature from blocking and the Ring
  tempts you, II fetches a Mountain onto the battlefield, and III makes
  Smaug, a 6/6 flying haste Dragon.
- **Urza's Saga:** a mana source on chapter I, a Construct maker on II, and
  III fetches a zero or one cost artifact such as Sol Ring.

Double-faced Sagas (Fable, Kumano, Teachings, Restoration) exile and
transform on chapter III instead of being sacrificed.

### Counter Doublers and Engines

- **Hardened Scales:** +1 on each batch of +1/+1 counters, which Sigurd's
  triggers feed.
- **Branching Evolution:** doubles +1/+1 counters placed on your creatures.
- **Conclave Mentor:** +1 on counter batches. It gains you life equal to its
  power when it dies.
- **Kami of Whispered Hopes:** +1 on counter batches and taps for mana equal
  to its power.
- **Ozolith, the Shattered Spire:** +1 on counter batches for artifacts and
  creatures, plus an activated counter at sorcery speed, and cycling.
- **The Ozolith:** stores counters from creatures that die and moves them to
  another creature at your next combat.
- **Power Conduit:** removes a counter from a permanent you control to put
  a +1/+1 counter on a creature, which is the core of the Saga loop.
- **Nesting Grounds:** a land that moves a counter between permanents at
  sorcery speed.
- **Storyweave:** two +1/+1 counters on a creature, or two lore counters on a
  Saga. Lore counters trigger Sigurd.
- **Unbounded Potential:** a +1/+1 counter on up to two creatures, or
  proliferate, or both with entwine.
- **Invigorating Hot Spring:** an enchantment with four +1/+1 counters it
  can hand out once each turn at sorcery speed, and it gives haste to
  modified creatures.

### Proliferate Pieces

- **Evolution Sage:** proliferates on each land you play.
- **Grateful Apparition:** a flyer that proliferates on combat damage.
- **Huatli's Raptor:** proliferates when it enters and has vigilance.
- **Metastatic Evangel:** proliferates whenever another nontoken creature
  enters under your control.
- **Norn's Choirmaster:** a flying first strike creature that proliferates
  whenever your commander enters or attacks.
- **Pollenbright Druid:** a +1/+1 counter on a creature, or proliferate.
- **Karn's Bastion:** a land that proliferates for {4}.

### Payoffs

- **All Will Be One:** damage to an opponent, one of their creatures, or a
  planeswalker for each counter you put on a permanent or player.
- **Shalai and Hallar:** a flying vigilance creature that deals damage equal
  to the +1/+1 counters put on your creatures.
- **Casey Jones, Back Alley Brute:** menace, adds a counter when it attacks,
  and deals damage equal to +1/+1 counters put on your creatures.
- **Garnet, Princess of Alexandria:** lifelink. Removes lore counters from
  Sagas on attack to grow herself and replay chapters.
- **Satsuki, the Living Lore:** taps to add a lore counter to every Saga at
  sorcery speed, and returns a Saga when it dies.
- **Weaver of Harmony:** enchantment creatures get +1/+1, and it copies
  chapter triggers.
- **Clash of the Eikons:** a fight and lore counter manipulation, in any
  combination.

### Creatures and Value Engines

- **Luminarch Aspirant:** a counter on a creature at the start of your
  combat, which Sigurd does not trigger but doublers do.
- **Managorger Hydra:** trample, and it grows with every spell cast.
- **Mikaeus, the Lunarch:** enters with X counters and pumps your team.
- **Sun Titan:** returns a permanent with mana value 3 or less on enter and
  attack, such as a Saga or mana dork.
- **Sythis, Harvest's Hand:** gains 1 life and draws a card on each
  enchantment spell, including Sagas.
- **Starfield Mystic:** enchantment spells cost {1} less, and it grows when
  an enchantment goes to the graveyard.
- **Jukai Naturalist:** lifelink, and enchantment spells cost {1} less.
- **Sanctum Weaver:** taps for mana equal to the number of enchantments you
  control.

### Tutors

- **Enlightened Tutor:** puts an artifact or enchantment on top of your
  library. Finds All Will Be One, a doubler, or Swiftfoot Boots.
- **Idyllic Tutor:** fetches an enchantment into your hand. Finds All Will Be
  One, a Saga, or a doubler.
- **Eladamri's Call:** fetches any creature. Finds Shalai and Hallar, Casey
  Jones, Garnet, or Satsuki.

### Protection and Interaction

- **Swiftfoot Boots:** hexproof and haste for Sigurd.
- **Lightning Greaves:** haste and shroud, with equip {0}.
- **Heroic Intervention:** gives your permanents hexproof and indestructible
  for a turn. Hold it up before you deploy a payoff.
- **Teferi's Protection:** a full protection turn, but your permanents phase
  out. Use it as a last resort.
- **Boros Charm:** four damage to a player, indestructible permanents, or
  double strike.
- **Darksteel Plate:** an indestructible artifact, equip {2}.
- **Shield of the Oversoul:** an Aura that gives a green creature +1/+1 and
  indestructible, or a white creature +1/+1 and flying.
- **Swords to Plowshares:** the one flexible removal spell.

### Mana

Early mana gets Sigurd and the first Saga down a turn sooner. The mana
creatures also carry counters, but they die to sweepers.

- **Sol Ring:** {C}{C} for {1}. The best turn-one play.
- **Arcane Signet:** one mana of any color in Sigurd's identity.
- **Llanowar Elves:** {G} on turn one.
- **Birds of Paradise:** any color, and flies, so it can carry counters
  over blockers.
- **Avacyn's Pilgrim:** {W}, which helps cast white cards off a
  Forest-heavy hand.
- **Delighted Halfling:** {C}, or any color for a legendary spell that
  then can't be countered. Use it to land Sigurd and legendary Sagas
  through counterspells.
- **Nature's Lore:** puts a Forest onto the battlefield untapped. It can
  fetch Stomping Ground, Temple Garden, Canopy Vista or Cinder Glade, not
  just a basic.
- **Three Visits:** a second Nature's Lore.
- **Fetch lands:** Arid Mesa, Windswept Heath, and Wooded Foothills thin the
  deck and find dual lands.
- **Terramorphic Expanse and Evolving Wilds:** fetch a basic land onto the
  battlefield tapped.
- **Ash Barrens:** a colorless land that can basic landcycle for {1}.
- **Command Tower and Exotic Orchard:** fix all three colors.
- **Dual lands:** Sacred Foundry, Stomping Ground, Temple Garden, Clifftop
  Retreat, Rootbound Crag, Sunpetal Grove, Canopy Vista, and Cinder Glade.
- **Filter lands:** Fire-Lit Thicket and Rugged Prairie.
- **Utility lands:** Kessig Wolf Run turns extra mana into a pump with
  trample, Karn's Bastion and Nesting Grounds are above, and Urza's Saga is
  a Saga.
- **Basics:** 6 Forest, 3 Mountain, and 3 Plains.

### Mulligan

Keep hands with 3+ lands (or 2 lands plus a mana creature) and at least one
Saga or engine piece. Tutors count as engine pieces.

### Turn Guide

1. Turns 1-2: play lands and mana creatures, then a cheap Saga or Sol Ring.
2. Turn 3: Sigurd with Swiftfoot Boots or Lightning Greaves, or a counter
   doubler.
3. Turn 4: Sagas and another doubler. Tutor for All Will Be One if you can
   protect it.
4. Turns 5-6: add proliferate, Power Conduit, and the Saga loop. Deploy a
   payoff when you hold Heroic Intervention, Teferi's Protection, or Boros
   Charm, or when the table is tapped out.
5. Turns 7+: attack with Sigurd and loop chapters until the damage kills the
   table.

### Matchups and Cautions

- The Elder Dragon War chapter I deals 2 to each creature, including your
  mana creatures. Use read ahead to skip to chapter II or III when needed.
- The Ozolith keeps counters from creatures that die, and Sun Titan returns
  Sagas with mana value 3 or less from the graveyard.
- Against sweepers, keep Sagas on the table and hold Heroic Intervention.
- Against aggro bots, chump-block early with Saga tokens while the engine
  builds.
