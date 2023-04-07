#Given a list of first 10 natural numbers, write a program to find the square of all even numbers 
#and cube of all odd numbers and store them in another list

#option 1
nn=[1,2,3,4,5,6,7,8,9,10]
b=len(nn)
result1=[]
result2=[]
for i in nn[1::2]:
    result1.append(i*i)    
print("The squre of the event numbers:", result1)
for j in nn[0::2]:
    result2.append(j*j)
print("The Cube of the odd numbers:", result2)

#option 2

L1=[1,2,3,4,5,6,7,8,9,10]

even_sq,odd_sq = [],[]
print("-------------------------------")
for k in L1:
    (even_sq if k%2==0 else odd_sq).append(k*k)

print("the option2 result ",even_sq,odd_sq)