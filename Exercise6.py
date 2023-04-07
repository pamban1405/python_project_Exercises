#Write a program to extract the words starting with lowercase letter present in the list. [‘Nissan’, 
#‘maruti’, ‘hyundai’, ‘Volkswagen’, ‘audi’]

car_list=['Nissan', 'maruti', 'hyundai', 'Volkswagen', 'audi']
print(type(car_list))

for char in car_list:
    if char.islower():
        print(char)


