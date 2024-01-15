import dataiku
import time

# Dictionnaire de correspondance entre les clés de projet et les clés de scénario (noms génériques d'exemple)
dict_projects_scenarios_ids_to_run = {
    "Project1": "Scenario1",
    "Project2": "Scenario2",
    "Project3": "Scenario3",
    "Project4": "Scenario4",
    "Project5": "Scenario5",
    "Project6": "Scenario6",
    "Project7": "Scenario7",
    "Project8": "Scenario8",
    "Project9": "Scenario9",
}

scenario_runs = []

# Création du client API Dataiku
client = dataiku.api_client()

# Boucle pour chaque projet et scénario dans le dictionnaire
for project_key, scenario_key in dict_projects_scenarios_ids_to_run.items():
    print("Project Key : ", project_key)
    print("Scenario Key : ", scenario_key)

    # Récupération du projet et du scénario
    project = client.get_project(project_key=project_key)
    scenario = project.get_scenario(scenario_key)

    # Déclenchement de l'exécution du scénario
    trigger_fire = scenario.run()

    # Attente jusqu'à ce que le déclenchement réel du scénario ait commencé
    scenario_run = trigger_fire.wait_for_scenario_run()
    scenario_runs.append(scenario_run)

# Surveillance de l'état de tous les scénarios en cours d'exécution
while True:
    any_not_complete = False
    for scenario_run in scenario_runs:
        # Mise à jour du statut depuis l'API Dataiku
        scenario_run.refresh()
        if scenario_run.running:
            any_not_complete = True

    if any_not_complete:
        print("Au moins un scénario est encore en cours...")
    else:
        print("Tous les scénarios sont terminés")
        break

    # Attente avant de vérifier à nouveau l'état
    time.sleep(30)

# Vérification des résultats de l'exécution des scénarios
for sr in scenario_runs:
    print(sr.outcome)
    if sr.outcome == 'FAILED':
        raise Exception

# Affichage des ID des scénarios et de leurs résultats d'exécution
print("Résultats des scénarios : %s" % ([(sr.id, sr.outcome) for sr in scenario_runs]))
