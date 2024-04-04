import dataiku

def check_dataset_schema(dataset_type="Oracle"):
    """
    Affiche les noms des datasets dont le type correspond à dataset_type 
    et dont le schéma correspond au nom de la connexion.
    
    Args:
    - dataset_type (str): Type de la connexion des datasets à vérifier. Par défaut, "Oracle".
    """
    
    project_key = dataiku.default_project_key()
    project = dataiku.api_client().get_project(project_key)
    datasets = project.list_datasets()
    
    for dataset in datasets:
        if dataset['type'] == dataset_type:
            dataset_loc = dataiku.Dataset(dataset["name"]).get_location_info()
            schema = dataset_loc["info"].get("schema", "")
            connection = dataset_loc["info"].get("connectionName", "")
            
            if schema == connection:
                print(f"Dataset correspondant : {dataset['name']}")
            else:
                print(f"Dataset non correspondant (schema différent de la connexion) : {dataset['name']}")
        else:
            print(f"Dataset ignoré (type différent de {dataset_type}) : {dataset['name']}")

# Exemple d'utilisation
