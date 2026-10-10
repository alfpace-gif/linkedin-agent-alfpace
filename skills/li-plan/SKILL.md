---
name: li-plan
description: >-
  Pianifica la settimana LinkedIn di Alfonso Pace sul suo sistema editoriale:
  slot fissi (micro BYI, spinta articolo Warp 7, insight, ricondivisione),
  arco del mese, angoli concreti da materiale vissuto, e lista di persone con
  cui interagire. Usala quando Alfonso dice "pianifica la settimana", "cosa
  pubblico", "calendario", "non ho niente da scrivere", o vuole il piano dei
  prossimi giorni.
---

# li-plan

La sala di controllo. Le altre skill eseguono, questa decide cosa eseguire.
Si lancia una volta a settimana, idealmente il venerdì per la settimana dopo.

## Fonti

Con Notion collegato, leggi in quest'ordine:

1. **Contenuti** (`collection://6c630542-6113-4d79-b967-58a77228cef3`):
   righe dei prossimi 10 giorni, cioè cosa è già in programma e in che stato,
   e degli ultimi 30 per non ripetere angoli.
2. **Archi mensili** (`collection://2a429f04-bcac-4ead-b549-84bbcc30de32`):
   il tema del mese e a che punto è.
3. **Regole editoriali** attive (`collection://2a568ed7-e842-47f4-a84b-10331cb47239`).
4. **Archivio articoli Warp 7** (`collection://5017a34a-a702-4702-8167-cc067aae08a8`):
   per la spinta del martedì controlla il campo *Già spinto su LinkedIn*, non la
   data di pubblicazione sul sito. Sono due cose diverse e solo la prima conta.

Senza Notion, usa `voice.md` nella cartella di `li-post` e chiedi ad Alfonso
cosa è già in programma.

## La settimana tipo

| giorno | canale | formato | nota |
| --- | --- | --- | --- |
| lunedì | BYI (alfpace) | micro | prende l'ostacolo, l'attrito |
| martedì | Warp 7 (pagina) | spinta articolo | dall'Archivio articoli, link nel primo commento |
| mercoledì | BYI (alfpace) | insight | prende il metodo; dà per acquisito ciò che il micro ha nominato |
| giovedì | Warp 7 (pagina) | ricondivisione | rilancia l'insight con taglio commerciale misurato |

Questa è la griglia che emerge dalle regole attive. Se Contenuti mostra uno
schema diverso per la settimana in esame, vale Contenuti: segnala la differenza
e non correggerla da solo. Formati nuovi solo con conferma esplicita.

Riflessioni personali (cappello Alfonso) fuori griglia, quando c'è materiale.
Non riempire uno slot per riempirlo: uno slot vuoto è meglio di un post debole,
e va segnato `saltato`.

## Gli angoli

Per ogni slot da produrre: il tema, l'**angolo concreto**, la fonte del
materiale e l'apertura da `li-post/hooks.it.json`. Non un argomento: un angolo.
"Retention" non è un piano. "Il fornitore che mi ha chiamato cinque volte in
due mesi" è un post.

Dove si trova il materiale, in ordine:

1. Quello che è successo davvero ad Alfonso questa settimana: chiamate, progetti,
   acquisti, scambi. Chiedilo in una domanda sola se non lo sai.
2. Un aggancio reale e datato dalla mailbox (se Gmail è collegato:
   `category:updates newer_than:2d -from:me`).
3. La skill `content-mine`, un'intervista una domanda alla volta.

Per il micro il materiale deve essere **vissuto**, non solo letto. Un fatto
letto va all'insight.

## Con chi interagire

Una lista di 10, in tre gruppi:

- **5 portata:** persone con il pubblico che interessa ad Alfonso (imprenditori
  e CEO di aziende da 10-20 milioni in su, responsabili marketing e
  commerciali), sui cui post può aggiungere qualcosa di vero. Commentare prima
  che abbiano 20 commenti.
- **3 pari:** consulenti e professionisti allo stesso livello.
- **2 potenziali clienti:** si commenta per settimane prima di qualsiasi DM, e
  mai una proposta in un commento.

Venti minuti al giorno, prima di pubblicare. Se non hai nomi, chiedili:
non inventare persone.

## Orari

Il pubblico è B2B italiano. Martedì-giovedì 7:30-9:30 è il default di
lavoro, lunedì mattina va bene per il micro. Ma l'orario conta molto meno della
prima riga: se Alfonso ottimizza l'orario prima dell'apertura, sta lucidando la
cosa sbagliata. E le metriche si confrontano solo a parità di distribuzione.

## Output

```
SETTIMANA DEL 12 OTTOBRE · arco: {tema del mese}

LUN  BYI    micro            fatto vissuto   - il fornitore che chiama per chiedere come va   [da produrre]
MAR  Warp 7 spinta articolo  domanda-setup   - "Buyer persona" (mai spinto)                   [da produrre]
MER  BYI    insight          affermazione    - il metodo dietro il micro di lunedì            [in bozza]
GIO  Warp 7 ricondivisione   -               - rilancio dell'insight 11                       [da produrre]

INTERAZIONI (5 portata / 3 pari / 2 clienti)
  ...

DA CHIARIRE: {cosa manca per chiudere il piano}

Scrivi "scrivi lunedì" e preparo la bozza con /li-post.
```

Con Notion collegato e il via di Alfonso, crea le righe mancanti in Contenuti
con Stato `da produrre`, Data, Canale, Formato, Arco e l'angolo nel campo
Angolo. Non toccare le righe esistenti senza chiederlo. Senza Notion, scrivi il
piano in `~/.claude/linkedin/plan.md`. Niente viene programmato o pubblicato:
il piano lo esegue Alfonso.
