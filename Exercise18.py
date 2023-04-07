'''Print the below rohmbus pattern according to the given number
for eg: given number is 4 then 
o/p will be 
 1
 212
32123
4321234
32123 
 212 
 1'''

'''for i in range (1,8):
    #print("the value of i",i)
    for j in range(i):
     #print('The value in the j ' ,j)
        print(" ", i ," ",end='')
    print('')'''

num=int(input("Enter the number of the rows"))

for i in range (0,num+1):
    for j in range (1,num-i+1):
        print(end=" ")
    for j in range (i,0,-1):
        print(j,end="")
    for j in range (2,i+1):
        print(j,end="")
    print()
for i in range(num-1,0,-1):
    #print(i)
    for j in range(num-i,0,-1):
        print(end=" ")
    for j in range (i,0,-1):
        print(j,end="")
    for j in range (2,i+1):
        print(j,end="")
    
    print("")