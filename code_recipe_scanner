import dataiku

def list_and_count_code_recipes(target_recipe_types=None):
    """
    Liste et compte les recettes de code dans le projet courant, selon les types spécifiés.
    Convertit également le code des recettes SQL en minuscules et les stocke dans une liste.
    
    Args:
        target_recipe_types (list): Liste des types de recettes à compter. 
                                    Par défaut à ['python', 'R', 'sql_query'].
    
    Returns:
        list: Une liste des recettes SQL avec leur nom et code en minuscules.
    """
    if target_recipe_types is None:
        target_recipe_types = ['python', 'R', 'sql_query']
    
    project_key = dataiku.default_project_key()
    project = dataiku.api_client().get_project(project_key)
    recipes = project.list_recipes()

    code_recipe_count = 0
    sql_recipes_info = []

    for recipe in recipes:
        recipe_name = recipe['name']
        recipe_details = project.get_recipe(recipe_name).get_settings()
        recipe_type = recipe_details.get_recipe_raw_definition().get('type', '')

        if recipe_type in target_recipe_types:
            code_recipe_count += 1
            
            if recipe_type == 'sql_query':
                # Supposons que `get_payload()` renvoie le code SQL directement
                sql_code = recipe_details.get_payload()
                code_lowercase = sql_code.lower()
                sql_recipes_info.append({"name": recipe_name, "code": code_lowercase})

    # Affichage facultatif
    print(f"Total code recipes detected: {code_recipe_count}")
    for recipe_info in sql_recipes_info:
        print(f"Recipe Name: {recipe_info['name']}\nSQL Code in lowercase: {recipe_info['code']}\n")
            
    return sql_recipes_info

# Exemple d'utilisation
sql_recipes_info_lowercase = list_and_count_code_recipes()
print(sql_recipes_info_lowercase)
