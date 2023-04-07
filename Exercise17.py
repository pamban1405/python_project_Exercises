#Write a program to replace duplicate adjacent alphabets from given string with ‘_’.
#For Example -- input given string : 'abcdaa hssbbye' and output : ‘abcda_ hs_b_ye’

str_val='abcdaa hssbbye'


'''for i in str_val:

    if i in str_val:
        strarry.append('_')'''
    
'''for i in range(0,len(str_val)): 
    print(i)
    if ord(str_val[i])== i:
        str_val.replace(str_val[i], '_')
print(str_val)'''
    

a = "abcdaa hssbbye"
a1 = ""
for i in range(len(a)):
    if a[i] == a[c]:
        print("inside the if block",a[i])

        a1 = a1 + '_'.join(a[i])
        print(a1)
print(a1) 