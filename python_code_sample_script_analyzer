import dataiku
import dataikuapi
import pandas as pd
import re
from radon.complexity import cc_visit

# Récupération variable light : uniquement custom
def get_dataiku_variables():
    try:
        return dataiku.get_custom_variables()
    except Exception as e:
        print(f"Erreur lors de la récupération des variables de Dataiku : {e}")
        return {}

# Calcul de la complexité cyclomatique
def calculate_complexity(recipe_code):
    try:
        blocks = cc_visit(recipe_code)
        return max(block.complexity for block in blocks) if blocks else None
    except Exception as e:
        print(f"Erreur lors du calcul de la complexité : {e}")
        return None

# Détection les variables Dataiku du recipe code
def detect_global_dataiku_variables(recipe_code, dataiku_vars):
    detected_vars = set()
    lines = [line.strip() for line in recipe_code.split('\n') if line.strip() and not line.strip().startswith('#')]
    pattern = r"dataiku\.get_custom_variables\(\)\[\"([^\"]+)\"\]"
    for line in lines:
        matches = re.findall(pattern, line)
        detected_vars.update(match for match in matches if match in dataiku_vars)
    return detected_vars

def main():
    project_key = "YOUR_PROJECT_KEY"
    project = dataiku.api_client().get_project(project_key)
    recipe_list = project.list_recipes()

    recipe_codes_df = pd.DataFrame(columns=["Recipe Name", "Recipe Code"])
    recipe_stats_df = pd.DataFrame(columns=["Recipe Name", "Code Size (bytes)", "Number of Lines"])
    dataiku_vars = get_dataiku_variables()

    for recipe in recipe_list:
        if recipe["type"] == "python":
            recipe_name = recipe["name"]
            try:
                recipe_obj = project.get_recipe(recipe_name)
                recipe_code = dataikuapi.dss.recipe.DSSRecipe.get_settings(recipe_obj).data['payload'].strip()

                recipe_codes_df = recipe_codes_df.append({"Recipe Name": recipe_name, "Recipe Code": recipe_code}, ignore_index=True)
                code_size = len(recipe_code)
                num_lines = recipe_code.count('\n')
                recipe_stats_df = recipe_stats_df.append({"Recipe Name": recipe_name, "Code Size (bytes)": code_size, "Number of Lines": num_lines}, ignore_index=True)

                # ajout des critères d'évaluation / best-practice interne
                ##
                ##
                ##
                
            except Exception as e:
                print(f"Erreur lors du traitement de la recette {recipe_name}: {e}")

    for index, row in recipe_stats_df.iterrows():
        recipe_name = row["Recipe Name"]
        recipe_code = recipe_codes_df.loc[index, "Recipe Code"]

        complexity = calculate_complexity(recipe_code) if recipe_code.strip() else None
        detected_dataiku_vars = detect_global_dataiku_variables(recipe_code, dataiku_vars)

        #Résultat output
        print(f"{recipe_name} - Code Size: {row['Code Size (bytes)']} bytes, Number of Lines: {row['Number of Lines']}, Complexity: {complexity}, Dataiku Variables: {detected_dataiku_vars}")

if __name__ == "__main__":
    main()
