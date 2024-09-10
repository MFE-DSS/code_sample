import dataiku
from dataiku import pandasutils as pdu
import pandas as pd
import time
import matplotlib.pyplot as plt
import random

# ### Introduction
# Dans ce notebook, nous allons comparer deux méthodes pour effectuer des opérations similaires, mais avec des niveaux d'optimisation différents. 
# Nous examinerons l'impact de l'optimisation de code en termes de performances : Manipulation des  array de dimension deux à travers deux approches Nested Loop VS Array Difference

# ## Exemple 1: Manipulation d'Array
# ### Méthode naïve
# La méthode naïve itère directement sur les indices de l'array pour réaliser les opérations demandées.

def naive_array_manipulation(n, queries):
    arr = [0] * n
    for a, b, k in queries:
        for i in range(a - 1, b):
            arr[i] += k
    val_max = 0
    for val in arr:
        if val > val_max:
            val_max = val
    return val_max

# ### Méthode optimisée
# La méthode optimisée utilise la technique de la "difference array" pour réduire le nombre d'itérations nécessaires.

def optimized_array_manipulation(n, queries):
    arr = [0] * (n + 1)
    for a, b, k in queries:
        arr[a - 1] += k
        if b < n:
            arr[b] -= k
    max_value = 0
    current_value = 0
    for val in arr:
        current_value += val
        if current_value > max_value:
            max_value = current_value
    return max_value

# Pour évaluer les performances de ces deux méthodes, nous allons générer des datasets de tailles croissantes et mesurer le temps d'exécution des deux approches.

sizes = [10, 100, 1000, 10000, 100000, 200000]
naive_times = []
optimized_times = []

for n in sizes:
    num_queries = max(1, n // 10)
    queries = [[random.randint(1, n), random.randint(1, n), random.randint(1, 1000)] for _ in range(num_queries)]

    start_time = time.time()
    naive_array_manipulation(n, queries)
    naive_times.append(time.time() - start_time)

    start_time = time.time()
    optimized_array_manipulation(n, queries)
    optimized_times.append(time.time() - start_time)

plt.figure(figsize=(10, 6))
plt.plot(sizes, naive_times, label='Naive Method', marker='o')
plt.plot(sizes, optimized_times, label='Optimized Method', marker='o')
plt.xlabel('Size of Array')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs. Size of Array')
plt.legend()
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.show()

# ## Exemple 2: Calcul de puissance modulaire
# ### Méthode naïve
# La méthode naïve effectue une multiplication répétée pour calculer le résultat final.

def naive_power_mod(a, b, c):
    result = 1
    for _ in range(b):
        result = (result * a) % c
    return result

# ### Méthode optimisée
# La méthode optimisée utilise la technique de l'exponentiation rapide (exponentiation par squaring) pour réduire le nombre d'opérations.

def optimized_power_mod(a, b, c):
    result = 1
    a = a % c
    while b > 0:
        if (b % 2) == 1:
            result = (result * a) % c
        b = b >> 1
        a = (a * a) % c
    return result

# Pour évaluer les performances de ces deux méthodes, nous allons générer des valeurs exponentielles croissantes et mesurer le temps d'exécution des deux approches.

size_exponents = [10, 100, 1000, 10000]
naive_times = []
optimized_times = []

a = 2
c = 999999937

for b in size_exponents:
    start_time = time.time()
    naive_power_mod(a, b, c)
    naive_times.append(time.time() - start_time)

    start_time = time.time()
    optimized_power_mod(a, b, c)
    optimized_times.append(time.time() - start_time)

plt.figure(figsize=(10, 6))
plt.plot(size_exponents, naive_times, label='Naive Method', marker='o')
plt.plot(size_exponents, optimized_times, label='Optimized Method', marker='o')
plt.xlabel('Exponent Value (b)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs. Exponent Value for Power Modulo')
plt.legend()
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.show()

# ### Conclusion
# En comparant les résultats des méthodes naïves et optimisées, nous pouvons clairement voir l'impact des techniques d'optimisation sur le temps d'exécution.
# Cela démontre l'importance d'écrire du code efficace, en particulier lorsqu'on travaille avec des ensembles de données de grande taille ou des calculs intensifs.