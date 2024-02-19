
'''
This script performs non-regression tests on a Dataiku DSS project to ensure the stability and consistency of Spark, R, Python versions, integration with graphical interfaces, various connectors (Oracle, PostgreSQL, Hive, Cloud), and overall system health (Centos/Java/Linux versions). It includes functions to:
- Check Spark version by creating a SparkSession.
- Verify system instance systeme versions (OS, Java).
- List and verify code environments for Python and R, including checking their versions against expected values.
- List datasets, checking their types and schemas to detect any unintended changes.
- The script also intends to execute specific tests like exporting a dashboard to JPEG to verify graphical integration and perform schema checks on datasets to ensure no unexpected (schema etc.) changes have occurred.
'''
'''
check python & R version integrate
check deep install tools
build autotest project and send an email report to admin system
enpackage it as a recipe-tool in the main toolsbox pluggin'''

import dataiku
import subprocess
import platform
from pyspark.sql import SparkSession

# create spark session and close it.
def check_spark_version():
    spark = None
    try:
        spark = SparkSession.builder.appName("VersionCheck").getOrCreate()
        print("Spark Version:", spark.version)
    finally:
        if spark:
            spark.stop()
            print("Spark session stopped.")

# check OS/Java version
def check_system_version():
    print("OS Version:", platform.platform())
    java_version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)
    print("Java Version:", java_version.decode().split('\n')[0])

# R and Python code environment versions
def get_code_env_mapping():
    client = dataiku.api_client()
    project_key = dataiku.default_project_key()
    project = client.get_project(project_key)
    mapping = {"python": [], "r": []}
    defaults = get_instance_default_code_env()
    all_recipes = project.list_recipes()

    for recipe in all_recipes:
        recipe_type = recipe['type']
        if recipe_type in ["python", "r"]:
            env_selection = recipe.get('settings', {}).get('envSelection', {})
            env_mode = env_selection.get('envMode', 'INHERIT')
            env_name = env_selection.get('envName', defaults[recipe_type])

            if env_mode == 'EXPLICIT_ENV' and env_name:
                mapping[recipe_type].append({"name": recipe['name'], "code_env": env_name})
            elif env_mode == 'INHERIT':
                mapping[recipe_type].append({"name": recipe['name'], "code_env": defaults[recipe_type]})
            else:
                pass
    return mapping

def get_project_code_envs():
    client = dataiku.api_client()
    project_key = dataiku.default_project_key()
    project = client.get_project(project_key)

    # Initialize a dict to hold the environments for Python and R
    code_envs = {"python": [], "r": []}

    # Retrieve the mapping of recipes to their code environments
    mapping = get_code_env_mapping()

    for lang, items in mapping.items():
        for item in items:
            env_name = item['code_env']
            # Check if the environment is not already in the list
            if env_name not in code_envs[lang]:
                code_envs[lang].append(env_name)

    # Print the environments for Python and R
    for lang, envs in code_envs.items():
        print(f"{lang.upper()} Environments: {', '.join(envs)}")


def get_instance_default_code_env():
    """Return the global default code environments for Python and R at the instance level."""
    client = dataiku.api_client()
    defaults = {}
    general_settings = client.get_general_settings().get_raw()

    # Default environments for Python and R might be set at the instance level
    # Adjust the keys based on your DSS version and setup
    defaults['python'] = general_settings.get('codeEnvs', {}).get('python', {}).get('defaultEnv', 'dss_builtin')
    defaults['r'] = general_settings.get('codeEnvs', {}).get('r', {}).get('defaultEnv', 'dss_builtin')

    return defaults



# controle input datasets, check their types and schema
def list_and_check_datasets(project_key):
    client = dataiku.api_client()
    project = client.get_project(project_key)
    datasets = project.list_datasets()

    for dataset in datasets:
        ds = project.get_dataset(dataset['name'])
        settings = ds.get_settings()
        schema = ds.get_schema()
        schema_columns = [col['name'] for col in schema.get('columns', [])]

        # Example for schema check - Compare with a reference schema if available
        reference_schema_columns = ["column1", "column2"]  # Define your reference schema columns here
        if set(schema_columns) == set(reference_schema_columns):
            schema_status = "Good"
        else:
            schema_status = "Check"  # Indicates that the schema has changed or needs review

        print(f"Dataset: {dataset['name']}, Type: {settings.get_raw().get('type', 'Unknown')}, Columns: {schema_columns}, Schema Status: {schema_status}")



def check_code_env_versions():
    client = dataiku.api_client()
    code_envs = client.list_code_envs()
    for env in code_envs:
        lang = env.get("envLang")
        env_name = env.get("envName")
        if lang in ['PYTHON', 'R']:
            try:
                env_settings = client.get_code_env(lang, env_name).get_settings().get_raw()
                version_info = env_settings.get('desc', {})
                version = version_info.get('pythonVersion', version_info.get('rVersion', 'Unknown'))
                print(f"{lang} Environment: {env_name} - Version: {version}")
            except Exception as e:
                print(f"Error retrieving version for {env_name}: {e}")


# redéfinir la variable project_key dans le cas où la cible n'est pas self_project
def main():
    project_key = "TODELETE"

    print("\nChecking Spark Version...")
    check_spark_version()

    print("\nChecking System Versions...")
    check_system_version()

    print("\nChecking Code Environment Versions...")
    get_project_code_envs()
    check_code_env_versions()

    print("\nListing and Checking Datasets...")
    list_and_check_datasets(project_key)

if __name__ == "__main__":
    main()
