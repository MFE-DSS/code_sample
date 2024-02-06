import dataiku
from dataikuapi.dss.dataset import DSSDatasetSettings

'''
Flat file repositories on DSS instances are automatically interpreted by Dataiku according to their format. 
for excel/csv files, the Parse next line as column headers parameter is often the default.
In some case, issue comes from the "Use row 0 as column names" option, which is an older processor that doesn't work well with file datasets (the processor has been deprecated in later versions of DSS). You'll need to remove this processor and, instead, in the input dataset parameters, use "Parse next row as headers". Then go to the Schema tab in the dataset parameters, 
delete all columns, then click on "Check schema consistency" and then on "reload from data".
'''

def get_project(client, project_key=None):
    """
    Récupère le projet Dataiku DSS, soit par la clé fournie, soit par défaut.
    """
    if project_key:
        print(f"Récupération du projet : {project_key}")
        return client.get_project(project_key)
    else:
        print("Récupération du projet par défaut.")
        return client.get_default_project()

def filter_csv_datasets(datasets):
    """
    Filtre les datasets au format CSV ou Excel.
    """
    return [
        ds for ds in datasets
        if ds['type'] == 'UploadedFiles' and ds['formatType'] in ['excel', 'csv']
    ]

def disable_parse_header(dataset):
    """
    Désactive l'option 'Parse next line as column headers' pour un dataset.
    """
    settings = dataset.get_settings()
    format_settings = settings.get_raw().get('formatParams', {})
    
    # Vérification et modification si nécessaire
    if format_settings.get('parseHeaderRow', False):
        print(f"Désactivation de 'Parse next line as column headers' pour : {dataset.name}")
        format_settings['parseHeaderRow'] = False
        settings.save()
    else:
        print(f"'Parse next line as column headers' déjà désactivé pour : {dataset.name}")


        
# Définir project_key si le script s'éxecute à l'exterieur du projet à traiter sinon remplacer par client.get_default_project 

def main():
    client = dataiku.api_client()
    project_key = 'WIKI_POC'
    project = get_project(client, project_key)
    
    try:
        datasets = project.list_datasets()
        csv_datasets = filter_csv_datasets(datasets)
        
        if not csv_datasets:
            print("Aucun dataset CSV ou Excel trouvé.")
            return
        
        for ds_info in csv_datasets:
            ds = project.get_dataset(ds_info['name'])
            disable_parse_header(ds)
            
    except Exception as e:
        print(f"Erreur lors de l'exécution du script : {e}")

if __name__ == "__main__":
    main()
