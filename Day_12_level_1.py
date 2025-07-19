import random
import string

def random_user_id():
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def user_id_gen_by_user():
    characters = string.ascii_lowercase + string.digits
    try:
        length = int(input("Número de caracteres por ID: "))
        count = int(input("Número de IDs a generar: "))
    except ValueError:
        return "Por favor ingresa números enteros válidos."

    ids = []
    for _ in range(count):
        new_id = ''.join(random.choice(characters) for _ in range(length))
        ids.append(new_id)

    return ids

if __name__ == "__main__":
    print("ID aleatorio de 6 caracteres:", random_user_id())

    print("\nGenerador personalizado de IDs:")
    ids = user_id_gen_by_user()
    if isinstance(ids, list):
        for user_id in ids:
            print(user_id)
    else:
        print(ids)
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())
