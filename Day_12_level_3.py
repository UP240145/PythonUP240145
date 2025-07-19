import random

def shuffle_list(lst):
    shuffled = lst[:] 
    random.shuffle(shuffled)
    return shuffled

def unique_seven_numbers():
    return random.sample(range(10), 7)


# Ejemplo de uso:
lista = [1, 2, 3, 4, 5]
print("Lista original:", lista)
print("Lista mezclada:", shuffle_list(lista))

print("7 números únicos entre 0 y 9:", unique_seven_numbers())
