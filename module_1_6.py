my_dict = {'Adrian': 1993, 'Brian': 1994, 'Carl': 1995}
print  ("Dict:",my_dict,
        '\n'"Existing value:", my_dict.get('Carl'),
        '\n' "Not existing value:", my_dict.get ("Anna"))
del my_dict['Brian']
print ("Deleted value: 1994")
my_dict.update({'Anna': 1996,
               'Scott': 1997})
print ("Modified dictionary:", my_dict)


my_set = {1,2,3,1,2,3, "iphone", (1,2,3)}
print ("Set:", my_set)
my_set.add(3.14),(True)
my_set.remove(1)
print ("Modified set:", my_set)
