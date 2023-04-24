#20. You are given a string having alphabets,digits,special characters. Write three different functions 
#to extract the digits[should be in sorted order], special character & vowels[should be in reverse] 
#from the given string.
#i/p string : "abcd123bye09@8#"
#o/p: digits - 012389
#special character - @
#vowels - ea

str1="abcd123bye09@8#"

def digits(str1):
    numbers="0123456789"
    digi=" "
    for i in str1:
        if i in numbers:
            digi=digi+i    
    return digi
           
def spl_char(str1):
    splchar=('/','@','!','#','$','%','^','&','*')
    splseter=" "
    for j in str1:
        if j in splchar:
            splseter+=j   
    return splseter

def vowels_str(str1):
    vols=('a','e','i','o','u')
    volsset=" "
    for k in str1:
        if k in vols:
            volsset=volsset+k
    return volsset
        


digit_output=digits(str1)
print(''.join(sorted(digit_output)))
spl_output=spl_char(str1)
print(''.join(reversed(spl_output)))
vowels_output=vowels_str(str1)
print(''.join(reversed(vowels_output)))
