#Write a python function with name reverse_vowel that takes one string as an argument and 
#reverse the order of vowels present in the string. The function should return the string having 
#reversed order of vowels. For example – If the input string which is given as argument is ‘Hello’ 
#then the output string should be ‘Holle’. You need to reverse the vowel irrespective of lowercase or 
#uppercase.


def reverse_vowel(strval):
    chars = list(strval)
    index = []
    vowels = []
    for i in range(len(chars)):
        if chars[i] in ['a','e','i','o','u']:
            vowels.append(chars[i])
            print ("The vowels values",vowels)       
        index.append(i)
        print("the index values",index)
    vowels = vowels[::-1]
    print("the values in the vowels is:",vowels)
   
    final = []  
    ind = 0
    for i in range(len(chars)):
        if i in index:
            final.append(vowels[ind])
            ind += 1 
        else:
             final.append(chars[i])
    str1 = ""
    return str1.join(final)

strval="bala"
print(reverse_vowel(strval))

