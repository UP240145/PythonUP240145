num=int(input('Insert the problem number: '))
if num==1:
    grade=int(input('Insert your grade: '))
    if grade>100:
        print("\n","Your grade cant be greater than 100")
    elif grade>=80 and grade<=100:
        print("\n","Yor grade is: A")
    elif grade>=70 and grade<=79:
        print("\n","Yor grade is: B")
    elif grade>=60 and grade<=69:
        print("\n","Yor grade is: C")
    elif grade>=50 and grade<=59:
        print("\n","Yor grade is: D")
    elif grade>=0 and grade<=49:
        print("\n","Yor grade is: F")
elif num==2:
    month=input('Insert the month: ')
    if month=='September' or month=='October' or month=='November':
        print("\n","The season is autumn")
    elif month=='December'or month=='January' or month=='February':
        print("\n","The season is Winter")
    elif month=='March'or month=='April' or month=='May':
        print("\n","The season is Spring")
    elif month=='June' or month=='July' or month=='August':
        print("\n","The season is Summer")
    else:
        print("\n","Error")
elif num==3:
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruit=input('Insert a fruit: ')
    if fruit in fruits:
        print("\n","That fruit already exist in the list",fruits)
    else:
        fruits.append(fruit)
        print("\n","Here is the updated list: ",fruits)