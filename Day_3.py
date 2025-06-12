import math
#1, 2, 3, 4
age=18
height=1.7
comp=3+2j
base=float(input("Enter the base of the triangle: "))
triangle_height=float(input("Enter the height of the triangle: "))
area=(base*triangle_height*0.5)
print("The area of your triangle is: ",area,".")
#5
triangle_a=float(input("Enter side a: "))
triangle_b=float(input("Enter side b: "))
triangle_c=float(input("Enter side c: "))
perimeter=triangle_a+triangle_b+triangle_c
print("The perimeter of your triangle is: ",perimeter,".")
#6
rectangle_lenght=float(input("Enter the lenght of your rectangle:"))
rectangle_width=float(input("Enter the width of your rectangle:"))
rectangle_area=rectangle_lenght*rectangle_width
rectangle_perimeter=2(rectangle_lenght+rectangle_width)
print("The perimeter of your rectangle is: ",rectangle_perimeter,", the area of your rectangle is: ",rectangle_area,".")
#7
circle_radius=float(input("Enter the radius of your circle: "))
circle_area=3.14*(circle_radius*circle_radius)
circle_circumference=2*3.14*circle_radius
print("The circumference of your circle is: ",circle_radius,", the area of your circle is: ",circle_area,".")
#8
slope = 2
y_intercept = -2  
x_intercept = -slope / y_intercept  
print("Given equation: y = 2x - 2")
print("Slope:", slope)
print("Y-intercept:", y_intercept, "(Point: (0,", y_intercept, "))")
print("X-intercept:", x_intercept, "(Point: (", x_intercept, ", 0))")
#9
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Point 1:", (x1, y1))
print("Point 2:", (x2, y2))
print("Slope:", slope)
print("Euclidean Distance:", distance)
#10
slope_task8 = 2
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_task9 = (y2 - y1) / (x2 - x1)
print("Slope from Task 8 (y = 2x - 2):", slope_task8)
print("Slope from Task 9 (points (2,2) and (6,10)):", slope_task9)
if slope_task8 == slope_task9:
    print("The slopes are equal.")
else:
    print("The slopes are different.")
#11
x=float(input("Enter the value of x: "))
y = (x*x)+6*x+9
#it will be 0 when x is equal to -3
#12
word1 = "python"
word2 = "dragon"
len_word1 = len(word1)
len_word2 = len(word2)
print("Length of 'python':", len_word1)
print("Length of 'dragon':", len_word2)
comparison = len_word1 == len_word2
print("Are the lengths equal?", comparison)
#13
contains_on='on' in word1 and 'on' in word2
print("'on' found in both 'python' and 'dragon'?", contains_on)
#14
sentence="I hope this course is not full of jargon."
contains_jargon='jargon' in sentence
print("'jargon' found in sentence 1?",contains_jargon,)
#16
text="python"
length = len(text)
print("Length (integer):", length)
length_float = float(length)
print("Length (float):", length_float)
length_str = str(length_float)
print("Length (string):", length_str)
#17
num=float(input("Enter a number"))
if num%2 == 0:
    print("The number is even")
else:
    print("The number isnt even")
#19
print(type('10'))
print(type(10))
#20
n1=int(9.8)
n2=10
if n1 == n2:
    print("The two numbers are equal")
else:
    print("The numbers arent equal")
#21
hours=float(input("Enter the hours you work weekly: "))
rate=float(input("Enter the rate you get for hour: "))
if hours < 0 or rate < 0:
    print("Error")
else:
    earning=hours*rate
    print("Your weekly earning is: ",earning,)
#22
years=float(input("Enter the number of years you have lived"))
if years<0:
    print("error")
else:
    seconds= years*86400*365
    print("You have lived: ",seconds," seconds.")