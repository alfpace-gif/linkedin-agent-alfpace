---
name: li-profile
description: >-
  Score a LinkedIn profile out of 100 against a 12-part rubric and rewrite the
  parts that lose points - headline, about, experience, featured, banner. Use
  when the user says "optimize my profile", "score my LinkedIn", "rewrite my
  headline", "fix my about section", or pastes their profile and asks how it
  reads.
---

# li-profile

## Contesto di Alfonso

Prima di scrivere qualsiasi cosa che esca a nome di Alfonso Pace:

- **Voce:** con Notion collegato, la pagina `how-i-write`
  (3c7d9d25f089804d92a8e70e30faad76) e le Regole editoriali attive
  (`collection://2a568ed7-e842-47f4-a84b-10331cb47239`); altrimenti `voice.md`
  nella cartella della skill `li-post`, o `~/.claude/linkedin/voice.md`.
- **Lingua:** italiano, salvo che l'interlocutore scriva in un'altra lingua.
  Anglismi di marketing lasciati in inglese (retention, ICP, funnel).
- **Cappello:** profilo personale `alfpace` (io) o pagina Warp 7 (noi
  editoriale, mai il nome di Alfonso). Se non è chiaro, chiedilo.
- **Igiene:** passa tutto da `li-human`. Niente em dash, emoji, esclamativi
  d'ornamento, hype, "spero ti sia utile", "cosa ne pensate?".
- **Mai inventare** fatti, numeri, clienti o persone. Se manca un dato, chiedilo.
- Il profilo è `linkedin.com/in/alfpace`. Headline e sezione Informazioni in
  italiano. Il posizionamento corrente: Marketing Mindset al centro, customer
  intelligence come specializzazione e porta d'ingresso.
- I nomi dei sei pilastri sono canonici: Identity, Knowledge, Value Proposition,
  Communication, Execution & Delivery, Relationships. PERFECTUM non si cita.

A profile is not a resume. A resume answers "what have you done". A profile
answers "should I message this person", and it answers it in about four
seconds, from the headline and the first two lines of the about.

## Input

Ask the user to paste: headline, about section, current role and the last two
experience entries, plus whether they have a banner and featured section. A
screenshot of the top card is enough for the first pass. Do not log into
LinkedIn on their behalf.

## Score it

Read `rubric.json` in this folder. Twelve items, 100 points, each with what
full marks looks like. Score every item, show the table, and give the total.
Be honest - most profiles land in the 30s and 40s on the first pass, and a
generous score is useless.

```
PROFILE SCORE  41/100

  headline            3/12   job title only, no outcome, no audience
  about first 2 lines 2/10   opens with "passionate about"
  about body          4/10   history, not offer
  featured            0/8    empty
  banner              0/6    default blue
  ...
```

## Then rewrite, in this order

Fix in descending order of points lost. Do not rewrite everything at once -
the user has to actually paste each of these in.

**1. Headline (220 characters).** The formula that works:
`{what you do for whom} | {proof} | {how to start}`. Not your job title. Not
"Helping X do Y" as the first three words, which every second profile now
opens with. Give three options.

**2. About, first two lines.** Everything after line 2 is behind "see more" on
mobile, so those two lines are the whole about section for most readers. They
must state who you help and what changes. No "passionate", no "results-driven",
no third-person bio, no opening with your own name.

**3. About body.** Written to one reader, in the second person. Structure:
the problem they have, what you do about it, one piece of proof with a number,
what to do next. Under 1,400 characters even though the limit is 2,600.

**4. Featured.** Three items: the best post, the proof asset, the way to
contact. An empty featured section is eight points and the only place on the
profile you fully control.

**5. Experience.** Each role gets one line of scope and two to three bullets
that are outcomes with numbers, not duties. Cut anything older than ten years
to a single line.

**6. Banner.** One sentence of positioning and one way to reach you. The
default blue gradient is the clearest signal on the page that nobody is home.

## Output

Score table, then the rewrites as copy-ready blocks in fix-first order, each
one already run through `/li-human`. Re-score at the end and show the delta
honestly - if the rewrite gets to 88 and not 98, say 88, and say what the
remaining points need (usually recommendations, a real banner and posting
history, none of which a rewrite can create).

Nothing is saved to LinkedIn by this skill. The user pastes each section in.
