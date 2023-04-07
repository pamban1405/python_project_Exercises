#. In the dictionary {‘India’:’New Delhi’, ‘USA’:’Washington D.C.’, ‘Nepal’:’Kathmandu’} list out 
#all the keys in a list named as ‘list_keys’ and list out all the values in a list named as ‘list_values’. 
#Also find out the value of key ‘Australia’ in the list and as it is not existing in the list print ‘NA’ as 
#its value.

country_captial={'India':'New Delhi', 'USA':'Washington D.C.', 'Nepal':'Kathmandu'}
print(country_captial)
list_keys=list(country_captial.keys())
print(list_keys)
print(type(list_keys))

list_values=list(country_captial.values())
print(list_values)
print(type(list_values))

if list_keys=='Australia':
    print ("key austraila present in the key list")
else:
    print("NA")

