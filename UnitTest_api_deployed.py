"""
Ce script illustre comment intégrer des tests unitaires directement dans le code d'une API développée avec l'API Designer. 
L'objectif est de permettre une validation automatique des fonctionnalités de l'API avant sa mise en production, en utilisant 
la bibliothèque unittest de Python. Les tests unitaires peuvent être exécutés en passant un paramètre spécifique lors de l'appel 
de l'API, ce qui permet de s'assurer que l'API fonctionne comme attendu sous divers scénarios d'entrée. Ce modèle est particulièrement 
utile dans les environnements de développement et de test, permettant aux développeurs d'intégrer des pratiques de test continu 
directement dans leur flux de travail API sans nécessiter d'outils ou de processus externes supplémentaires.
"""

import unittest
import traceback

# Initialization code here (e.g., load models, set up environment)

class TestApiPyFunction(unittest.TestCase):
    def test_api_py_function_success(self):
        """Test case for successful operation."""
        result = api_py_function(2, 3, 4)
        self.assertEqual(result, 14)  # 2 + 3 * 4 = 14

    def test_api_py_function_edge_cases(self):
        """Test case for edge cases."""
        # Example edge case
        result = api_py_function(0, 0, 0)
        self.assertEqual(result, 0)  # 0 + 0 * 0 = 0

def api_py_function(param1, param2, param3, perform_test=False):
    result = param1 + param2 * param3
    if perform_test:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestApiPyFunction)
        runner = unittest.TextTestRunner()
        test_result = runner.run(suite)
        if test_result.wasSuccessful():
            return result, "All tests passed successfully."
        else:
            return result, f"Tests failed. {test_result.failures}"
    return result

# Example on how to use it
# Note: In real use, the perform_test parameter would likely be controlled by an external condition or environment variable.
print(api_py_function(2, 3, 4, perform_test=True))
