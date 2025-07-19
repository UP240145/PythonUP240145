import sys
import os
ruta_data = os.path.abspath('30-Days-Of-Python\data')
if ruta_data not in sys.path:
    sys.path.append(ruta_data)
from countries import countries
from countries_data import countries_data
land_countries = [c for c in countries if 'land' in c]
print("Países con 'land':", land_countries)
fruitlist = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruitlist) - 1, -1, -1):
    reversed_fruits.append(fruitlist[i])
print(reversed_fruits)
all_languages = []

for country in countries_data:
    all_languages.extend(country['languages'])

unique_languages = set(all_languages)
print("Total de idiomas únicos:", len(unique_languages))
from collections import Counter

language_counts = Counter()

for country in countries_data:
    for lang in country['languages']:
        language_counts[lang] += 1

top_10_languages = language_counts.most_common(10)

print("\n10 idiomas más hablados:")
for lang, count in top_10_languages:
    print(f"{lang}: {count} países")
top_10_populated = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]

print("\n10 países más poblados:")
for country in top_10_populated:
    print(f"{country['name']}: {country['population']:,} personas")
