---
name: li-audit
description: >-
  Analisi a posteriori dei post LinkedIn già pubblicati da Alfonso Pace
  (profilo alfpace e pagina Warp 7): quali hanno funzionato, perché, cosa
  smettere di fare. Legge le metriche dal database Contenuti su Notion o da un
  export LinkedIn. Usala quando Alfonso chiede "cosa funziona", "perché questo
  è andato male", "leggi le metriche", "audit dei contenuti", o vuole sapere su
  cosa raddoppiare.
---

# li-audit

L'unica fonte onesta su cosa funziona per un account è quell'account. Ogni
regola di ogni guida LinkedIn, comprese quelle di questo pacchetto, è
un'ipotesi. Gli ultimi post di Alfonso sono l'evidenza.

## Input

Con Notion collegato, la fonte è **Contenuti**
(`collection://6c630542-6113-4d79-b967-58a77228cef3`), righe con Stato
`pubblicato`. Ci sono già: Canale, Formato, Data, Impression, Interazioni,
Utenti raggiunti, Fuori rete, Distribuzione, Angolo, Arco, Note editoriali, e
il testo pubblicato nel corpo pagina.

Altrimenti chiedi l'export di LinkedIn (Analytics → Contenuti → Esporta) o gli
screenshot con impression, reazioni, commenti, condivisioni.

## Regola prima di tutto: parità di distribuzione

Le metriche di due post si confrontano **solo se distribuiti nelle stesse
condizioni**. Il campo Distribuzione registra le eccezioni: vuoto o `organica`
è confrontabile; `pod`, `ripresa da altri`, `mista` si escludono dai confronti
di formato e di angolo. Un post spinto insegna qualcosa sulla distribuzione,
non sulla qualità del contenuto. Dichiara quante righe hai escluso e perché.

Confronta anche **canale con canale**: il profilo `alfpace` e la pagina Warp 7
hanno pubblici di dimensione diversa, quindi metterli nella stessa classifica
non ha senso.

## Cosa misurare

Le impression grezze sono il numero meno utile: dipendono soprattutto da quanti
già ti seguono. Calcola, mostrando il conto:

| metrica | come | cosa dice |
| --- | --- | --- |
| **Engagement rate** | interazioni / impression | se il post si è guadagnato la sua portata. È il segnale scelto da Alfonso per le valutazioni. |
| **Fuori rete** | campo omonimo, quando c'è | se il post ha viaggiato oltre i collegamenti diretti |
| **Portata relativa** | utenti raggiunti / follower del canale | se è uscito dal pubblico abituale (chiedi i follower se non li hai) |

Attenzione alle finestre: se le metriche vengono da un export che include il
giorno di pubblicazione, dillo, perché il primo giorno pesa molto.

## Trovare lo schema

Con i migliori e i peggiori affiancati, cerca cosa li separa davvero, e sii
disposto a una conclusione che ad Alfonso potrebbe non piacere:

- Formato (micro, insight, spinta articolo, ricondivisione).
- Apertura: quale voce di `li-post/hooks.it.json`, ricavata dalla prima riga.
- Tipo di materiale: vissuto in prima persona, scena attribuita, fatto letto.
- Arco e tema.
- Lunghezza.
- Giorno e ora, **per ultimi**, e solo se il resto non mostra niente.

Esprimi ogni conclusione come affermazione con l'evidenza accanto e di' quanto
sei sicuro. Con 30 post si vede uno schema; con 6 no, e va detto invece di
inventarne uno.

## Output

```
AUDIT · BYI (alfpace) · 24 post organici · 12 lug - 9 ott   (esclusi: 2, pod)

MIGLIORI PER ENGAGEMENT RATE
  2,5%  micro  scena           "Aula di piccoli imprenditori. Tanti anni fa."   1.677 imp · 66% fuori rete
  ...

PEGGIORI
  ...

COSA DICONO I DATI
1. {affermazione} · {evidenza, n=} · {quanto è solida}
2. ...

SMETTERE: ...
FARE DI PIÙ: ...
REGOLA CANDIDATA: {se emerge, formulata come le Regole editoriali, con il post che fa da precedente}
```

Una regola candidata non entra in **Regole editoriali** da sola: proponila ad
Alfonso e, se la conferma, crea la riga con il precedente collegato. Poi passa
le conclusioni a `/li-plan`, così il piano della settimana dopo poggia sulle
sue evidenze e non sui default.
