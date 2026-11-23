#!/usr/bin/env python3
"""
Initialise le tableau Kanban GitHub Projects de la SAE KerLogis (Release 0).

Prérequis : GitHub CLI (`gh`) connecté avec les droits `repo` et `project`
    gh auth login
    gh auth refresh -s project

Usage :
    python3 scripts/kanban_setup.py OWNER/REPO NUMERO_PROJET [--dry-run]

  - OWNER/REPO     : le dépôt de l'équipe, ex. breizhops/kerlogis-sae
  - NUMERO_PROJET  : numéro du GitHub Project (créé au préalable dans l'interface,
                     vue « Board »), visible dans son URL .../projects/<numéro>
  - --dry-run      : affiche les commandes sans rien créer

Le script :
  1. crée les étiquettes (classes de service, domaines, releases, bloqué, aléa) ;
  2. crée une issue par story de backlog_v0.json (story, critères, dépendances) ;
  3. ajoute chaque issue au projet.

À faire à la main ensuite dans GitHub Projects (non automatisable simplement) :
  - renommer les options du champ Status en : À faire, Analyse, En cours, À vérifier, Terminé ;
  - ajouter les champs Date de début / Date de fin (type Date), Release, Taille ;
  - afficher la limite de WIP sur les colonnes (menu de la colonne > Set limit) :
    Analyse 3, En cours 3, À vérifier 2 ;
  - écrire les règles de sortie dans la description de chaque colonne ;
  - donner au PO l'accès en lecture au projet.
"""
import json, os, subprocess, sys

LABELS = [
    ("expedite", "B60205", "Classe : passe devant tout, une seule à la fois"),
    ("date-fixe", "D93F0B", "Classe : démarrer assez tôt pour tenir la date"),
    ("standard", "1D76DB", "Classe : ordre du backlog"),
    ("intangible", "BFBFBF", "Classe : quand il reste de la capacité"),
    ("gestion-projet", "5319E7", "Domaine"),
    ("ebios", "0E8A16", "Domaine"),
    ("infrastructure", "006B75", "Domaine"),
    ("documentation", "C5DEF5", "Domaine"),
    ("etude-pilpro", "FBCA04", "Domaine"),
    ("R0", "EDEDED", "Release"), ("R1", "EDEDED", "Release"), ("R2", "EDEDED", "Release"),
    ("R3", "EDEDED", "Release"), ("R4", "EDEDED", "Release"),
    ("bloqué", "000000", "Indicateur : cause / responsable / prochaine action en commentaire"),
    ("alea", "F9D0C4", "Carte déclenchée par le PO"),
]
CLASS = {"Expedite": "expedite", "Date fixe": "date-fixe", "Standard": "standard", "Intangible": "intangible"}


def run(cmd, dry):
    print("$", " ".join(cmd))
    if dry:
        return ""
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("  ! ", r.stderr.strip())
    return r.stdout.strip()


def body(s):
    crit = "\n".join(f"- [ ] {c.strip()}" for c in s["Critères d'acceptation"].split(" / "))
    return (f"**{s['ID']}** · {s['Activité']} · Release {s['Release']} · {s['Classe']} · "
            f"{s['MoSCoW']} · Taille {s['Taille']} · Rang {s['Rang']}\n\n"
            f"## User story\n{s['User story']}\n\n"
            f"## Critères d'acceptation\n{crit}\n\n"
            f"## Dépend de\n{s['Dépend de'] or '—'}\n\n"
            f"## Suivi\n- Responsable : {s.get('Responsable', '')}\n- Relecteur : {s.get('Relecteur', '')}\n- Date de début : \n- Date de fin : \n\n"
            "## Tâches\n- [ ] \n")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    if len(args) != 2:
        sys.exit(__doc__)
    repo, project = args
    owner = repo.split("/")[0]
    here = os.path.dirname(os.path.abspath(__file__))
    stories = json.load(open(os.path.join(here, "..", "backlog", "backlog_v0.json"), encoding="utf-8"))

    for name, color, desc in LABELS:
        run(["gh", "label", "create", name, "--repo", repo, "--color", color,
             "--description", desc, "--force"], dry)

    for s in sorted(stories, key=lambda x: x["Rang"]):
        labels = [CLASS[s["Classe"]], s["Domaine"]]
        rel = s["Release"] if s["Release"] in ("R0", "R1", "R2", "R3", "R4") else "R0"
        labels.append(rel)
        url = run(["gh", "issue", "create", "--repo", repo,
                   "--title", f"{s['ID']} – {s['Titre']}",
                   "--body", body(s), "--label", ",".join(labels)], dry)
        if url:
            run(["gh", "project", "item-add", project, "--owner", owner, "--url", url], dry)

    print(f"\n{len(stories)} stories traitées. Terminez la configuration du projet à la main (voir l'en-tête du script).")


if __name__ == "__main__":
    main()
