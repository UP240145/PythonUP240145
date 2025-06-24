#1
word_1 = 'Thirty'
word_2 = 'Days'
word_3 = 'of'
word_4 = 'Python'
space = ' '
text=word_1+space+word_2+space+word_3+space+word_4
print("\n",text)

#2
word_2_1 = 'Coding'
word_2_2 = 'For'
word_2_3 = 'All'
space = ' '
text_2=word_2_1+space+word_2_2+space+word_2_3
print("\n",text_2)

#3
company="Coding for all"

#4
print("\n",company)

#5
print("\n"," The lenght of the variable is: ",len(company))

#6
print("\n","Here is the variable in upper case: ",company.upper())

#7
print("\n","Here is the variable in lower case: ",company.lower())

#8
print("\n","Here is the text in capital letters: ",company.capitalize())
print("\n","Here is the text in title: ",company.title())
print("\n","Here is the text with swapped cases: ",company.swapcase())

#9
company_cut=company[6:]
print("\n","Here is the text cut: ",company_cut)

#10
n10=company.find('Coding')
if n10 >= 0 :
    print("\n","The variable contains the word Coding")
else:
    print("\n","The variable does not contain the word Coding")

#11
print("\n","Here is the sentence changed: ",company.replace('Coding','Python'),)

#12
nose="Python for everyone"
print("\n","Here is the sentence changed: ",nose.replace('everyone','all'),)

#13
print("\n",company.split(', '))

#14
string_1="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("\n",string_1.split(', '))

#15
first_letter=company[0]
print("\n",first_letter)

#16
last_index=len(company)-1
last_letter=company[last_index]
print("\n",last_letter)

#17
index_10=company[10]
print("\n",index_10)

#18
def crear_acronimo(frase):
    palabras=frase.split()
    acronimo=''.join(palabra[0].upper() for palabra in palabras)
    return acronimo
frase="Python for everyone"
print("\n",crear_acronimo(frase))

#19
frase="Coding for all"
print("\n", crear_acronimo(frase))

#20
index_c=company.index('C')
print("\n", index_c)

#21
index_f=company.index('f')
print("\n", index_f)

#22
lastindex_1=company.rfind('1')
print("\n", last_index)

#23
frase="You cnnot en a sentence with because because because is a conjunction"
index_because=frase.index('because')
print("\n", index_because)

#24
lastindex_because=frase.rindex('because')
print("\n", lastindex_because)

#25
oracion = 'You cannot end a sentence with because because because is a conjunction'
inicio = oracion.find('because because because')
fin = inicio + len('because because because')
phrase = oracion[inicio:fin]
print("\n",phrase)

#28
resultado=company.startswith("Coding")
print("\n", resultado)

#29
resultado=company.endswith("coding")
print("\n", resultado)

#30
texto="   Coding For All      "
texto_limpio=texto.strip()
print("\n", texto_limpio)

#32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined = ' '.join(libraries)
print("\n",joined)

#33
text = "I am enjoying this challenge.\nI just wonder what is next."
print("\n",text)

#34
text = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print("\n",text)

#35
radius = 10
area = 3.14 * radius ** 2
output = "The area of a circle with radius {} is {} meters square.".format(radius, int(area))
print("\n",output)

#36
a = 8
b = 6
print("\n{} + {} = {}".format(a, b, a + b))
print("\n{} - {} = {}".format(a, b, a - b))
print("\n{} * {} = {}".format(a, b, a * b))
print("\n{} / {} = {:.2f}".format(a, b, a / b))
print("\n{} % {} = {}".format(a, b, a % b))
print("\n{} // {} = {}".format(a, b, a // b))
print("\n{} ** {} = {}".format(a, b, a ** b))