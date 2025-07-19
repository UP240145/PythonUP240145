n=int(input('Enter your age: '))
if n<18:
    x=18-n
    print("\n","You need ",x," more years to learn to drive")
else:
    print("\n","You are old enough to learn how to drive")
age=int(input('Enter your age: '))
my_age=18
if age>my_age+1:
    x=age-my_age
    print("\n","You are ",x," years older than me")
elif age>my_age and age==my_age+1:
    x=age-my_age
    print("\n","You are ",x," year older tan me")
elif age<my_age and age+1==my_age:
    x=my_age-age
    print("\n","You are ",x," year younger than me")
elif age==my_age:
    print("\n","We are the same age")
else:
    x=my_age-age
    print("\n","You are ",x," years younger than me")
a=int(input('Insert the first number:'))
b=int(input('Insert the second number:'))
if a<b:
    print("\n","a is smaller than b")
elif b<a:
    print("\n","a is greater than b")
else:
    print("\n","a is equal to b")