
#Write a program to reverse a number without using any inbuit function
a = input("enter the value of the reverse: ")
result=''
b= len(a)
for i in range(0,b):
    b=b-1
    result=result+a[b]
print(result)

#Extended sliceing 

"""strr="helloworld"
print(strr[-1::-1])"""


