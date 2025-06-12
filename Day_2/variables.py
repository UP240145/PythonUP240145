#Day 2:30 Days of python programing
#level 1
firstname="Adrian"
lastname="Lezama"
fullname="Adrian Lezama Ibarra"
country="mexico"
city="Aguascalientes"
age=18
year=2025
is_married="No"
is_true="Yes"
is_light_on="Yes"
#Level2
#1
print(type(firstname))
print(type(lastname))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
#2
print(len(firstname))
print(len(lastname))
#3
diferencia=len(firstname)-len(lastname)
print("The diference in lenght between firstname and lastname is: ",diferencia,)
#4, 5, 6, 7, 8, 9, 10
num_one=5
num_two=4
total=num_one+num_two
diff=num_one-num_two
product=num_one*num_two
division=num_one/num_two
reminder=num_two/num_one
i=0
exp=num_one
while i < num_two:
    exp=num_one*exp
    i=i+1

print(total)
print(diff)
print(product)
print(division)
print(reminder)
print(exp)
#11, 12
floor_division=num_one//num_two
radius=30
area_of_circle=3.1416*(radius*radius)
circum_of_circle=3.1416*(radius*2)
print("The area and circumference of circle that has ",radius," of radius is:",area_of_circle," of area and: ",circum_of_circle," of circumference")
#13
user_firstname = input("Write your first name ")
user_lastname = input("Write your last name ")
user_country = input("Write your country of origin ")
user_age = input("Write your age ")
print("Hi, " , user_firstname , user_lastname)
print("You are from , " , user_country)
print("You have, " , user_age , "years of age")
