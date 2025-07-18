fruits=('mango','manzana','piña')
vegetables=('tomate','pepino','jicama')
animal_products=('sausage','beef','bacon')
food_stuff_tp=fruits+vegetables+animal_products
food_stuff_ls=list(food_stuff_tp)
lenght=len(food_stuff_ls)//2
food_stuff_ls=food_stuff_tp[:lenght]+food_stuff_tp[lenght+1:]
print("\n","Here is the tuple whitout the midle item: ",food_stuff_ls)
food_stuff_ls=food_stuff_tp[3:]
print("\n","Here is the tuple whitout the first three items: ",food_stuff_ls)
food_stuff_ls=food_stuff_tp[:-3]
print("\n","Here is the tuple whitout the last three items: ",food_stuff_ls)
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("\n","Is Estonia a nordic country? ",'Estonia' in nordic_countries)
print("\n","Is Iceland a nordic country? ",'Iceland' in nordic_countries)