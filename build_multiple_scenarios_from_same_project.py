# Importation des bibliothèques nécessaires
import time  # Importe la bibliothèque pour gérer les délais et les temps d'attente
import dataiku  # Importe la bibliothèque Dataiku pour interagir avec la plateforme Dataiku

# Liste des identifiants des scénarios à exécuter en parallèle
scenarios_ids_to_run = ["SCENARIO_1",
                        "SCENARIO_2",
                        "SCENARIO_3"]

# Initialisation de la liste pour stocker les résultats des scénarios
scenario_runs = []

# Obtention de l'API client Dataiku et du projet correspondant
client = dataiku.api_client()  # Initialise l'API client Dataiku
project = client.get_project(project_key="YOUR_PROJECT_KEY")  # Récupère le projet en utilisant sa clé

# Boucle pour chaque scénario à exécuter en parallèle
for scenario_id in scenarios_ids_to_run:
    scenario = project.get_scenario(scenario_id)  # Récupère le scénario spécifié par son ID

    trigger_fire = scenario.run()  # Déclenche l'exécution du scénario
    # Attente jusqu'à ce que le déclenchement réel du scénario ait commencé
    scenario_run = trigger_fire.wait_for_scenario_run()
    scenario_runs.append(scenario_run)  # Ajoute le résultat de l'exécution du scénario à la liste

# Boucle de surveillance de l'état de tous les scénarios en cours d'exécution
while True:
    any_not_complete = False
    for scenario_run in scenario_runs:
        # Met à jour le statut depuis l'API Dataiku
        scenario_run.refresh()
        if scenario_run.running:
            any_not_complete = True

    if any_not_complete:
        print("Au moins un scénario est encore en cours...")
    else:
        print("Tous les scénarios sont terminés")
        break
