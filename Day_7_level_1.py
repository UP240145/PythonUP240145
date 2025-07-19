# set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("\n","Here is the lenght of the set: ",len(it_companies))#1
it_companies.add('Twitter')#2
print("\n","Here is set after adding the request: ",it_companies)
it_companies.update(['Youtube','Tiktok'])#3
print("\n","Here is the list updated with more it companies: ",it_companies)
it_companies.remove('Facebook')#4
print("\n","Here is the list after removing an item: ",it_companies)
print("\n","Te diference between remove and discard is that if the item is not found in the set remove will return an error and  discard wont.")#5