import dataiku
import paramiko
import pandas as pd

# Création d'une instance SSHClient de Paramiko
client_ssh = paramiko.SSHClient()

# Ajout automatique de la clé de l'hôte s'il manque
client_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Récupération des informations de connexion depuis les variables personnalisées de Dataiku
ssh_host = dataiku.get_custom_variables()["ssh_host"]
ssh_username = dataiku.get_custom_variables()["ssh_username"]
ssh_password = dataiku.get_custom_variables()["ssh_password"]

# Connexion au serveur SSH
client_ssh.connect(ssh_host, username=ssh_username, password=ssh_password)

# Ouverture d'une session SFTP
sftp_session = client_ssh.open_sftp()

# À partir d'ici, vous pouvez utiliser `sftp_session` pour effectuer des opérations SFTP, 
# comme sftp_session.get('remote_filepath', 'local_filepath') pour télécharger un fichier, 
# ou sftp_session.put('local_filepath', 'remote_filepath') pour en uploader.

# N'oubliez pas de fermer les sessions lorsque vous avez terminé
sftp_session.close()
client_ssh.close()
