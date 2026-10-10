#!/usr/bin/env python3
"""
detect.py - a five-check panel that scores how machine-written a draft looks.

What this is:  five local heuristics modelled on the signals public AI
detectors actually measure - sentence-length variation, concreteness, stock
vocabulary, typographic fingerprint, and voice. Every score is computed on
your machine from the text alone. Nothing is uploaded.

What this is NOT:  GPTZero, Originality, Copyleaks, Winston or Turnitin.
It does not call their APIs and it cannot promise their verdict. It catches
the things they all key on, which is why fixing them tends to move their
numbers too - but the only honest claim is the one on this line.

Each check returns a HUMAN score from 0 to 100. Higher is better.

Usage
  python3 detect.py draft.txt
  pbpaste | python3 detect.py -
  python3 detect.py draft.txt --json
  python3 detect.py before.txt after.txt      # compare two drafts
"""

import argparse
import json
import os
import re
import statistics
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
LEX = os.path.join(HERE, "slop.json")

SENT_RE = re.compile(r"[^.!?\n]+[.!?]*")
WORD_RE = re.compile(r"[^\W\d_]+(?:'[^\W\d_]+)?")
LEX_IT = os.path.join(HERE, "slop.it.json")

IT_MARKERS = re.compile(r"\b(?:il|lo|gli|della|delle|degli|che|non|per|una|sono|ho|è|perché|anche|questo|questa|più|nel|nella|con|come)\b", re.I)
EN_MARKERS = re.compile(r"\b(?:the|and|of|to|is|you|that|this|with|for|are|was|have|it's|i'm)\b", re.I)

# Italian voice. Italian drops the subject, so first/second person shows up in
# clitics, possessives and verb forms more than in pronouns. Contractions do
# not exist; the closest human signal is colloquial register.
IT_PERSON = re.compile(
    r"\b(?:io|me|mi|mio|mia|miei|mie|noi|ci|nostro|nostra|nostri|nostre|"
    r"tu|te|ti|tuo|tua|tuoi|tue|voi|vi|vostro|vostra|vostri|vostre|"
    r"ho|abbiamo|hai|avete|avevo|avevamo|ero|eravamo|siamo|sei|siete|"
    r"faccio|facciamo|fai|dico|diciamo|penso|pensiamo|credo|so|sappiamo|"
    r"volevo|voglio|devo|dobbiamo|posso|possiamo|lavoro|lavoriamo|scrivo|vedo|"
    r"chiedi|ottieni|guarda|prova|pensaci|"                    # tu didattico
    r"[^\W\d_]{2,}iamo|[^\W\d_]{2,}(?:avamo|evamo|ivamo)|"     # noi: seguiamo, andavamo
    r"[^\W\d_]{2,}(?:avo|evo|ivo))\b",                        # io: parlavo, credevo
    re.IGNORECASE)
# Italian writes small numbers, months and time anchors in words.
IT_CONCRETE = re.compile(
    r"\b(?:due|tre|quattro|cinque|sette|otto|nove|dieci|undici|dodici|quindici|"
    r"venti|trenta|quaranta|cinquanta|cento|mille|mila|milioni|miliardi|metà|"
    r"gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|"
    r"ottobre|novembre|dicembre|lunedì|martedì|mercoledì|giovedì|venerdì|"
    r"sabato|domenica|ieri|stamattina|anni fa|mesi fa|settimane fa)\b",
    re.IGNORECASE)
IT_COLLOQUIAL = re.compile(
    r"\b(?:c'è|c'era|c'erano|l'ho|l'abbiamo|l'hai|po'|beh|boh|mica|insomma|"
    r"tipo|ecco|già|proprio|davvero|ok|eh|magari|tanto|comunque|figurati|"
    r"dai|tra l'altro|a dire il vero|detto questo)(?![\w'])",
    re.IGNORECASE)


def detect_lang(text):
    return "it" if len(IT_MARKERS.findall(text)) > len(EN_MARKERS.findall(text)) else "en"


def load_lexicon(path, lang):
    base = json.load(open(path, encoding="utf-8"))
    if lang != "it":
        return base
    lex = json.load(open(LEX_IT, encoding="utf-8"))
    for key in ("invisible", "typographic"):
        if lex.get(key) == "inherit":
            lex[key] = base[key]
    return lex


def term_pattern(find):
    body = re.escape(find).replace(r"\ ", r"\s+")
    head = r"\b" if find[:1].isalnum() else r"(?<!\w)"
    tail = r"\b" if find[-1:].isalnum() else ""
    return re.compile(head + body + tail, re.IGNORECASE)
CONTRACTIONS = re.compile(r"\b\w+'(?:s|t|re|ve|ll|d|m)\b", re.IGNORECASE)
PRONOUNS = re.compile(r"\b(i|me|my|mine|we|us|our|you|your)\b", re.IGNORECASE)
NUMBERS = re.compile(r"\b\d[\d,.]*%?\b|\$\d|€\s?\d")
PROPER = re.compile(r"(?<![.!?]\s)(?<!^)\b[A-ZÀ-Ý][a-zà-ÿ]{2,}\b", re.MULTILINE)


def clamp(n):
    return max(0.0, min(100.0, n))


def scale(value, human, machine):
    """Map value onto 0-100 where `human` -> 100 and `machine` -> 0."""
    if human == machine:
        return 50.0
    return clamp((value - machine) / (human - machine) * 100)


def sentences(text):
    return [s.strip() for s in SENT_RE.findall(text) if len(s.split()) > 2]


def words(text):
    return WORD_RE.findall(text)


def check_burstiness(text):
    """Humans vary sentence length hard. Models write even."""
    lens = [len(s.split()) for s in sentences(text)]
    if len(lens) < 4:
        return 50.0, "too short to judge"
    mean = statistics.mean(lens)
    cv = statistics.pstdev(lens) / mean if mean else 0
    score = scale(cv, human=0.70, machine=0.22)
    return score, f"variation {cv:.2f} across {len(lens)} sentences (want 0.55+)"


def check_specificity(text, lang="en"):
    """Numbers, names and concrete nouns. Slop is abstract."""
    w = words(text)
    if len(w) < 25:
        return 50.0, "too short to judge"
    per100 = 100 / len(w)
    hits = len(NUMBERS.findall(text)) + len(set(PROPER.findall(text)))
    if lang == "it":
        hits += len(IT_CONCRETE.findall(text))
    density = hits * per100
    score = scale(density, human=6.0, machine=0.5)
    return score, f"{hits} concrete markers, {density:.1f} per 100 words (want 4+)"


def check_slop(text, lex):
    """Stock vocabulary density against the lexicon."""
    w = words(text)
    if not w:
        return 50.0, "empty"
    hits, found = 0, []
    for entry in lex["words"] + lex["phrases"]:
        n = len(term_pattern(entry["find"]).findall(text))
        if n:
            hits += n
            found.append(entry["find"])
    density = hits * 100 / len(w)
    score = scale(density, human=0.0, machine=4.0)
    detail = f"{hits} stock terms, {density:.1f} per 100 words"
    if found:
        detail += " (" + ", ".join(sorted(found)[:4]) + (", ..." if len(found) > 4 else "") + ")"
    return score, detail


def check_fingerprint(text):
    """Characters a phone keyboard does not produce."""
    invisible = sum(1 for c in text if unicodedata.category(c) == "Cf")
    em = text.count("—")
    curly = sum(text.count(c) for c in "‘’“”")
    ellip = text.count("…")
    nbsp = sum(text.count(c) for c in "   ")
    total = invisible * 4 + em * 2 + curly + ellip + nbsp
    per1k = total * 1000 / max(len(text), 1)
    score = scale(per1k, human=0.0, machine=12.0)
    detail = (f"{invisible} invisible, {em} em dash, {curly} curly quote, "
              f"{ellip} ellipsis, {nbsp} hard space")
    return score, detail


def check_voice(text, lex, lang="en"):
    """Contractions, person, and the shapes models default to."""
    w = words(text)
    if len(w) < 25:
        return 50.0, "too short to judge"
    per100 = 100 / len(w)
    if lang == "it":
        return check_voice_it(text, lex, per100)
    contractions = len(CONTRACTIONS.findall(text)) * per100
    person = len(PRONOUNS.findall(text)) * per100
    tells = 0
    names = []
    for s in lex["structures"]:
        try:
            n = len(re.compile(s["regex"], re.MULTILINE).findall(text))
        except re.error:
            continue
        if n:
            tells += n
            names.append(s["id"])
    bullets = [len(b.split()) for b in re.findall(r"(?m)^\s*[-*•]\s+(.+)$", text)]
    uniform = (len(bullets) >= 3 and statistics.pstdev(bullets) < 1.6)
    score = (scale(contractions, human=3.0, machine=0.0) * 0.35
             + scale(person, human=8.0, machine=1.0) * 0.35
             + clamp(100 - tells * 22) * 0.30)
    if uniform:
        score -= 12
        names.append("uniform-bullets")
    detail = (f"{contractions:.1f} contractions, {person:.1f} personal pronouns "
              f"per 100 words, {tells} structural tell(s)")
    if names:
        detail += " [" + ", ".join(names[:4]) + "]"
    return clamp(score), detail


def count_tells(text, lex):
    tells, names = 0, []
    for s in lex["structures"]:
        try:
            n = len(re.compile(s["regex"], re.MULTILINE).findall(text))
        except re.error:
            continue
        if n:
            tells += n
            names.append(s["id"])
    return tells, names


def check_voice_it(text, lex, per100):
    """Italian: verbal person carries most of the weight, register a bit."""
    person = len(IT_PERSON.findall(text)) * per100
    colloquial = len(IT_COLLOQUIAL.findall(text)) * per100
    tells, names = count_tells(text, lex)
    bullets = [len(b.split()) for b in re.findall(r"(?m)^\s*[-*•]\s+(.+)$", text)]
    score = (scale(person, human=6.0, machine=0.8) * 0.50
             + scale(colloquial, human=2.0, machine=0.0) * 0.15
             + clamp(100 - tells * 22) * 0.35)
    if len(bullets) >= 3 and statistics.pstdev(bullets) < 1.6:
        score -= 12
        names.append("elenco-uniforme")
    detail = (f"{person:.1f} marcatori di persona, {colloquial:.1f} di registro "
              f"colloquiale per 100 parole, {tells} strutture sospette")
    if names:
        detail += " [" + ", ".join(names[:4]) + "]"
    return clamp(score), detail


CHECKS = ["BURSTINESS", "SPECIFICITY", "SLOP DENSITY", "FINGERPRINT", "VOICE"]


def run(text, lex, lang="en"):
    results = {}
    results["BURSTINESS"] = check_burstiness(text)
    results["SPECIFICITY"] = check_specificity(text, lang)
    results["SLOP DENSITY"] = check_slop(text, lex)
    results["FINGERPRINT"] = check_fingerprint(text)
    results["VOICE"] = check_voice(text, lex, lang)
    scores = [results[c][0] for c in CHECKS]
    # The weakest check drags the verdict: a detector only needs one signal.
    overall = statistics.mean(scores) * 0.6 + min(scores) * 0.4
    verdict = "PASS" if overall >= 70 and min(scores) >= 55 else (
        "REVIEW" if overall >= 50 else "FLAGGED")
    return results, overall, verdict


def bar(score, width=24):
    filled = round(score / 100 * width)
    return "#" * filled + "." * (width - filled)


def render(results, overall, verdict, label=None, out=sys.stdout):
    title = "AI DETECTION PANEL" + (f"  -  {label}" if label else "")
    print("\n" + title, file=out)
    print("=" * max(len(title), 62), file=out)
    for name in CHECKS:
        score, detail = results[name]
        print(f"  {name:<13} {bar(score)} {score:5.1f}", file=out)
        print(f"  {'':<13} {detail}", file=out)
    print("-" * 62, file=out)
    print(f"  {'HUMAN SCORE':<13} {bar(overall)} {overall:5.1f}   {verdict}", file=out)
    if verdict != "PASS":
        weakest = min(CHECKS, key=lambda c: results[c][0])
        print(f"\n  Weakest signal: {weakest}. Fix that first.", file=out)
    print("", file=out)


def main():
    ap = argparse.ArgumentParser(description="Score how machine-written a draft looks.")
    ap.add_argument("input", nargs="?", default="-", help="file, or - for stdin")
    ap.add_argument("compare", nargs="?", help="second file, to show before/after")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--lexicon", default=LEX)
    ap.add_argument("--lang", default="auto", choices=["auto", "en", "it"],
                    help="language profile (default: detect from the text)")
    args = ap.parse_args()

    read = lambda p: sys.stdin.read() if p == "-" else open(p, encoding="utf-8").read()

    targets = [(args.input, read(args.input))]
    if args.compare:
        targets.append((args.compare, read(args.compare)))
    lang = detect_lang(targets[0][1]) if args.lang == "auto" else args.lang
    lex = load_lexicon(args.lexicon, lang)

    payload = []
    for name, text in targets:
        results, overall, verdict = run(text, lex, lang)
        payload.append({
            "source": name,
            "checks": {k: {"score": round(v[0], 1), "detail": v[1]} for k, v in results.items()},
            "human_score": round(overall, 1),
            "verdict": verdict,
        })

    if args.json:
        print(json.dumps(payload if args.compare else payload[0], indent=2, ensure_ascii=False))
        return

    for (name, text), p in zip(targets, payload):
        results, overall, verdict = run(text, lex, lang)
        render(results, overall, verdict, label=os.path.basename(name) if args.compare else None)
    if args.compare:
        a, b = payload
        delta = b["human_score"] - a["human_score"]
        print(f"  {a['human_score']:.1f} {a['verdict']}  ->  "
              f"{b['human_score']:.1f} {b['verdict']}   ({delta:+.1f})\n")

    sys.exit(0 if payload[-1]["verdict"] == "PASS" else 1)


if __name__ == "__main__":
    main()
