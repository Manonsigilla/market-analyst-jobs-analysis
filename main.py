import pandas as pd

# Chargement des données nettoyées
df = pd.read_csv("jobs_cleaned_v1.csv")
df['description'] = df['description'].fillna("")

print("Extraction intelligente des compétences...")

# Dictionnaire : "Nom de la colonne" : "Mot clé Regex à chercher"
# r'...' permet d'écrire des regex sans problème
skills_map = {
    'python': r'python',
    'sql': r'sql',
    'excel': r'excel',
    'power_bi': r'power bi',
    'tableau': r'tableau',
    # Les corrections importantes :
    'r': r'\br\b',          # \b = limite de mot. Trouve " R " mais pas "Work"
    'go': r'\bgo\b',        # Trouve " Go " mais pas "Good"
    'c++': r'c\+\+',        # Le + est un caractère spécial, il faut mettre \ devant
    'aws': r'\baws\b',      # Pour éviter de trouver "laws" (lois)
    'spark': r'\bspark\b',
    'hadoop': r'\bhadoop\b',
    'docker': r'\bdocker\b',
    'kubernetes': r'\bkubernetes\b',
    'javascript': r'javascript',
    'java': r'\bjava\b',
    'html': r'html',
    'css': r'\bcss\b'
}

# On boucle sur le dictionnaire
for skill_name, pattern in skills_map.items():
    col_name = f"has_{skill_name}"
    # regex=True est activé par défaut, mais on le précise pour être sûr
    df[col_name] = df['description'].str.lower().str.contains(pattern, regex=True).astype(int)

# Affichage des résultats corrigés
print("\n--- VRAIS Pourcentages ---")
for skill_name in skills_map.keys():
    col_name = f"has_{skill_name}"
    pourcentage = df[col_name].mean() * 100
    print(f"{skill_name.capitalize()}: {pourcentage:.2f}%")

# Export final
df.to_csv("jobs_final_bi.csv", index=False)
print("\n✅ Fichier final 'jobs_final_bi.csv' généré ! Prêt pour Power BI.")