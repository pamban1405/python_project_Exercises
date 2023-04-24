'''21. You are given a string and width. Your task is to wrap the string into paragraph of width in 
reverse order. Blank spaces should be ignored.
for eg: i/p - first line contains a string with blank spaces - Hello, welcome to this 
organisation.
 the second line conatins the width - 4
 o/p
lleH
ew,o
mocl
tote
osih
nagr
tasi
.noi'''
import textwrap
str=('Hello, welcome to this organisation.').replace(' ','') 
phara=int(input("Enter the Width of the Paragraph: ").strip())
result=''
strlen= len(str)
for i in range(0,strlen):
    strlen=strlen-1
    result=result+str[strlen]
    #strev=result.split()
#print (strev)
print(textwrap.fill(result,phara))
#print(' '.join(i[::-1]  for i in str.split()))

'''for i in str.split():
    i+=i[::-1]

print(i)'''


  



