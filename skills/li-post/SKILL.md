---
name: li-post
description: >-
  Scrive un post LinkedIn di Alfonso Pace da un'idea grezza, nella sua voce e
  nei formati del suo sistema editoriale (micro, insight, spinta articolo,
  ricondivisione), sotto il cappello giusto (BYI sul profilo alfpace, pagina
  Warp 7, riflessione personale), ripulito dai segnali AI. Usala quando Alfonso
  chiede un post LinkedIn, un micro, un'apertura, "scrivi un post su X",
  "trasforma questo in un post", o opzioni di hook. Produce tre aperture, una
  bozza completa e un blocco pronto da incollare; non pubblica mai.
---

# li-post

Trasforma un'idea in un post che Alfonso possa pubblicare dopo la sua passata
finale. Il testo pubblicato resta suo: questa skill prepara, non decide.

## Prima di scrivere

1. **Voce.** In quest'ordine, fermandoti alla prima fonte disponibile:
   - Notion collegato: leggi la pagina `how-i-write`
     (3c7d9d25f089804d92a8e70e30faad76) e le **Regole editoriali** attive
     (`collection://2a568ed7-e842-47f4-a84b-10331cb47239`, Stato = attiva).
     Le regole sono vive e prevalgono su tutto il resto.
   - altrimenti `voice.md` in questa cartella;
   - altrimenti `~/.claude/linkedin/voice.md`.
   Se lavori senza Notion, dillo in una riga: le regole potrebbero essere cambiate.
2. **Cappello e formato.** Se non sono chiari dalla richiesta, chiedili
   insieme, in una domanda sola. Non dare Warp 7 per scontato.

   | cappello | dove esce | voce | formati |
   | --- | --- | --- | --- |
   | BYI | profilo `alfpace`, canale BYI | io | micro, insight, insight dimostrativo, longform, teaser |
   | Warp 7 | pagina aziendale | noi editoriale, mai il nome di Alfonso | spinta articolo, ricondivisione |
   | Alfonso | profilo `alfpace`, fuori dagli archi | io, lente filosofica | riflessione |

3. **Calendario.** Con Notion collegato, leggi **Contenuti**
   (`collection://6c630542-6113-4d79-b967-58a77228cef3`) sui 10 giorni
   prossimi e sui 15 passati. Ti serve per tre cose: lo slot in cui cade il
   pezzo, l'arco del mese, e gli angoli già usati da non ripetere. Se il micro
   del lunedì e l'insight del mercoledì insistono sulla stessa materia, il micro
   prende l'ostacolo e l'insight il metodo, e l'insight dà per acquisito ciò che
   il micro ha già nominato.
4. **Materiale.** Un post ha bisogno di una cosa vera e specifica. Se l'idea è
   sottile ("un post sull'AI"), non riempire: chiedi in una sola domanda cosa è
   successo, a chi, quando, e cosa è costato o ha reso. Per il micro serve che
   Alfonso sia **dentro la scena**: un fatto letto e non vissuto va all'insight.
   Se manca un'idea, la fonte preferita è un aggancio reale e datato dalla
   mailbox, oppure la skill `content-mine`.
5. **Aperture.** Leggi `hooks.it.json` in questa cartella. Contiene le aperture
   compatibili con la voce e quelle escluse, con il motivo. `hooks.json` è
   l'originale inglese: non usarlo per i post di Alfonso.

## La forma

```
Riga 1   l'apertura. Da sola. Deve reggere il troncamento a ~140 caratteri.
Riga 2   il seguito della riga 1, non una premessa.
Corpo    paragrafi brevi, 1-3 righe. Ogni 3-5 una frase-paragrafo di rottura.
Svolta   una riga che rilegge quello che è venuto prima.
Chiusura secondo il formato (sotto). Una domanda o un invito, mai entrambi.
```

| formato | lunghezza indicativa | chiusura |
| --- | --- | --- |
| micro | 500-1.000 caratteri | due frasi brevi in anafora poi contrasto netto, o understatement, o il concetto nominato a posteriori. Non risolve tutto. Mai enfasi. |
| insight / post di accompagnamento | 900-1.500 | aforisma che chiude il cerchio, o riconnessione al principio. Nessuna promozione dei servizi. |
| spinta articolo (Warp 7) | 700-1.200 | rimando al pezzo, link nel primo commento. |
| ricondivisione (Warp 7) | 600-1.000 | cosa facciamo, detto con misura, e invito a parlarne. Niente promesse, niente numeri non dimostrabili, niente clienti in corso. |
| riflessione (Alfonso) | 700-1.300 | aforisma; la lente filosofica arriva dopo il fatto, mai in apertura. |

Il longform non si scrive qui: ha epigrafe e struttura propria.

## Il ciclo

**1. Tre aperture, non una.** Scegli da `hooks.it.json` tre aperture diverse
che si adattano davvero al materiale. Mostrale come tre righe numerate e di' in
una frase quale useresti e perché.

**2. Bozza completa** sull'apertura più forte.

**3. Igiene.** Passa la bozza da `li-human` prima di mostrarla:

```bash
python3 <cartella li-human>/humanize.py bozza.txt -o pulita.txt --report
python3 <cartella li-human>/detect.py bozza.txt pulita.txt
```

Riscrivi a mano ogni termine in *TERMINI DA RISCRIVERE A MANO* e ogni
struttura segnalata. Poi controlla le regole di igiene AI di Alfonso, che lo
script non vede tutte: niente em dash, al massimo due grassetti, al massimo un
elenco verticale a frase singola, al massimo una costruzione per negazione,
una sola insinuazione retorica e dopo la spiegazione, niente tricolonne
perfette, PERFECTUM mai nominato, chi si critica resta anonimo.

Come leggere il verdetto: **FLAGGED** significa riscrivere. **REVIEW** vuol
dire guardare il segnale più debole e decidere: i micro di Alfonso, con frasi
di lunghezza simile, stanno spesso lì e vanno bene così. **PASS** non è una
garanzia, è l'assenza dei segnali misurati.

**4. Il blocco.** Pronto da incollare, in un blocco di codice, esattamente come
va su LinkedIn. Sotto:

```
POST PRONTO
cappello:   BYI · micro · lunedì 12 ottobre
apertura:   fatto vissuto e databile
lunghezza:  740 caratteri
igiene:     3 artefatti tolti, 2 termini riscritti, 71 PASS
da verificare: {{dato mancante}} alla riga 6

Scrivi "sì" per salvarlo in Contenuti come "pronto", o dimmi cosa cambiare.
```

**5. Non pubblicare mai.** Su "sì", con Notion collegato, salva in
**Contenuti**. Se esiste già la riga per quello slot (stessa Data, Canale e
Formato), **aggiornala**: Stato `pronto`, Angolo se è cambiato, e la nuova
bozza nel corpo pagina sotto un titolo datato ("## Bozza (giorno mese)"),
senza cancellare le bozze precedenti né le Note editoriali. Solo se la riga
non esiste, creala: Titolo nella forma "Micro — {tema}", Canale, Formato,
Data dello slot, Stato `pronto`, Angolo in una riga, Arco se c'è, e la bozza
nel corpo pagina. Ricorda che il corpo pagina ospiterà il **testo pubblicato** e
che Alfonso spesso cambia il finale in pubblicazione: non è una discrepanza.
Senza Notion, aggiungi data, cappello, formato e prima riga a
`~/.claude/linkedin/log.md`.

## Regole che fanno la differenza

- **Un'idea per post.** Se la bozza ne ha due, sono due post: dillo.
- **Mai inventare.** Niente metriche, clienti, cifre o esempi plausibili sotto
  il nome di Alfonso. Se un dato serve e manca, lascia `{{dato mancante}}` nel
  testo e segnalalo. Se un esempio è ipotetico, il testo lo dichiara.
- **Niente esca per commenti.** "Cosa ne pensate?" è morto. La domanda finale,
  se c'è, è una che solo questo post può fare.
- **Hashtag:** di default nessuno. Al massimo tre, in fondo, se Alfonso li chiede.
- **Link:** mai nel corpo. Nel primo commento, e il blocco lo dice.
- **Emoji:** nessuna, tranne 👇 accanto a "link nel primo commento".
- **Formati nuovi** solo con conferma esplicita di Alfonso.
- **Warp 7:** "Boost Your Insights" indica solo la newsletter; per i servizi
  "nei nostri progetti".

## Esempio

```
/li-post il fornitore nuovo mi ha chiamato cinque volte in due mesi per chiedere come va
```

```
APERTURE
1. fatto vissuto     Da luglio lavoro con un nuovo fornitore.
2. affermazione      La telefonata più utile di un fornitore è quella in cui non vende niente.
3. buoni / ottimi    Alcuni fornitori aspettano il reclamo. Altri lo vanno a cercare.

Uso la 1: il fatto è tuo e datato, e lascia alla chiusura il lavoro di nominare il concetto.
```
