#16. Write a function which will take a string argument and reverse the words in the string. For 
#example – Input string -- “Hello World”. Output should be “olleH dlroW”

def my_function(x):
  #return x[::-1]
    print(' '.join(i[::-1]  for i in x.split()))


mytxt = my_function(input())
