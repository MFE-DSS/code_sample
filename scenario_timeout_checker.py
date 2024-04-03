import time
import dataiku
from dataiku.scenario import Scenario
from dataikuapi.dss.future import DSSFuture

# Initialisation d'une instance de scénario
s = Scenario()

# Récupération de l'instance du projet courant
client = dataiku.api_client()
project = client.get_default_project()

# Récupération de la variable de projet pour le timeout
project_variables = project.get_variables()
# Ici, 'average_scenario_time_limit' est un nom générique pour la variable de projet.
# Assurez-vous de définir cette variable dans les paramètres de votre projet.
TIMEOUT_SECONDS = float(project_variables["standard"].get("average_scenario_time_limit", 3600))

# Début du traitement d'un exemple de step dans le scénario
# Remplacez "nom_du_dataset" par le nom réel du dataset que vous souhaitez construire
step_handle = s.build_dataset("nom_du_dataset", asynchronous=True)

start = time.time()
while not step_handle.is_done():
    end = time.time()
    # Vérification si le temps de traitement dépasse le TIMEOUT_SECONDS
    if end - start > TIMEOUT_SECONDS:
        # Abandon du traitement si le timeout est dépassé
        future = DSSFuture(client, step_handle.future_id)
        future.abort()
        # Configuration d'une alerte ou notification si nécessaire
        raise Exception("Scénario interrompu : limite de temps moyenne de traitement dépassée.")
    else:
        print(f"En cours d'exécution... Durée : {int(end-start)}s")
    # Attente avant la prochaine vérification pour minimiser la charge
    time.sleep(10)
