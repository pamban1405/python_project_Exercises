#. Given two lists --
#list_1 = [‘Msys’, ‘Tata’, ‘Wells’, ‘Mobinius’]
#list_2 = [‘Technologies’, ‘Power’, ‘Fargo’, ‘Technologies’]
#Write a python code using map and lambda function which will create the list named as my_list 
#consisting of the combination of first name and second name from list_1 and list_2 respectively.

list_1 = ['Msys', 'Tata', 'Wells', 'Mobinius']
list_2 = ['Technologies', 'Power', 'Fargo', 'Technologies']
print("The first list",list_1)
print("The second list",list_2)
my_list=(map( lambda x, y: [x , y], list_1, list_2))
print(list(my_list))