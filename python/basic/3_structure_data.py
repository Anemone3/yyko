# list
my_list = [1, 2, 3]


# set

my_set = set([1, 2, 2, 3])
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
comunes = set_a & set_b  # Resultado: {3, 4} en O(min(len(a), len(b)))
unicos_en_a = set_a - set_b  # Resultado: {1, 2}
unicos_en_b = set_b - set_a  # Resultado: {1, 2}
print("Set coumnes: ", comunes)
print("Set unicos en a: ", unicos_en_a)
print("Set unicos en b: ", unicos_en_b)

# tuple
my_tuple = (1, 2, 3)


# diccionary
hash_map = {"key": "value"}


# collections:
from collections import Counter

cuenta = Counter("mississippi")
# Resultado: {'i': 4, 's': 4, 'p': 2, 'm': 1}
