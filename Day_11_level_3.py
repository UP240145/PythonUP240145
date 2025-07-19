import sys
import os
ruta_data = os.path.abspath('30-Days-Of-Python\data')
if ruta_data not in sys.path:
    sys.path.append(ruta_data)
from countries_data import countries_data
import keyword
import re
from collections import Counter
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def all_unique(items):
    return len(items) == len(set(items))
def all_same_type(items):
    if not items:
        return True
    first_type = type(items[0])
    return all(isinstance(item, first_type) for item in items)
def is_valid_variable(var_name):
    if not isinstance(var_name, str):
        return False
    if keyword.iskeyword(var_name):
        return False
    pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
    return bool(re.match(pattern, var_name))
def most_spoken_languages(countries_data, top_n=10):
    language_counter = Counter()
    for country in countries_data:
        languages = country.get('languages', [])
        for lang in languages:
            language_counter[lang] += 1
    return language_counter.most_common(top_n)
def most_populated_countries(countries_data, top_n=10):
    sorted_countries = sorted(countries_data, key=lambda c: c.get('population', 0), reverse=True)
    return [(country['name'], country['population']) for country in sorted_countries[:top_n]]
print("¿Es 17 primo?", is_prime(17))  
print("¿Todos únicos [1,2,3,4,5]?", all_unique([1,2,3,4,5]))  
print("¿Todos mismo tipo [1, 2, 3]?", all_same_type([1, 2, 3])) 
print("¿'var_name' es variable válida?", is_valid_variable('var_name'))  
print("¿'2var' es variable válida?", is_valid_variable('2var'))  

print("\nTop 10 idiomas más hablados:")
for lang, count in most_spoken_languages(countries_data, 10):
    print(f"{lang}: {count} países")

print("\nTop 10 países más poblados:")
for name, pop in most_populated_countries(countries_data, 10):
    print(f"{name}: {pop:,} personas")