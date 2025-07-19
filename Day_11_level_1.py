import math
def add_two_numbers(a,b):#1
    return a+b
def area_of_circle(radius):#2
    return math.pi * radius * radius
def add_all_nums(*args):#3
    total = 0
    for arg in args:
        if not isinstance(arg, (int, float)):
            return f"Todos los argumentos deben ser números. '{arg}' no es válido."
        total += arg
    return total
def convert_celsius_to_fahrenheit(celsius):#4
    return (celsius * 9/5) + 32
def check_season(month):#5
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return 'Autumn'
    elif month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    else:
        return 'Mes no válido'
def calculate_slope(x1, y1, x2, y2):#6
    if x2 == x1:
        return "Pendiente indefinida (división por cero)"
    return (y2 - y1) / (x2 - x1)
def solve_quadratic_eqn(a, b, c):#7
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No tiene soluciones reales"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"Una solución: x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Dos soluciones: x1 = {x1}, x2 = {x2}"
def print_list(lst):#8
    for item in lst:
        print(item)
def reverse_list(arr):#9
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
def capitalize_list_items(items):#10
    return [item.capitalize() for item in items]
def add_item(lst, item):#11
    lst.append(item)
    return lst
def remove_item(lst, item):#12
    if item in lst:
        lst.remove(item)
    return lst
def sum_of_numbers(n):#13
    return sum(range(n + 1))
def sum_of_odds(n):#14
    return sum(i for i in range(n + 1) if i % 2 != 0)
def sum_of_even(n):#15
    return sum(i for i in range(n + 1) if i % 2 == 0)
print(add_two_numbers(3, 7))
print(f"Área círculo radio 5: {area_of_circle(5):.2f}")
print(add_all_nums(1, 2, 3, 4))
print(add_all_nums(1, 'a', 3))
print(convert_celsius_to_fahrenheit(0))
print(convert_celsius_to_fahrenheit(100))
print(check_season('March'))
print(check_season('november'))
print(check_season('hello'))
print(calculate_slope(1, 2, 3, 6))
print(calculate_slope(2, 3, 2, 7))
print(solve_quadratic_eqn(1, -3, 2)) 
print(solve_quadratic_eqn(1, 2, 1))
print(solve_quadratic_eqn(1, 0, 1))
print_list(['manzana', 'banana', 'cereza'])  
print(reverse_list([1, 2, 3, 4]))
print(capitalize_list_items(['mango', 'banana']))      
print(add_item([1, 2, 3], 4))                         
print(remove_item(['a', 'b', 'c'], 'b'))               
print(sum_of_numbers(5))                               
print(sum_of_odds(5))                                  
print(sum_of_even(6))                                  
