### A INTEGRER DANS LES CODES ENVS PYTHONS DSS COMPATIBLES ###
import os
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sentence_transformers import SentenceTransformer

# Configuration du chemin pour le modèle pré-entraîné
# Utiliser une variable d'environnement pour spécifier le chemin de stockage des modèles
MODEL_HOME = os.getenv('MODEL_HOME', './models')
print("Chemin du répertoire des modèles :", MODEL_HOME)

# Nom du modèle pré-entraîné à charger
MODEL_NAME = 'sentence-transformers/all-MiniLM-L6-v2'

# Chargement du modèle à partir de Hugging Face ou du chemin local spécifié
# Assurez-vous que le modèle est disponible dans MODEL_HOME si vous n'utilisez pas la version de Hugging Face
try:
    model = SentenceTransformer(MODEL_NAME)
except OSError:
    # Si le modèle n'est pas trouvé, tentez de le charger depuis un chemin local
    model_path = os.path.join(MODEL_HOME, MODEL_NAME.replace('--', '/'))
    print(f"Tentative de chargement du modèle depuis {model_path}")
    model = SentenceTransformer(model_path)

# Exemple de phrases pour obtenir des embeddings
sentences = ["I really like ice cream.", "Brussels sprouts are okay too."]

# Obtention des embeddings des phrases
embeddings = model.encode(sentences)
print("Embeddings des phrases :", embeddings)

# Exemple d'utilisation de `AutoTokenizer` et `AutoModel` pour plus de flexibilité
# Chargez spécifiquement un tokenizer et un modèle pour la classification de séquences ou d'autres tâches
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model_for_seq = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# Tokenisation des phrases pour préparation à l'inférence
inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")

# Inférence avec le modèle (exemple pour classification)
outputs = model_for_seq(**inputs)
print("Sorties du modèle pour classification :", outputs)
