dog = {'name':'Chucho', 'color':'White', 'breed':'French puddle', 'legs':4, 'age':2}#1 y 2
student = {
    'first_name':'ADRIAN',
    'last_name':'Lezama',
    'gender':'Male',
    'age':25,
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'country':'Mexico',
    'city':'Aguascalientes',
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}#3
print("\n","Here is the leght of the student dictionery: ",len(student))#4
skills=student['skills']#5
print("\n","Here are the skills of the student: ",skills)
print("\n","Here is the data type: ",type(skills))
student['skills'].append('HTML')#6
student['skills'].append('Xamarin')
print("\n","Here are the updated skills of the student: ",student['skills'])
print("\n","Here are the dictionary keys as a list: ",student.keys())#7
print("\n","Here are the dictionary values as a list: ",student.values())#8
print("\n","Here is the dictionary as a list of tuples: ",student.items())#9
del student['age']#10
print("\n","Here is the dictionary with one of the items deleted: ",student)
del dog#11