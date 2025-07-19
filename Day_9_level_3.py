person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
    skills = person['skills']
    midle = skills[len(skills)//2]
    print("\n","Here is the midle skill in the skills list: ",midle)
    if 'Python' in skills:
        print("\n","The person has python as a skill? ",'Python' in skills)
    else:
        print("\n","He does not have Python as a skill.")
    if sorted(skills) == sorted(['JavaScript','React']):
        print("\n","He is a front end developer")
    else:
        print("\n","He does not only has those two skills")
    if 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        print("\n","He is a backend developer")
    else:
        print("\n","He is not a backend developer")
    if 'React' in skills and 'Node' and 'MongoDB' in skills:
        print("\n","He is a fullstack developer")
    else:
        print("\n","unknown title")
    is_married=person['is_marred']
    space=' '
    name=person['first_name']+space+person['last_name']
    country=person['country']
    if is_married==True and country=='Finland':
        print("\n",name,"Lives in",country,"He is married")