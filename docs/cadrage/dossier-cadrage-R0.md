# Dossier de cadrage – Release 0

Équipe BreizhOps Conseil · parcours PilPro · version du 23/11/2026

Ce dossier constitue la Release 0 (S1–S2) : il traduit la demande de KerLogis en backlog priorisé, fixe le MVP et configure le flux Kanban. Les hypothèses sont à faire valider par le PO.

## 0. L'équipe prestataire

**Nom d'équipe :** BreizhOps Conseil (maîtrise d'œuvre). Client : KerLogis, représenté par le PO (maîtrise d'ouvrage). Parcours : PilPro (référent enseignant : M. Duron).

### Responsabilités Kanban

| Responsabilité | R0 | R1 | R2 | R3 | R4 | Missions |
| --- | --- | --- | --- | --- | --- | --- |
| Coordinateur du flux | Yolan | Benjamin | Elouan | Melvin | Yolan | Tableau à jour, respect du WIP, animation des points avec le PO, mails client, indicateurs, release note (US-05) |
| Référent EBIOS | Melvin | Melvin | Melvin | Melvin | Melvin | Ateliers 1 à 5, cohérence risques ↔ mesures ↔ backlog |
| Référent technique | Elouan | Elouan | Yolan | Elouan | Elouan | Plateforme Proxmox, demandes de ressources, procédures |
| Référent documentation | Benjamin | Yolan | Benjamin | Benjamin | Benjamin | Journal de bord, versionnage du backlog, dossier final |
| Référent étude financière (PilPro) | – | – | Benjamin | Yolan | Yolan | Données de coûts, scénarios, recommandation |

**Logique de la répartition :** les référents EBIOS (Melvin) et technique (Elouan) restent stables pour garder la continuité d'expertise ; la coordination tourne à chaque release pour que chacun soit face au PO au moins une fois. À chaque release, chaque membre tient au moins un rôle. Yolan reprend la technique en R2 pendant qu'Elouan coordonne, et l'étude financière passe de Benjamin (collecte des données) à Yolan (chiffrage et recommandation).

### Répartition des stories (responsable)

Chaque story a un responsable et un relecteur différent (Definition of Done) ; le détail est dans [`backlog/backlog_v0.csv`](../../backlog/backlog_v0.csv). Les stories marquées * sont « si capacité ».

| Release | Yolan | Melvin | Elouan | Benjamin |
| --- | --- | --- | --- | --- |
| R0 | **Coordination** · US-02 Story map et backlog | US-01 Analyse de la demande | US-03 Tableau Kanban GitHub | US-04 Plan de release |
| R1 | US-40 Comptes admin + MFA · US-30 Sauvegarde PBS · US-70 Dossier de preuves | US-10 Atelier 1 · US-11 Atelier 2 | US-20 Lab Proxmox · US-21 Migration du WMS | **Coordination** · US-31 Test de restauration |
| R2 | US-41 Segmentation + OPNsense · US-43 Droits des partages | US-12 Atelier 3 · US-13 Atelier 4 · US-45 MFA messagerie | **Coordination** · US-42 Réseau scanners · US-33 Autres sauvegardes | US-24 Portail en DMZ · US-72 Données de coûts |
| R3 | US-32 Copie externalisée · US-73 Scénario sur site | **Coordination** · US-14 Atelier 5 · US-60 Simulation d'incident · US-51 Journalisation | US-22 Haute disponibilité · US-50 Supervision · US-44 Coffre de secrets* | US-74 Scénario cloud · US-61 PCA/PRA · US-71 Questionnaire fournisseur* |
| R4 | **Coordination** · US-75 Rennes et pics · US-77 Recommandation | US-76 Impacts et risques des scénarios · US-62 Fiche rançongiciel* | US-23 Gabarit de site Rennes · US-52 Cas de détection* | US-78 Dossier technique · US-79 Restitution |

**Règles d'équipe :**

- Une personne a au plus une carte en En cours ; quand sa carte est en À vérifier, elle relit celle d'un autre avant d'en démarrer une nouvelle.
- Le test de restauration (US-31) est fait par Benjamin et non par Elouan, qui a construit la plateforme : c'est la preuve que la procédure fonctionne sans son auteur.
- Les relectures sont équilibrées : 10 par personne sur l'ensemble du projet.
- Le coordinateur garde moins de stories dans sa release : la coordination, les mails et les indicateurs comptent comme une charge.
- Toute réaffectation en cours de release est notée dans le journal de bord et sur la carte.

### Charte de communication

- **Canal client unique :** un mail par décision, envoyé par le coordinateur du flux, équipe en copie, objet préfixé `[KerLogis][Rx]`.
- **Délai de réponse :** toute question du PO reçoit une réponse sous 24 h ouvrées, même partielle.
- **Blocage :** signalé au PO dès qu'il est identifié, sans attendre le point quotidien, avec cause, impact et prochaine action.
- **Changement de plan :** annonce écrite au PO avec l'impact (stories décalées, nouvelle date), puis trace dans le journal de bord.
- **Comptes rendus :** chaque échange avec le PO donne un compte rendu de 5 lignes maximum dans `gestion-projet/comptes-rendus/`, sous 24 h.
- **Interne :** Discord pour l'informel ; toute décision qui touche le périmètre, le planning ou l'architecture passe dans le journal de bord.

## 1. Analyse de la demande

**Besoin reformulé :** KerLogis doit, d'ici la fin du semestre, pouvoir prouver à son client grand compte et à son assureur qu'il maîtrise ses risques cyber et sait reprendre son activité après un incident. Il attend (1) une analyse de risques EBIOS RM, (2) une maquette d'infrastructure modernisée qui supprime les points faibles majeurs et peut s'étendre au site de Rennes, et (3) pour le parcours PilPro, une recommandation chiffrée entre modernisation sur site et cloud public, le tout dans un budget contraint.

### Ce que le client dit, ce que nous comprenons

| Verbatim client | Traduction en besoin vérifiable | Question à poser au PO |
| --- | --- | --- |
| « Une infra qui ne tombe plus jamais en panne, mais peu de budget » | Contradiction : le « zéro panne » n'existe pas. On fixe par service une durée d'interruption maximale (RTO) et une perte de données maximale (RPO) acceptables, et on chiffre le coût de chaque niveau | Quel budget (investissement et annuel) ? Combien coûte une heure d'arrêt du WMS en haute saison ? |
| « Un accès simple mais sécurisé » | Comptes nominatifs, authentification forte (MFA) pour l'administration et la messagerie, une seule identité par personne (SSO) | Quels profils utilisent quoi ? Les scanners peuvent-ils porter un compte individuel ? |
| « Mon client veut des preuves » | Dossier de preuves : rapport EBIOS, plan de traitement, PV de test de restauration, PCA/PRA, politique d'accès | Pouvez-vous nous transmettre le questionnaire fournisseur et les exigences de l'assureur ? |
| « On ouvre à Rennes, il faut que ça suive » | Architecture reproductible : gabarit de site (VLAN, VPN inter-sites, sauvegarde), coût d'un site supplémentaire chiffré | Date d'ouverture, effectif et usages prévus à Rennes ? |
| « Si on est attaqué, savoir ce qui s'est passé et retrouver mes données » | Journalisation centralisée et conservée, supervision avec alertes, sauvegardes hors ligne ou immuables testées | Durée de conservation souhaitée des journaux ? Qui doit être alerté, et la nuit ? |

### Hypothèses de travail (à valider par le PO)

- H1. La maquette est réalisée sur un lab (Proxmox fourni par l'IUT ou VM imbriquées), sans toucher à la production KerLogis.
- H2. Odoo 12 / PostgreSQL 10 est le service le plus critique (WMS) : c'est lui qui sert de service pilote pour le MVP.
- H3. L'échéance « fin du semestre » du grand compte coïncide avec la restitution finale (S10).
- H4. Le budget est contraint : la solution privilégie l'open source (Proxmox, PBS, OPNsense, Zabbix/Wazuh).
- H5. L'application de tournées SaaS et la messagerie restent chez leurs éditeurs ; nous traitons leurs risques (MFA, comptes, contrats) sans les remplacer.
- H6. Le parcours PilPro garde les ateliers EBIOS et le socle technique ; l'étude financière remplace les études Cyber/DevCloud.

### Questions ouvertes pour la première interview

1. Budget : enveloppe d'investissement et coût annuel acceptable ? Qui décide ?
2. Criticité : quels services ne doivent jamais s'arrêter en haute saison ? Combien d'heures d'arrêt sont tolérables par service ? Combien de données peut-on perdre ?
3. Preuves : peut-on obtenir le questionnaire du grand compte et les exigences de l'assureur ? Date exacte d'échéance ?
4. Incidents passés : pannes ou attaques déjà subies, durée et coût ?
5. Rennes : date d'ouverture, nombre de postes, de scanners, liaison Internet prévue ?
6. Pics : volume de commandes et d'utilisateurs en novembre–janvier vs le reste de l'année ?
7. Prestataire externe : quel contrat, quels accès, peut-il utiliser un compte nominatif ?
8. Données personnelles : la géolocalisation continue des chauffeurs est-elle déclarée (registre RGPD, information des salariés) ? Qui est le référent RGPD ?
9. Locaux : salle serveur, onduleur, climatisation, débit Internet à Brest et Lorient ?
10. Préférences : contraintes de souveraineté ou fournisseur cloud imposé par le grand compte ?
11. Projet : quelles ressources de lab peut-on obtenir (nombre de VM, RAM, réseau) et sous quel délai ?

### Périmètre

| Dans le périmètre | Hors périmètre |
| --- | --- |
| Analyse de risques EBIOS RM (ateliers 1 à 5) sur le SI de Brest et Lorient, avec Rennes en projection | Migration réelle de la production KerLogis |
| Maquette fonctionnelle : virtualisation, sauvegarde testée, segmentation, comptes, supervision, reprise | Montée de version applicative d'Odoo (développement, reprise de données métier) |
| Documentation technique et procédures (installation, restauration, exploitation) | Achat de matériel, négociation de contrats fournisseurs |
| Étude financière PilPro : sur site vs cloud, Rennes, pics de saison, recommandation | Remplacement de l'application SaaS de tournées ou de la messagerie |
| Dossier de preuves pour le grand compte et l'assureur | Mise en conformité RGPD complète (seuls les risques sont identifiés et des mesures proposées) |
| Pilotage Kanban et relation client | Déploiement d'une gestion de flotte (MDM) sur les 30 scanners : étudiée, pas déployée |

## 2. Parties prenantes et parcours utilisateurs

Le besoin est porté par la direction (MOA), vécu par l'équipe informatique et les opérationnels, et imposé de l'extérieur par le grand compte et l'assureur. Notre équipe est la MOE.

### Cartographie

| Partie prenante | Rôle | Ce qu'elle attend | Influence | Intérêt |
| --- | --- | --- | --- | --- |
| Dirigeant de KerLogis | MOA – porte le besoin, décide du budget | Rassurer le grand compte et l'assureur, ne pas dépenser trop | Forte | Fort |
| Product Owner (enseignant) | Représentant de la MOA, valide les stories | Backlog clair, démos, transparence | Forte | Fort |
| Équipe informatique (1 admin, 1 technicien) | Utilisateur clé et futur exploitant | Moins de pannes subies, outils simples, fin du compte partagé | Moyenne | Fort |
| Exploitation et planification (6) | Utilisateurs métier | WMS disponible 24 h/24 en haute saison | Moyenne | Fort |
| Préparateurs et caristes (28) | Utilisateurs finaux (scanners) | Se connecter vite, ne jamais être bloqué | Faible | Moyen |
| Chauffeurs-livreurs (22) | Utilisateurs finaux (SaaS tournées) | Application qui marche, respect de leur vie privée (géolocalisation) | Faible | Moyen |
| Administratif, RH, direction, commerciaux (7) | Utilisateurs (fichiers, messagerie, portail) | Accès simple, messagerie fiable | Faible | Moyen |
| Client grand compte | Externe – prescripteur | Questionnaire fournisseur rempli, PCA crédible | Forte | Moyen |
| Assureur cyber | Externe – prescripteur | Preuves (MFA, sauvegardes testées, plan de réponse) | Forte | Moyen |
| Transporteurs et clients EDI | Externe – écosystème | Échanges SFTP continus et sûrs | Moyenne | Faible |
| Éditeur SaaS tournées, hébergeur mail | Externe – fournisseurs | Respect du contrat | Faible | Faible |
| Prestataire informatique externe | Externe – accès privilégié | Continuer à intervenir | Moyenne | Moyen |
| BreizhOps Conseil (notre équipe) | MOE – réalise, conseille, rend compte | Ressources de lab, réponses du client à temps | – | – |
| Enseignant référent (M. Duron) | Accompagnement, évaluation | Démarche visible | Forte | Fort |

Les externes (grand compte, transporteurs, SaaS, mail, prestataire) seront repris comme parties prenantes de l'écosystème à l'atelier 3 d'EBIOS.

### Parcours 1 – L'administrateur rétablit le WMS après une panne (parcours structurant du MVP)

Un mardi de décembre à 4 h, le serveur unique perd un disque puis plante. Aujourd'hui, l'admin l'apprend par un appel de préparateur, ne sait pas quelle sauvegarde est bonne et n'a jamais restauré. **Cible :** il est alerté automatiquement, identifie la VM touchée, restaure la dernière sauvegarde vérifiée sur un autre nœud en suivant une procédure écrite, contrôle que les préparateurs travaillent, et consigne l'incident (durée d'arrêt, données perdues).

### Parcours 2 – Le dirigeant prouve sa sécurité au grand compte et à l'assureur

Il reçoit le questionnaire fournisseur et ne sait pas quoi répondre. **Cible :** il dispose d'une analyse de risques lisible (cartographie gravité × vraisemblance), d'un plan de mesures hiérarchisé et chiffré, et de preuves datées (test de restauration, MFA activée, journalisation). Il choisit un scénario d'investissement (sur site ou cloud) à partir d'une recommandation argumentée, puis répond au questionnaire.

### Parcours 3 – Le préparateur travaille en pleine haute saison

Il prend son scanner, se connecte au Wi-Fi de l'entrepôt et ouvre ses missions dans le WMS. Aujourd'hui, le Wi-Fi a une clé affichée au mur et partage le réseau des serveurs. **Cible :** le scanner est sur un réseau dédié qui n'atteint que le WMS, l'accès reste aussi rapide, et une panne serveur est rétablie dans le délai convenu.

## 3. Story mapping

**MVP (R1) :** le WMS tourne sur une plateforme Proxmox administrée par comptes nominatifs avec MFA, il est sauvegardé automatiquement chaque nuit, sa restauration a été testée et chronométrée, et le dirigeant sait ce qu'il doit protéger (ateliers EBIOS 1 et 2). C'est le plus petit parcours de bout en bout : connaître → héberger → sauvegarder → reprendre → prouver.

Le parcours cartographié est celui de KerLogis (dirigeant + équipe informatique) : « sécuriser le SI et prouver qu'on sait reprendre l'activité ». Les activités se lisent de gauche à droite ; sous chaque activité, les stories vont de la plus essentielle à la plus accessoire. Chaque ligne est une ligne de release.

| Release | A1 Connaître ses risques | A2 Héberger les services | A3 Sauvegarder et restaurer | A4 Contrôler les accès | A5 Surveiller et détecter | A6 Reprendre après incident | A7 Prouver et décider |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **R1 – MVP** (S3–S4) | US-10 Atelier 1 · US-11 Atelier 2 | US-20 Lab Proxmox · US-21 WMS migré sur Proxmox | US-30 Sauvegarde nocturne automatisée (PBS) | US-40 Comptes admin nominatifs + MFA | (notification d'échec de sauvegarde suffisante en R1) | US-31 Restauration testée et chronométrée | US-70 Dossier de preuves v1 |
| **R2 – Risques et sécurité** (S5–S6) | US-12 Atelier 3 · US-13 Atelier 4 + cartographie des risques | US-24 Portail client en DMZ derrière reverse proxy | US-33 Sauvegarde des autres services | US-41 Segmentation VLAN + OPNsense · US-42 Réseau scanners · US-43 Droits par groupe · US-45 MFA messagerie | – | – | US-72 Inventaire et données de coûts |
| **R3 – Résilience et visibilité** (S7–S8) | US-14 Atelier 5 : plan de traitement | US-22 Haute disponibilité du WMS | US-32 Copie externalisée protégée | US-44 Coffre de secrets | US-50 Supervision et alertes · US-51 Journalisation centralisée | US-60 Simulation d'incident · US-61 PCA/PRA | US-73 Scénario sur site · US-74 Scénario cloud · US-71 Questionnaire fournisseur |
| **R4 – Expertise et finalisation** (S9–S10) | – | US-23 Gabarit de site Rennes (VPN inter-sites) | – | – | US-52 Cas de détection EBIOS* | US-62 Fiche réflexe rançongiciel* | US-75 Rennes et pics · US-76 Impacts et risques · US-77 Recommandation · US-78 Dossier technique · US-79 Restitution |

**Pourquoi ces lignes :**

- R1 couvre toutes les activités nécessaires pour répondre à la peur n°1 (« retrouver mes données ») sur le service le plus critique, avec une sécurité minimale non négociable (MFA admin).
- R2 traite le réseau à plat et les services exposés, que les ateliers 3 et 4 devraient classer parmi les scénarios les plus vraisemblables.
- R3 apporte la visibilité et la preuve chiffrée de reprise ; c'est aussi là que l'étude PilPro dispose des données techniques pour chiffrer les deux scénarios.
- R4 est consacrée à l'expertise PilPro et à la consolidation ; les stories « si capacité » sont les premières sacrifiées.
- Les stories de pilotage (US-01 à US-05) ne figurent pas sur la carte : elles ne font pas partie du parcours client.

## 4. Product Backlog, Definition of Ready et Definition of Done

Le backlog complet (41 stories ordonnées, critères d'acceptation « Étant donné / Quand / Alors », classe de service, MoSCoW, taille, dépendances, responsable et relecteur) est dans [`backlog/backlog_v0.csv`](../../backlog/backlog_v0.csv), versionné à chaque release. Le rang est proposé par l'équipe et décidé par le PO.

### Règles d'ordonnancement

1. **Valeur métier :** ce qui répond à l'échéance du grand compte et de l'assureur passe d'abord (sauvegarde testée, MFA, analyse de risques).
2. **Risque :** on traite tôt ce qui est incertain (obtention du lab, migration du WMS).
3. **Dépendances :** US-20 (lab) conditionne toute la technique ; US-10/11 conditionnent les ateliers 3 à 5 ; US-72 conditionne l'étude PilPro.
4. **Coût du retard :** les livrables liés à une démo sont en classe Date fixe.

### Exemple de story prête

**US-31 – Restauration testée et chronométrée** · A3 · R1 · Standard · Must · taille M · dépend de US-30

En tant qu'administrateur de KerLogis, je veux restaurer le WMS à partir de la dernière sauvegarde en suivant une procédure écrite, afin de savoir combien de temps il me faut pour reprendre l'activité après une panne.

- Étant donné une sauvegarde nocturne vérifiée du WMS et une commande test créée la veille, quand je restaure la VM sur un nœud de la plateforme en suivant la procédure, alors le WMS démarre et la commande test est présente.
- Étant donné la restauration terminée, quand je consulte le PV de test, alors il indique la date, l'opérateur, la durée mesurée (RTO) et l'âge de la sauvegarde (RPO).
- **Scénario de démo :** on supprime la VM WMS devant le PO, on la restaure en direct, le PO vérifie lui-même la présence de la commande test.

### Definition of Ready

- [ ] Rédigée « En tant que… je veux… afin de… » avec un acteur réel et une valeur exprimée (sinon c'est une tâche).
- [ ] Respecte INVEST, en particulier Small : réalisable en moins d'une semaine par une ou deux personnes.
- [ ] Au moins deux critères d'acceptation vérifiables et un scénario de démonstration.
- [ ] Dépendances levées ou planifiées ; ressources nécessaires demandées formellement au PO.
- [ ] Une classe de service et un domaine.

### Definition of Done

1. Tous les critères d'acceptation sont vérifiés et le résultat est démontrable sur la plateforme ou dans un livrable.
2. Relue ou testée par un autre membre que son auteur.
3. **Technique :** configuration exportée ou décrite dans le dépôt, testée en lab, procédure de retour arrière ou de restauration écrite si le changement est risqué, schéma draw.io et inventaire à jour.
4. **EBIOS / étude :** livrable au format convenu, sources et hypothèses citées, lien explicite avec les risques ou les stories concernées.
5. Documentation utile à l'exploitation remise (procédure, identifiants dans le coffre, jamais dans le document).
6. Dates de début et de fin renseignées sur la carte, PO informé.

## 5. Tableau Kanban

Tableau GitHub Projects (vue Board) partagé en lecture au PO ; limite de départ **3 cartes en En cours** pour 4 personnes.

### Colonnes, WIP et règles de sortie

| Colonne | WIP | Contenu | Règle de sortie |
| --- | --- | --- | --- |
| À faire | illimité | Stories ordonnées, issues de la planification de release | Story choisie en planification et conforme à la DoR |
| Analyse | 3 | Précision du besoin, questions au PO, découpage en tâches | Besoin compris, critères écrits et relus, risques et ressources identifiés, demande de ressources envoyée si besoin |
| En cours | 3 | Réalisation, un responsable nommé | Réalisé et testé par son auteur (en lab pour la technique), preuve jointe |
| À vérifier | 2 | Relecture ou test croisé | Relu ou testé par le relecteur, documentation à jour, DoD respectée |
| Terminé | – | Stories livrées | Critères validés, PO informé ; validation formelle en revue |

**Bloqué :** étiquette `bloqué` + commentaire « Cause / Responsable / Prochaine action / Date ». La carte reste dans sa colonne et compte dans le WIP. Une carte annulée est fermée avec un motif.

**Flux tiré :** quand En cours est plein, on aide à terminer ou débloquer une carte (relecture, binôme) avant d'en démarrer une nouvelle.

### Classes de service

| Classe | Exemples | Règle |
| --- | --- | --- |
| Expedite | Aléa PO bloquant, plateforme de démo en panne la veille d'une revue | Passe devant tout, une seule à la fois, peut dépasser le WIP ; annonce immédiate au PO |
| Date fixe | Livrables de démo (ateliers EBIOS, release notes, restitution) | Démarrée au plus tard à J-7 ; orange au point si non commencée à J-5 |
| Standard | Stories techniques et d'étude | Ordre du backlog |
| Intangible | Documentation, collecte de données, stories « si capacité » | Quand il reste de la capacité ; jamais plus d'1 carte en En cours |

### Étiquettes

- Classe : `expedite`, `date-fixe`, `standard`, `intangible`
- Domaine : `gestion-projet`, `ebios`, `infrastructure`, `documentation`, `etude-pilpro`
- Release : `R0` … `R4` · Autres : `bloqué`, `alea`

### Indicateurs de flux

Date de début (entrée en Analyse) et de fin (entrée en Terminé) sur chaque carte. À chaque point quotidien, le coordinateur relève le nombre de cartes en En cours.

- **Débit** = cartes terminées dans la release / nombre de semaines
- **WIP moyen** = moyenne des relevés de En cours
- **Temps de cycle moyen** = WIP moyen / débit (loi de Little), comparé à la moyenne réelle (fin − début)

### Indicateur d'état pour le PO

- **Vert :** livrables dans les temps, aucune carte bloquée depuis plus de 48 h.
- **Orange :** une carte Date fixe en léger retard, ou un blocage de plus de 48 h avec solution identifiée.
- **Rouge :** une story du MVP ou un livrable de démo compromis, ou un blocage sans solution.

## 6. Plan de release et cadence

Cinq releases de deux semaines, chacune close par une démo client ; le MVP est démontré le 18/12, avant les congés. Dates à caler sur l'emploi du temps de la SAE (planning visuel dans le [README](../../README.md#planning)).

| Release | Objectif | Stories | Démo client |
| --- | --- | --- | --- |
| R0 – Cadrage (S1–S2) | Le PO valide notre compréhension, le MVP et le plan. | US-01 à US-05 | Story map, backlog et plan ; validation par mail |
| R1 – Socle MVP (S3–S4) | Le WMS tourne sur Proxmox, est sauvegardé chaque nuit et sa restauration est prouvée. | US-20, 40, 21, 30, 31, 10, 11, 70 | Suppression puis restauration en direct de la VM WMS ; ateliers 1 et 2 |
| R2 – Risques et sécurité (S5–S6) | Le réseau est cloisonné et chaque mesure est reliée à un scénario de risque. | US-41, 42, 24, 43, 12, 13, 33, 72 (+45) | Un poste invité ne voit plus les serveurs ; un scanner n'atteint que le WMS ; cartographie des risques |
| R3 – Résilience et visibilité (S7–S8) | Une panne est détectée, rétablie et mesurée ; les deux scénarios financiers sont chiffrés. | US-50, 51, 22, 32, 14, 60, 61, 73, 74 (+44, 71) | Arrêt brutal d'un nœud : alerte, bascule, RTO/RPO mesurés ; plan de traitement |
| R4 – Expertise et finalisation (S9–S10) | La direction reçoit une recommandation argumentée et un dossier complet. | US-75, 76, 77, 23, 78, 79 (+52, 62) | Restitution finale |

### Capacité et lissage

Hypothèse à corriger avec le calendrier d'alternance réel : blocs de deux semaines école / entreprise. Semaine école = 4 × 2,5 j = 10 jours-personnes ; semaine entreprise = 4 × 0,5 j = 2 j-p ; congés = 0.

| Semaine | Dates | Période | Capacité réelle (j-p) | Capacité lissée (j-p) |
| --- | --- | --- | --- | --- |
| S1 | 23/11–27/11 | École | 10 | 6,8 |
| S2 | 30/11–04/12 | École | 10 | 6,8 |
| S3 | 07/12–11/12 | Entreprise | 2 | 6,8 |
| S4 | 14/12–18/12 | Entreprise | 2 | 6,8 |
| – | 21/12–01/01 | Congés | 0 | 0 |
| S5 | 04/01–08/01 | École | 10 | 6,8 |
| S6 | 11/01–15/01 | École | 10 | 6,8 |
| S7 | 18/01–22/01 | Entreprise | 2 | 6,8 |
| S8 | 25/01–29/01 | Entreprise | 2 | 6,8 |
| S9 | 01/02–05/02 | École | 10 | 6,8 |
| S10 | 08/02–12/02 | École | 10 | 6,8 |
| **Total** | | | **68** | **68** |

Conséquence : US-20 et US-21 doivent être analysées et la demande de ressources envoyée dès S2, pour que la faible capacité de S3–S4 serve à réaliser et pas à attendre. Pendant les congés, aucune story n'est prévue ; le lab reste allumé et la sauvegarde nocturne tourne, ce qui donne des données de RPO réelles à la rentrée.

### Rituels

| Rendez-vous | Quand | Durée | Qui | Ce qui en sort |
| --- | --- | --- | --- | --- |
| Point quotidien avec le PO | Créneaux de l'emploi du temps | 15 min max | Équipe + PO, devant le tableau | Fait / prévu / blocages, indicateur, relevé du WIP |
| Planification de release | Premier jour de chaque release | 30 min | Équipe + PO | Stories retenues, objectif, confirmation par mail |
| Revue de release | Dernier jour de chaque release | 20 min + 10 min de questions | Équipe + PO | Démo + diapositives, stories validées, release note |
| Rétrospective | Après la revue | 20 min | Équipe seule | Points +, points −, une amélioration tracée en carte |

## 7. Risques projet

| Risque | Probabilité | Impact | Parade |
| --- | --- | --- | --- |
| Ressources de lab obtenues tard | Moyenne | Bloque tout le MVP | Demande formelle dès S1 (US-20) ; plan B : Proxmox imbriqué sur un poste perso |
| Faible capacité en période entreprise | Forte | Stories R1 et R3 en retard | Analyse et préparation en semaine école ; WIP strict ; stories « si capacité » sacrifiées en premier |
| Le PO ne donne pas d'informations spontanément | Forte | Hypothèses fausses, étude financière fragile | Grille d'interview, CR validés par mail, hypothèses explicites dans chaque livrable |
| Cartes d'aléas en cours de release | Certaine | Glissement d'une story | Classe Expedite, une seule à la fois ; annonce écrite au PO avec l'impact |
| Haute disponibilité trop ambitieuse | Moyenne | Démo R3 ratée | Repli documenté : reprise depuis PBS sur un second nœud, RTO mesuré |
| Données de coûts peu fiables | Moyenne | Recommandation contestable | Sources datées, hypothèses chiffrées, analyse de sensibilité |
| Charge déséquilibrée dans l'équipe | Moyenne | Note individuelle modulée | Responsable sur chaque carte, rotation des rôles, point en rétrospective |

Journal de bord : [`gestion-projet/journal-de-bord.md`](../../gestion-projet/journal-de-bord.md) · Mails au PO : [`gestion-projet/mails/`](../../gestion-projet/mails/) · Modèle de release note : [`gestion-projet/release-notes/`](../../gestion-projet/release-notes/modele-release-note.md)
