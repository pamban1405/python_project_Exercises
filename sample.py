num=int(input("enter the number of rows : "))


for i in range (0,num+1):
    for j in range (1,num-i+1):
        print(end=" ")
    for j in range (i,0,-1):
        print("*",end="")
    for j in range (2,i+1):
        print("*",end="")
    print()
for i in range(num-1,0,-1):
    for j in range(num-i,0,-1):
        print(end=" ")
    for j in range (i,0,-1):
        print("*",end="")
    for j in range (2,i+1):
        print("*",end="")
    
    print("")

