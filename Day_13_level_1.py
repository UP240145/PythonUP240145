numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_and_zero = [n for n in numbers if n <= 0]
print("Negativos y ceros:", neg_and_zero)

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat_list = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print("Lista aplanada:", flat_list)

tuplas = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("Lista de tuplas con potencias:")
for t in tuplas:
    print(t)

countries = [[('Finland', 'Helsinki')],
             [('Sweden', 'Stockholm')],
             [('Norway', 'Oslo')]]

formatted = [[
    country[0].upper(),
    country[0][:3].upper(),
    country[1].upper()
] for sublist in countries for country in sublist]
print("Países formateados:", formatted)

dict_list = [{'country': c[0].upper(), 'city': c[1].upper()} for sublist in countries for c in sublist]
print("Lista de diccionarios:", dict_list)

names = [[('Asabeneh', 'Yetayeh')],
         [('David', 'Smith')],
         [('Donald', 'Trump')],
         [('Bill', 'Gates')]]

full_names = [' '.join(name) for sublist in names for name in sublist]
print("Nombres concatenados:", full_names)

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else None
intercept = lambda m, x, y: y - m*x

m = slope(1, 2, 3, 6)
b = intercept(m, 1, 2)
print(f"Pendiente: {m}, Intercepto: {b}")
