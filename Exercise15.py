#. Given a list --list_1 = [10, 12, 15, 67, 95, 45, 43, 89, 91, 80, 75, 78, 94, 100]
#use the filter() function to find the list of numbers that are multiple of either 2 or 5.

def is_multiple_of_3(num):
    return num % 2 == 0

def is_multiple_of_5(num):
    return num % 5 == 0

list_1 = [10, 12, 15, 67, 95, 45, 43, 89, 91, 80, 75, 78, 94, 100]

result = list(filter(lambda x : is_multiple_of_3(x), list_1))

result2 = list(filter(lambda y : is_multiple_of_5(y), list_1))

print(result,result2)