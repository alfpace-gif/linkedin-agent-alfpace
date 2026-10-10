# linkedin-agent-alfpace

Adattamento personale di [linkedin-agent-skill](https://github.com/avi691/linkedin-agent-skill)
di Avi Grondin (licenza MIT, inclusa) all'italiano e al sistema editoriale di
Alfonso Pace. Uso privato: `voice.md` contiene riferimenti al workspace Notion,
non pubblicare questo repository.

## Cosa cambia rispetto all'originale

- **li-human:** lessico italiano (`slop.it.json`) con voci "solo segnalazione"
  per i termini che vanno riscritti a mano; rilevamento automatico della lingua
  (`--lang it|en|auto`); controllo VOICE italiano basato su persona verbale e
  registro; numeri in lettere, mesi e lettere accentate riconosciuti. Inglese
  invariato.
- **li-post:** formati del sistema editoriale (micro, insight, spinta articolo,
  ricondivisione, riflessione), tre cappelli, aperture in `hooks.it.json`
  filtrate su how-i-write (dieci formule originali escluse, con il motivo),
  salvataggio in Notion Contenuti come `pronto` invece di `log.md`.
- **li-plan, li-audit:** leggono Contenuti, Archi mensili, Regole editoriali e
  Archivio articoli Warp 7 su Notion; l'audit confronta solo a parità di
  distribuzione e per canale.
- **Altre sette skill:** blocco di contesto comune (voce, lingua, cappello,
  igiene) e note specifiche (ICP, design system Warp 7 per i caroselli,
  conferma per formati nuovi).
- Corretto un problema dell'originale: `$` seguito da una cifra nei SKILL.md
  veniva sostituito dagli argomenti del comando.

## Voce

Le fonti autoritative sono su Notion (how-i-write e Regole editoriali).
`skills/li-post/voice.md` è lo snapshot di riserva, usato quando Notion non è
collegato. In Claude Code si può copiare anche in `~/.claude/linkedin/voice.md`.

## Installazione in Claude Code

Da una cartella locale:

    /plugin marketplace add /percorso/linkedin-agent-alfpace
    /plugin install linkedin-agent-alfpace

Oppure da un repository GitHub privato con la stessa struttura.
