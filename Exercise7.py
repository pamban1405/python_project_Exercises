#Write a program using dictionary comprehension which will contain the key value pair of i:i**2. 
#Value of ‘i’ will start from 1 and will go upto 10

#Option 1
square_dict = {i: i**2 for i in range(1, 11)}
print(square_dict)


#option 2

for j in range(1,11):
    square={j:j**2}
    print(square)