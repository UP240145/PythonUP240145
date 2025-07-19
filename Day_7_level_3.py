age = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(age)
if len(age)<len(ages_set):
    print("\n","The set is larger than the list.")
elif len(age)>len(ages_set):
    print("\n","The list is larger than the set.")
else:
    print("\n","The list and the set have the same size.")
print("\n","The diference between those data types is that string is onli used if you are working with text, list is if you want an ordenated and changeable group of data, tuple is if you want an immutable group of data and set is if you dont want the data to be ordenated and does not suport duplicates")
sentence = "I am a teacher and I love to inspire and teach people."
sentence = sentence.replace(".","")
words = sentence.split()
unique_words = set(words)
num_unique = len(unique_words)
print("\n","Here are the unique words in the text: ",unique_words," You used a total of: ",num_unique," words in the sentence")