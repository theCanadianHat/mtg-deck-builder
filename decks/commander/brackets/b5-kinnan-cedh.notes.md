# B5 Kinnan cEDH: Notes

## Goals

- Commander: Kinnan, Bonder Prodigy (Simic, {G}{U}).
- Part of a five-deck set, one per Commander bracket. This is Bracket 5 (cEDH).
- Archetype: fast mana and mana-creature ramp that turns into a combo win.
  Win on turns 3-5, or earlier with a strong draw.

## Constraints

- Bracket 5: no Game Changer limit. 19 Game Changers are in the list.
- No budget (user proxies). The list is about $1,970 at current prices.
- Mana Crypt, Jeweled Lotus and Tinker are banned in Commander, so they are
  not in the deck.
- Noble Hierarch is out because its white identity does not fit Kinnan.
- Rest of the set: B1 Okaun and Zndrsplt, B2 Cosmic Spider-Man (tuned down),
  B3 Zaxara Hydras, B4 Super-Skrull (pushed up).

## Change Log

- 2026-10-15: First build. 17 lands, 15 fast-mana pieces, 13 mana creatures,
  about 14 counterspells and protection spells. Checked for legality and color
  identity.
- 2026-10-21: Added commander, engine-helper, fast-mana, mana-creature, card
  advantage and mana-base groups with a bullet per card, checked against
  cards/library.json. Fixed the Daze bullet (always free).

## Primer

### Game Plan

Kinnan adds one extra mana of the same type whenever you tap a nonland
permanent for mana. Each rock or mana creature therefore makes one more mana
than normal (Sol Ring makes three, Basalt Monolith four). Use that mana to
assemble an infinite-mana engine, then convert it to a win. Hold up free
counterspells to protect the combo turn.

### Commander

- **Kinnan, Bonder Prodigy:** {G}{U}. Whenever you tap a nonland permanent
  for mana, add one more mana of a type it produced. {5}{G}{U}: look at the
  top five cards and put a non-Human creature from among them onto the
  battlefield. Free counterspells (Fierce Guardianship) key off him.

### Mana engines

Infinite mana is a resource, not a win. These combos create it.

- **Basalt Monolith with Rings of Brighthearth:** activate Monolith's untap
  ({3}) and pay {2} to copy it with Rings. Both untaps resolve, so you tap
  twice for {C}{C}{C} each (six mana, or eight with Kinnan) against a cost
  of {5}. That nets +1 colorless per loop (+3 with Kinnan), so it is
  infinite mana, with or without Kinnan.
  - **Sequencing:** start with Monolith tapped and {5} available (the first
    tap's {C}{C}{C} plus {2} extra).
    1. Activate untap, paying {3}. Rings of Brighthearth triggers.
    2. Pay {2} to copy the ability. The stack, top first, is: copy of untap,
       original untap.
    3. The copy resolves, so Monolith untaps. Tap it for {C}{C}{C}. Mana
       abilities don't use the stack.
    4. The original resolves, so Monolith untaps again. Tap it for
       {C}{C}{C}.
    5. Monolith is tapped again and you hold the mana from two taps. Repeat
       from step 1.
- **Isochron Scepter with Dramatic Reversal:** the Scepter copies Reversal
  for {2}, untapping all your nonland permanents including itself. It is
  infinite when your rocks and mana creatures tap for more than {2} in
  total (Kinnan adds one mana per permanent).
- **Power Artifact with Basalt Monolith or Grim Monolith:** cheaper untap, so
  infinite mana.

### Mana sinks

These spend the mana and turn it into resources.

- **Walking Ballista:** pay {4} per counter, then remove counters to deal
  damage to any target.
- **Staff of Domination:** pay {5} and tap to draw a card, and untap it with
  {1}. This draws your whole library.
- **Hullbreaker Horror:** flash, can't be countered. Each spell you cast
  can bounce a spell you don't control or any nonland permanent. With the
  Isochron Scepter loop, every Dramatic Reversal copy is a cast spell, so
  you bounce every opposing permanent and protect your win.
- **Kinnan's ability:** with infinite mana, activate {5}{G}{U} over and
  over to put every non-Human creature in the top of your library onto the
  battlefield: Craterhoof Behemoth, Hullbreaker Horror and Thassa's Oracle
  are all non-Human. (Walking Ballista would enter with no counters and
  die, so cast it instead.)

### Win conditions

- **Walking Ballista:** infinite counters deal infinite damage to every
  opponent.
- **Thassa's Oracle:** wins when your devotion to blue is at least your
  library size. Cast it after drawing out your library with Staff of
  Domination.
- **Laboratory Maniac:** if you would draw from an empty library, you win
  instead. Draw out your deck with Staff of Domination or another draw
  engine.
- **Craterhoof Behemoth:** needs {G}{G}{G}. Your creatures get +X/+X and
  trample, where X is your creature count. Win with a wide board of mana
  creatures.
- **Jace, Wielder of Mysteries:** if you would draw from an empty library,
  you win instead. A second Laboratory Maniac that is a planeswalker, so
  creature removal can't stop it. Its −8 draws seven and wins on an empty
  library.
- **Backup plan:** if no combo comes together, grind with the card
  advantage engines below.

### Tutors

- **Mystical Tutor:** an instant or sorcery to the top of your library,
  usually Dramatic Reversal for Isochron Scepter or a counterspell to
  protect the combo.
- **Worldly Tutor:** a creature to the top of your library. Targets are
  Craterhoof Behemoth, Walking Ballista, Laboratory Maniac, Thassa's Oracle,
  Hullbreaker Horror and Eternal Witness.
- **Green Sun's Zenith:** a green creature with mana value X. Fetch a mana
  creature to fuel Kinnan, Eternal Witness (X=3), or Craterhoof Behemoth when
  you have {X}{G} for X=8.
- **Chord of Calling:** a creature straight onto the battlefield at instant
  speed. Convoke with your mana creatures to reach Hullbreaker Horror (X=7)
  or Craterhoof Behemoth (X=8).
- **Survival of the Fittest:** any creature to hand, for a discarded
  creature. Finds Thassa's Oracle, Laboratory Maniac, Walking Ballista or
  Craterhoof Behemoth.
- **Natural Order:** sacrifice a green creature (a mana creature) to put
  Craterhoof Behemoth onto the battlefield.
- **Crop Rotation:** sacrifice a land to fetch Ancient Tomb for burst mana, or
  Boseiju, Who Endures to remove an opposing artifact or enchantment.
- **Spellseeker:** an instant or sorcery with mana value 2 or less when it
  enters. Finds Dramatic Reversal, Pact of Negation or a cheap counterspell.
- **Intuition:** three cards, and an opponent picks one for your hand. Name
  three combo pieces, or two pieces plus Eternal Witness to recover the rest
  from the graveyard.
- **Gifts Ungiven:** four cards, and an opponent picks two for your
  graveyard. Name Eternal Witness plus combo pieces so any split still works.

### Interaction

Free spells (Force of Will, Force of Negation, Misdirection, Snapback) each
exile a blue card from your hand, so keep a spare blue card.

- **Force of Will:** counter any spell. Free for a blue card and 1 life.
- **Fierce Guardianship:** counter a noncreature spell. Free while Kinnan is
  on the battlefield.
- **Force of Negation:** counter a noncreature spell. Free on an opponent's
  turn, so use it to stop their combo while you are tapped out.
- **Pact of Negation:** free counter on the combo turn. You must pay
  {3}{U}{U} next upkeep, so cast it only when you win first.
- **Mana Drain:** counter any spell, then add that much colorless mana next
  main phase. Good early to ramp.
- **Counterspell:** counter any spell for {U}{U}.
- **Mana Leak:** counter a spell unless its controller pays {3}. Best early
  while opponents are tapped low.
- **Memory Lapse:** counter a spell and put it on top of the library, so the
  opponent loses their next draw.
- **Daze:** return an Island instead of paying, to counter a spell unless
  its controller pays {1}. Best early, when opponents tap out for fast
  mana.
- **Swan Song:** counter an enchantment, instant or sorcery for {U}. The
  opponent gets a 2/2 Bird.
- **Mental Misstep:** counter a spell with mana value 1 for 2 life. Hits cheap
  fast mana and one-mana tutors.
- **Spell Pierce:** counter a noncreature spell unless its controller pays
  {2}. Cheap protection for the combo turn.
- **Flusterstorm:** counter an instant or sorcery unless its controller pays
  {1}. Copies with storm when you cast several spells in a turn.
- **Misdirection:** change the target of a spell with a single target. Free
  protection for Kinnan against targeted removal.
- **Heroic Intervention:** your permanents gain hexproof and indestructible
  until end of turn. Protects Kinnan and the combo board from removal and
  wipes.
- **Snapback:** return a creature to hand. Free for a blue card, so save
  Kinnan or Eternal Witness from removal, or rebuy an enter-the-battlefield
  effect.
- **Cyclonic Rift:** return a nonland permanent to hand for {1}{U}. Overload
  at {6}{U} bounces every opposing nonland permanent, clearing the way for
  your combo turn.

### Engine Helpers

These untap your mana sources, which Kinnan turns into extra mana.

- **Thousand-Year Elixir:** your creatures can use tap abilities the turn
  they enter, so new mana creatures tap at once. {1} and tap untaps a
  creature: untapping Bloom Tender or Priest of Titania nets mana.
- **Seedborn Muse:** untap all your permanents during each other player's
  untap step. Your rocks and creatures untap every turn (not Basalt
  Monolith or Mana Vault, which skip untap steps),
  so you can hold up counterspells and still combo on your turn.
- **Quirion Ranger:** once each turn, return a Forest to hand to untap a
  creature. Untap your best mana creature, then replay the Forest.
- **Wirewood Symbiote:** once each turn, return an Elf to hand to untap a
  creature. Return an Elf mana creature after tapping it, then recast it.
- **Eternal Witness:** return a used combo piece or counterspell to hand.

### Fast Mana

Each rock taps for one more with Kinnan out.

- **Sol Ring:** {C}{C} for {1}; three mana with Kinnan.
- **Mana Vault:** {C}{C}{C} for {1}. Doesn't untap normally (pay {4} at
  upkeep) and deals 1 damage while tapped at your draw step.
- **Chrome Mox:** free; imprint a green or blue card for that color.
- **Mox Diamond:** free if you discard a land; any color.
- **Mox Amber:** free; taps for a color among your legendary creatures and
  planeswalkers. Needs Kinnan, Jace or Narset out.
- **Lotus Petal:** free, sacrifice for any color. Burst mana for a turn-one
  Kinnan.
- **Mind Stone:** {C}, and sacrifice for a card later.
- **Worn Powerstone:** enters tapped, then {C}{C}.
- **Arcane Signet:** {G} or {U}.
- **Simic Signet:** {1} into {G}{U}; with Kinnan it nets two.
- **Talisman of Curiosity:** {C}, or {G} or {U} for 1 damage.
- **Fellwar Stone:** a color an opponent's land could make.
- **Springleaf Drum:** tap it and an untapped creature for any color. Lets
  a summoning-sick creature pay for spells.

### Mana Creatures

Each creature taps for one more with Kinnan out, and they are Natural
Order and Craterhoof Behemoth fodder.

- **Birds of Paradise:** a flying dork of any color.
- **Delighted Halfling:** {C}, or any color for legendary spells that then
  can't be countered. Protects Kinnan from counterspells.
- **Llanowar Elves:** {G}. An Elf for Priest of Titania and Wirewood
  Symbiote.
- **Elvish Mystic:** a second Llanowar Elves.
- **Fyndhorn Elves:** a third Llanowar Elves.
- **Gilded Goose:** sacrifice a Food for any color; enters with one Food.
- **Sylvan Caryatid:** a hexproof dork of any color.
- **Paradise Druid:** any color; hexproof while untapped.
- **Bloom Tender:** one mana of each color among your permanents, usually
  {G}{U} (three mana with Kinnan).
- **Priest of Titania:** {G} for each Elf on the battlefield, including
  your opponents' Elves.
- **Wall of Roots:** {G} once each turn without tapping, even on an
  opponent's turn. Kinnan does not add to it, because it doesn't tap.

### Card Advantage

- **Rhystic Study:** draws whenever an opponent casts a spell unless they
  pay {1}.
- **Mystic Remora:** draws whenever an opponent casts a noncreature spell
  unless they pay {4}. Cumulative upkeep {1}, so let it go after a few
  turns.
- **Sylvan Library:** see two extra cards each draw step; keep them for 4
  life each.
- **Consecrated Sphinx:** draw two whenever an opponent draws.
- **Narset, Parter of Veils:** opponents can't draw more than one card each
  turn. −2 digs four deep for a noncreature, nonland card (Isochron
  Scepter, Rings of Brighthearth, a tutor or a counterspell).
- **Windfall:** everyone discards and draws as many as the largest hand
  discarded. With Narset out, opponents draw only one.
- **Brainstorm:** draw three, put two back. Puts back cards you'll tutor or
  shuffle away.
- **Ponder:** look at three, reorder or shuffle, draw one.
- **Preordain:** scry 2, draw one.
- **Gitaxian Probe:** see a hand and draw, for {U} or 2 life. Check for
  counterspells before you go off.
- **Frantic Search:** draw two, discard two, untap up to three lands.
  Usually free or better.
- **Dig Through Time:** delve; take the best two of the top seven.
- **Treasure Cruise:** delve; draw three.

### Mana Base

17 lands, because the rocks and creatures do most of the work. Ancient
Tomb adds {C}{C}. Crop Rotation can fetch Ancient Tomb or Boseiju, Who
Endures (channel it to destroy an opposing artifact, enchantment or
nonbasic land).

### Mulligan Guidance

Keep a hand with 2 lands or a mana source and at least one of: a fast-mana
piece, a one-drop mana creature, or a cheap tutor. Do not keep slow hands
with no way to reach turn-two ramp. Always mulligan hands with no plan.

### Turn-by-Turn

- **Turn 0-1:** free mana (Mox Diamond, Chrome Mox, Lotus Petal), then a land
  and a mana creature or Sol Ring. Ancient Tomb is a strong turn-one land.
- **Turn 2:** Kinnan if safe. Otherwise keep ramping and hold a counterspell.
- **Turn 3:** with Kinnan on board, tap everything for an extra mana each and
  tutor for the missing combo piece.
- **Turn 4-5:** go off. Keep a free counterspell up first, and pass the turn
  if the table has not tapped out or shown interaction.
- **If a combo is disrupted:** rebuild with Eternal Witness or a tutor
  and keep playing the grind engine (Remora, Rhystic, Sphinx).
