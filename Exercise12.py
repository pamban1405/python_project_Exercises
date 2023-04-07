#Write a method number_of_prime_numbers() which takes two input arguments num1 and 
#num2 and should return the total number of prime numbers in the range. The numbers num1 and 
#num2 are inclusive of the range. Also add all the numbers in an empty list and return the sum of the
#list. So finally your function will return two things, first will be the count of prime numbers and the 
#other will be the sum of all the prime numbers in the given range
#upto = int(input("Find prime numbers upto : "))

def number_of_prime_number(num1,num2):
    if(num1==1 or num1==0):
        return False
    for i in range(num1, num2):
        if(num2 % i == 0):
            
            print("the number is the prime number",i)
           # num2=num2-1
        else:
           print ("number is not a prime number",i)

num1,num2=2,12
print(number_of_prime_number(2,10))
'''N = 100;

#check for every number from 1 to N
for i in range(num1,num2+1):
  #check if current number is prime
  if(number_of_prime_number(i)):
    print(i,end=" ")'''

