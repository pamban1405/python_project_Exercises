''' Find the palindrome words with the count value from the given string.Output should be in 
form of dict. key will be palidrome word and value will be number of occurence.

i/p given a string - Nittin & his mom went to a park last friday. His Mom observed that the weather
was too cool. Nittin also met his sis. If we reverse the number 1331 then we also get 1331. 
o/p - {'nittin': 2, 'mom': 2, 'sis': 1, '1331': 2}'''

strgivin=('nittin & his mom went to a park last friday. His mom observed that the weather was too cool. nittin also met his sis. If we reverse the number 1331 then we also get 1331 .')
palstr=''
palreverse=''
count=0
for i in strgivin.split():
    #print("the value in the i is",i)
    str2=i[::-1]
    if(i==str2):
        #print('inside if')
        palstr=i
        count=count+1
        dics={palstr,count}
   # print(count)
    #print(palstr)
    print(dics)
