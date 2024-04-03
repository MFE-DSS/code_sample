from pyspark.sql import SparkSession

# Initialiser une session Spark avec une configuration de base
spark = SparkSession.builder \
    .appName("SparkSessionExample") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# Obtenir la version de Spark utilisée par la session
spark_version = spark.version

# Afficher la version de Spark pour vérifier l'environnement
print("La version de Spark installée est :", spark_version)

# Exemple d'opération Spark pour démontrer la configuration de session
# Vous pouvez remplacer cette partie par votre propre logique de traitement des données Spark
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]
columns = ["Language", "Users"]

df = spark.createDataFrame(data, schema=columns)

df.show()

# N'oubliez pas de stopper la session Spark une fois vos opérations terminées
spark.stop()
