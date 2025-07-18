#1
lista_1=list()
print("\n",lista_1)

#2
lista_1=['1','2','3','4','5']
primer_item, segundo_item, tercer_item, cuarti_item, quinto_item,*rest=lista_1
print("\n","Numeros: ",lista_1)

#3
print("\n","Cantidad de numeros: ",len(lista_1))

#4
print("\n"," Primer item: ",primer_item," Item central: ",tercer_item," Ultimo item: ",quinto_item)

#5
mixed_data_types=list()
mixed_data_types=['Adrian','18','1.7','Soltero','Aguascalientes mx']
print("\n",mixed_data_types)

it_companies=list()#6
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print("\n",it_companies)#7
print("\n","The number of companies in the list is: ",len(it_companies))#8
print("\n","First company: ",it_companies[1]," Midle company: ",it_companies[3]," Last company: ",it_companies[-1])#9
it_companies[0]='Walmart'#10
it_companies[4]='Burger king'
print("\n","Here is the modified list:",it_companies)
it_companies.append('Jugos tony')#11
print("\n","Here is the list with one extra company: ",it_companies)
it_companies.insert(3, 'Tesla')#12
print("\n","Here is the list after inserting another company: ",it_companies)
it_companies[2]=it_companies[2].upper()#13
print("\n","Here is the list with item 3 changed to uppercase: ",it_companies)
print("\n","Here are the two lists joined: ",it_companies+lista_1)#14
print("\n","Here are the two lists together: ",it_companies)
does_exist_1='Burger king' in it_companies#15
does_exist_2='HEB' in it_companies
print("\n","Does Burger king exists in the list? ",does_exist_1," Does HEB exists in the list? ",does_exist_2)
it_companies.sort()#16
print("\n","Here is the list sorted: ",it_companies)
it_companies.reverse()#17
print("\n","Here is the list reversed: ",it_companies)
it_companies_nof3=it_companies[3:]#18
print("\n","Here is the list without thr first 3 companies: ",it_companies_nof3)
it_companies_nol3=it_companies[:-3]#19
print("\n","Here is the list without the last 3 companies: ",it_companies_nol3)
it_companies_nomid1=it_companies[:1]#20
it_companies_nomid2=it_companies[4:]
print("\n","Here is the list without the midle items: ",it_companies_nomid1+it_companies_nomid2)
it_companies.remove('Walmart')#21
print("\n","Here is the list whitout the first company: ",it_companies)
it_companies.remove('Google')#22
print("\n","Here is the list without the middle company: ",it_companies)
it_companies.remove('Amazon')#23
print("\n","Here is the list without the last company: ",it_companies)
it_companies.remove('Tesla')#24
it_companies.remove('Oracle')
it_companies.remove('MICROSOFT')
it_companies.remove('Apple')
print("\n","Here is the list without the last company: ",it_companies)
del it_companies#25
print("\n",it_companies)
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']#26
back_end = ['Node','Express', 'MongoDB']
joined_lists=front_end+back_end
print("\n","Here are the two lists joined: ",joined_lists)
full_stack = joined_lists.copy()#27
index = full_stack.index('Redux')
full_stack.insert(index + 1, 'Python')
full_stack.insert(index + 2, 'SQL')
print("\n","Here is the list: ",full_stack)