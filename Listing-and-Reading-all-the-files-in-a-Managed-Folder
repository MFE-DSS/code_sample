'''Listing-and-Reading-all-the-files-in-a-Managed-Folder

Filtrer et copier des fichiers d'un dossier géré HDFS à un autre basé sur des motifs regex.

Solution 1: Utilisation d'une Recette code recipe Python

Étapes Clés:

    Importation et/ou vérifier que les librairies sont disponible dans le code environnement python associé à votre récipe : import re pour les expressions régulières.
    Accès aux Dossiers Gérés: Utilisation de dataiku.Folder pour accéder aux dossiers d'entrée et de sortie.
    Listage et Filtrage des Fichiers: Parcourir les fichiers dans le dossier d'entrée et appliquer le filtrage regex. (à modifier directement dans le fichier python.)
    Lecture et Écriture de Fichiers: Ouvrir les fichiers filtrés, lire leur contenu, et les écrire dans le dossier de sortie approprié. (à modifier directement dans le fichier python.)

Solution Alternative sans code : Définir dans les paramètres avancés du folder managed un critère de selection des fichiers pour crée les datasets output associés. Points à Noter:

    Moins flexible que la solution Python.
    Nécessite une configuration supplémentaire pour le routage des fichiers vers le dossier de sortie.
'''


import dataiku
import re

# Configuration des dossiers gérés
input_folder = dataiku.Folder("INPUT_MANAGED_FOLDER_ID")
output_folder1 = dataiku.Folder("OUTPUT_MANAGED_FOLDER1_ID")
output_folder2 = dataiku.Folder("OUTPUT_MANAGED_FOLDER2_ID")

# Listage et filtrage des fichiers
paths = input_folder.list_paths_in_partition()
for path in paths:
    if re.match(r"/[F|f]ile_\d+", path):
        # Copie vers output_folder1
        data = input_folder.get_download_stream(path).read()
        output_folder1.get_writer(path).write(data)
    elif re.match(r"/[i|I]nput_file_\d+", path):
        # Copie vers output_folder2
        data = input_folder.get_download_stream(path).read()
        output_folder2.get_writer(path).write(data)
