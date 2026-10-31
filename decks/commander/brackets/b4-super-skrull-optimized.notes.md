# B4 Super-Skrull Optimized: Notes

## Goals

- Commander: Super-Skrull ({1}{B}{B}{B}, five colors).
- Part of a five-deck set, one per Commander bracket. This is Bracket 4
  (Optimized). The original [super-skrull.txt](../super-skrull.txt) is the
  Bracket 3 version and is unchanged.
- Archetype: five-color ramp and tutors, with Super-Skrull as the mana sink and
  a few fast two-card wins as the plan if the game stalls.
- Pace: Super-Skrull on turn 3, win or lock the game around turns 6-8.

## Constraints

- Bracket 4: no Game Changer limit. 19 Game Changers are in the list.
- No budget (user proxies). The list is about $2,470 at current prices.
- Mana Crypt, Jeweled Lotus and Tinker are banned in Commander, so none of
  them are in the deck.
- Rest of the set: B1 Okaun and Zndrsplt, B2 Cosmic Spider-Man (tuned down),
  B3 Zaxara Hydras, B5 Kinnan (cEDH).

## Change Log

- 2026-10-15: First build from the Bracket 3 deck. 34 lands, 12 mana rocks,
  7 tutors, a faster mana base with original duals and fetch lands.
- 2026-10-21: Rebuilt the primer around role groups with a bullet per card,
  checked against cards/library.json.

## Primer

### Game Plan

Ramp with fast mana, find a black source for the {B}{B}{B}, and cast
Super-Skrull early. Tutors find answers or one of two two-card wins:
Thassa's Oracle with Demonic Consultation or Tainted Pact, or Kiki-Jiki with
a creature that untaps or blinks it. Keep protection up and close the game
with a combo or a big board, using Super-Skrull's abilities as the
fallback.

### Commander

- **Super-Skrull:** a 4/5 flier for {1}{B}{B}{B} with the four abilities
  above. Every other card in the deck either makes the mana to activate
  him, multiplies what his abilities produce, or copies him.

### Two-Card Wins

The fast plan. Tutors find the missing piece; counterspells protect it.

- **Thassa's Oracle:** when it enters, if your devotion to blue is at
  least your library size, you win. With an empty library, devotion 0 is
  enough.
- **Demonic Consultation:** name a card that is not in your library to
  exile your whole library. Cast it with Thassa's Oracle on the stack, or
  before casting Oracle with {U}{U} available.
- **Tainted Pact:** exile cards from the top until you take one or you
  exile two with the same name. Your three basic Swamps are the only
  duplicates: with two or more still in your library, it can stop early,
  so fetch out Swamps first or prefer Demonic Consultation.
- **Laboratory Maniac:** if you would draw from an empty library, you
  win instead. The backup to Thassa's Oracle after Consultation or Pact.
- **Kiki-Jiki, Mirror Breaker:** taps to make a hasty token copy of a
  nonlegendary creature you control. With any of the four partners below,
  this makes infinite hasty tokens.
- **Zealous Conscripts:** a Kiki-Jiki copy enters, gains control of
  Kiki-Jiki and untaps it. Repeat for infinite hasty 3/3s.
- **Pestermite:** a Kiki-Jiki copy untaps Kiki-Jiki. Repeat for infinite
  hasty fliers. Flash also lets it tap a blocker or a land.
- **Deceiver Exarch:** a Kiki-Jiki copy untaps Kiki-Jiki. Repeat for
  infinite hasty 1/4s. Alone, a flash tapper.
- **Felidar Guardian:** a Kiki-Jiki copy blinks Kiki-Jiki, which returns
  untapped with haste. Repeat for infinite hasty 1/4s.

### Tutors

- **Demonic Tutor:** any card to hand for {1}{B}. Usually Thassa's Oracle
  or Demonic Consultation, or the missing Kiki-Jiki piece.
- **Vampiric Tutor:** any card to the top of your library at instant
  speed, for 2 life. Cast it at the end of the turn before you go off.
- **Imperial Seal:** a sorcery-speed Vampiric Tutor.
- **Enlightened Tutor:** an artifact or enchantment to the top of your
  library. Finds Doubling Season, Necropotence, Rhystic Study or a fast-mana
  rock.
- **Worldly Tutor:** a creature to the top of your library. Finds
  Thassa's Oracle, Kiki-Jiki, a Kiki-Jiki partner, or Craterhoof Behemoth.
- **Mystical Tutor:** an instant or sorcery to the top of your library.
  Finds Demonic Consultation, Tainted Pact, a counterspell or Teferi's
  Protection.
- **Idyllic Tutor:** an enchantment to hand. Finds Doubling Season,
  Necropotence, Assault Formation or Smothering Tithe.

### Big Finishers

The fair plan if the combo is stopped. Doublers multiply their tokens.

- **Craterhoof Behemoth:** haste; your creatures get trample and +X/+X,
  where X is your creature count. Ends the game off Walls and tokens.
- **Hornet Queen:** five flying, deathtouch bodies in one card.
- **Elspeth, Sun's Champion:** +1 makes three Soldiers. −3 destroys
  creatures with power 4 or greater, which spares your Walls and tokens.
- **Grave Titan:** a 6/6 deathtouch that makes two 2/2 Zombies on enter
  and attack.
- **Avenger of Zendikar:** a 0/1 Plant per land you control, and +1/+1 on
  every Plant per land drop. Doubling Season and Mondrak double the
  Plants.
- **Walking Ballista:** enters with X counters, {4} adds one, and each
  counter removed deals 1 damage. A mana sink and a finisher.
- **Doubling Season:** doubles tokens and every counter placed on your
  permanents. Planeswalkers enter with double loyalty, so Elspeth, Sun's
  Champion enters with 8 and can use her −7 at once.
- **Mondrak, Glory Dominus:** doubles tokens. Sacrifice two other
  artifacts or creatures (spare tokens) for an indestructible counter.

### Walls

Super-Skrull's 0/4 Walls draw and attack with these.

- **Arcades, the Strategist:** draw a card whenever a creature with
  defender enters. Defenders deal combat damage equal to toughness and
  can attack.
- **Assault Formation:** every creature you control deals combat damage
  equal to its toughness. {G} lets one defender attack, and {2}{G} gives
  your team +0/+1.

### Card Advantage

- **Necropotence:** skip your draw step; pay 1 life per card exiled face
  down to hand at end step. Draw a dozen cards on the combo turn. Needs
  {B}{B}{B}, same as Super-Skrull.
- **Rhystic Study:** draws whenever an opponent casts a spell unless they
  pay {1}.
- **Sylvan Library:** see two extra cards each draw step; keep them for
  4 life each.
- **Phyrexian Arena:** an extra card each upkeep for 1 life.
- **Smothering Tithe:** a Treasure each time an opponent draws unless they
  pay {2}.
- **Sheoldred, the Apocalypse:** gain 2 life per card you draw; opponents
  lose 2 per card they draw. Aim the draw-four ability at an opponent.
- **Skullclamp:** equip a 1/1 token and it dies, drawing two. Walls
  survive it (they become 1/3).
- **Mulldrifter:** draw two, either as a 2/2 flier or evoked for {2}{U}.
- **Eternal Witness:** return any card from your graveyard to hand.

### Fast Mana and Ramp

Super-Skrull needs {B}{B}{B}; these cast him on turn 2 or 3 and pay for his abilities.

- **Sol Ring:** {C}{C} from turn one.
- **Mana Vault:** {C}{C}{C} for {1}. Doesn't untap normally (pay {4} at
  upkeep to untap) and deals 1 damage at draw step while tapped. A turn-two
  Super-Skrull with any black source.
- **Grim Monolith:** {C}{C}{C} for {2}; {4} untaps it. Turn-two
  four-drops.
- **Chrome Mox:** free; imprint a nonartifact, nonland card from hand
  and it taps for that card's colors. Imprint a black card for Super-Skrull.
- **Mox Diamond:** free if you discard a land; taps for any color.
- **Lotus Petal:** free, sacrifice for one mana of any color. Burst mana
  for a turn-two commander or a combo turn.
- **Arcane Signet:** any color in your identity.
- **Fellwar Stone:** a color an opponent's land could make.
- **Talisman of Hierarchy:** {W} or {B}.
- **Talisman of Resilience:** {B} or {G}.
- **Chromatic Lantern:** your lands tap for any color.
- **Coalition Relic:** any color, or store a charge counter for a burst
  of two the next turn (more with Doubling Season).
- **Birds of Paradise:** turn-one flying mana dork of any color.
- **Farseek:** a Plains, Island, Swamp or Mountain card onto the
  battlefield tapped. Finds any original dual or shock.
- **Nature's Lore:** a Forest card onto the battlefield untapped. Bayou,
  Tropical Island, Savannah, Taiga, Overgrown Tomb and Indatha Triome are
  all Forests.
- **Cultivate:** one basic onto the battlefield tapped, one to hand.
- **Kodama's Reach:** a second copy of Cultivate.

### Interaction

Counterspells protect your combo; removal stops theirs.

- **Force of Will:** counter any spell, free for a blue card and 1 life.
  Protects the combo turn.
- **Fierce Guardianship:** counter a noncreature spell, free while you
  control your commander.
- **Mana Drain:** counter any spell and gain that much {C} next main
  phase for a Super-Skrull activation.
- **Teferi's Protection:** phase out everything you control and gain
  protection from everything until your next turn.
- **Cyclonic Rift:** bounce a nonland permanent, or overload for {6}{U}
  to bounce everything opponents control.
- **Swords to Plowshares:** exile a creature for {W}.
- **Path to Exile:** exile a creature for {W}; its controller gets a
  basic land.
- **Assassin's Trophy:** destroy any permanent an opponent controls.
- **Vindicate:** destroy any permanent at sorcery speed.
- **Anguished Unmaking:** exile a nonland permanent for 3 life.
- **Chaos Warp:** shuffle any permanent into its owner's library.
- **Toxic Deluge:** all creatures get -X/-X for X life. Pick X to kill
  their creatures while your 0/4 Walls survive.
- **Damnation:** destroy all creatures. Use it when behind.

### Mana Base

34 lands, 3 basic Swamps. Twelve fetch lands find the ten original duals
and four shocks; all but Plateau, Savannah, Taiga, Tropical Island,
Volcanic Island and Tundra are Swamps. Urborg, Tomb of Yawgmoth makes every
land a Swamp. Ancient Tomb adds {C}{C} for 2 damage.

### Mulligan Guidance

Keep hands with two or more lands (one black source), a rock or tutor, and
a way to cast Super-Skrull on turn 3 or 4. Mulligan hands with only
expensive spells or no black source.

### Turn-by-Turn

- **Turn 1:** a land and Mox, Sol Ring or Birds.
- **Turn 2:** a rock or ramp spell, or a tutor.
- **Turn 3-4:** Super-Skrull with protection up, or a tutor for the right piece.
- **Turn 5+:** use Super-Skrull's abilities each turn, and assemble the combo
  when you have counter backup.
- **Behind on board:** Toxic Deluge or Damnation, then rebuild with
  Eternal Witness and card draw.
