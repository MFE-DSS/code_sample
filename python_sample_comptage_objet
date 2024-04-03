import dataiku

# Obtention de l'instance du projet courant
project = dataiku.api_client().get_default_project()

# Récupération de la liste des datasets et des recipes dans le projet
datasets = project.list_datasets()
recipes = project.list_recipes()

# Initialisation des compteurs
count_datasets = len(datasets)
count_recipes = len(recipes)

# Affichage des résultats
print(f"Nombre de datasets : {count_datasets}")
print(f"Nombre de recipes : {count_recipes}")
