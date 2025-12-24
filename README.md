# 📊 Analyse du Marché de l'Emploi Data Analyst (2025)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Power BI](https://img.shields.io/badge/Power%20BI-Desktop-yellow)
![Status](https://img.shields.io/badge/Status-Completed-success)

Ce projet est une analyse de données complète ("End-to-End") visant à décrypter les compétences les plus demandées pour les Data Analysts en 2025.
À partir d'un jeu de données brut de plus de **60 000 offres d'emploi**, j'ai construit un pipeline de nettoyage en Python et un tableau de bord interactif sur Power BI.

---

## 🎯 Objectifs du projet

L'objectif était de répondre de manière chiffrée aux questions que se posent tous les candidats en Data :
* **La guerre des langages :** Python a-t-il définitivement enterré R ?
* **L'impact financier :** Quelles compétences techniques augmentent le salaire moyen ?
* **Le cadre de travail :** Quelle est la part réelle du télétravail (Remote) vs Présentiel ?

## 🔍 Résultats Clés (Insights)

* **Le Duo Incontournable :** SQL (**51%**) et Excel (**53%**) restent les compétences les plus demandées, loin devant les langages de programmation.
* **Python vs R :** Python (**31%**) domine largement R (**20%**) sur le marché des Data Analysts.
* **Visualisation :** Tableau (**27%**) conserve une avance sur Power BI (**19%**) dans ce dataset spécifique.
* **Impact Salaire :** Les offres mentionnant Python affichent un salaire moyen supérieur à celles demandant uniquement Excel.

---

## 🛠️ Stack Technique

### 1. Python (Data Engineering & Cleaning)
* **Bibliothèque :** `pandas` pour la manipulation de données.
* **Technique avancée :** Utilisation d'expressions régulières (**Regex**) pour extraire précisément les compétences (ex: distinction entre "Go" le verbe et "Go" le langage, ou gestion du "C++").
* **Nettoyage :** Gestion des valeurs nulles, standardisation des salaires, détection des doublons.

### 2. Power BI (Data Visualization)
* **Modélisation :** Transformation des données via **Power Query** (Dépivotage des colonnes compétences).
* **DAX :** Création de mesures calculées (`DISTINCTCOUNT`, `AVERAGE`) pour des KPI dynamiques.
* **UX/UI :** Tableau de bord interactif avec filtres croisés (Cross-filtering) entre compétences, salaires et types de contrats.

---

## 📂 Structure du projet

```bash
├── main.py              # Script Python de nettoyage et d'extraction des données
├── jobs_final_bi.csv    # (Ignoré par Git) Fichier nettoyé prêt pour Power BI
├── report.pbix          # Fichier du tableau de bord Power BI
├── .gitignore           # Configuration pour exclure les fichiers lourds
└── README.md            # Documentation du projet
```

---

## 💾 Source des Données

Le dataset original provient de Kaggle. Il contient des métadonnées sur des milliers d'offres d'emplois (titre, description, salaire, localisation).
* **Source :** [Kaggle - Data Analyst Job Postings](https://www.kaggle.com/) *(Tu peux remplacer ce lien par l'URL exacte du dataset que tu as utilisé)*
* *Note : Les fichiers CSV bruts ne sont pas inclus dans ce dépôt GitHub pour respecter la limite de taille (<100Mo).*

---

## 🚀 Guide d'installation (Pour débutants)

Si vous souhaitez exécuter ce projet sur votre machine, suivez ces étapes :

### Étape 1 : Cloner le projet
Ouvrez votre terminal et lancez :
```bash
git clone [https://github.com/Manonsigilla/market-analyst-jobs-analysis.git](https://github.com/Manonsigilla/market-analyst-jobs-analysis.git)
cd market-analyst-jobs-analysis
```

### Étape 2 : Préparer les données
1.  Téléchargez le dataset depuis Kaggle (lien ci-dessus).
2.  Placez le fichier CSV dans le dossier du projet.
3.  Renommez-le si nécessaire pour correspondre au nom dans `main.py` (ou modifiez le script).

### Étape 3 : Lancer le script Python
Assurez-vous d'avoir Python installé. Installez la librairie Pandas :
```bash
pip install pandas
```

## Lancer le script de nettoyage

Exécutez la commande suivante :

```bash
python main.py
```

Cela va générer le fichier 'jobs_final_bi.csv'.

### Étape 4 : Ouvrir le Dashboard
* Installez Microsoft Power BI Desktop (gratuit sur Windows)
* Ouvrez le fichier 'report.pbix'.
* Si Power BI ne trouve pas la source de données (chemin du fichier modifié) :
** Allez dans Accueil > Transformer les données > Paramètres de la source de données.
** Cliquez sur Changer la source.
** Sélectionnez le fichier jobs_final_bi.csv que vous venez de générer sur votre ordinateur.

### Auteur

Manon — Aspiring Data Analyst

Passionnée par la data, je me forme actuellement aux outils de l’IA et de la Business Intelligence.
