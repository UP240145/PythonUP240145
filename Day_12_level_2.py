import random

def list_of_hexa_colors(n):
    hex_chars = '0123456789abcdef'
    colors = []
    for _ in range(n):
        color = '#' + ''.join(random.choice(hex_chars) for _ in range(6))
        colors.append(color)
    return colors

def list_of_rgb_colors(n):
    colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f"rgb({r},{g},{b})")
    return colors

def generate_colors(color_type, n):
    if color_type == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Tipo no soportado. Usa 'hexa' o 'rgb'."

print(generate_colors('hexa', 3)) 
print(generate_colors('hexa', 1))  
print(generate_colors('rgb', 3))  
print(generate_colors('rgb', 1))  
