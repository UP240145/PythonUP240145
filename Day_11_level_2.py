import math
from collections import Counter
def evens_and_odds(number):#1
    evens = 0
    odds = 0
    for digit in str(number):
        if int(digit) % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds
def factorial(n):#2
    if n < 0:
        return "No definido para números negativos"
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
def is_empty(param):#3
    if param:
        return False
    else:
        return True
def calculate_mean(numbers):#4
    return sum(numbers) / len(numbers) if numbers else None
def calculate_median(numbers):
    n = len(numbers)
    if n == 0:
        return None
    sorted_nums = sorted(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid -1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]
def calculate_mode(numbers):
    if not numbers:
        return None
    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    if len(modes) == len(counts):
        return None  
    return modes
def calculate_range(numbers):
    if not numbers:
        return None
    return max(numbers) - min(numbers)
def calculate_variance(numbers):
    n = len(numbers)
    if n == 0:
        return None
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / n
def calculate_std(numbers):
    var = calculate_variance(numbers)
    if var is None:
        return None
    return math.sqrt(var)
print("evens_and_odds(1234567890):", evens_and_odds(1234567890))
print("factorial(5):", factorial(5))  
print("is_empty([]):", is_empty([]))  
print("is_empty([1,2]):", is_empty([1,2]))  
nums = [1, 2, 2, 3, 4, 5, 5, 5, 6]
print("calculate_mean:", calculate_mean(nums))          
print("calculate_median:", calculate_median(nums))      
print("calculate_mode:", calculate_mode(nums))          
print("calculate_range:", calculate_range(nums))        
print("calculate_variance:", calculate_variance(nums))  
print("calculate_std:", calculate_std(nums))            
