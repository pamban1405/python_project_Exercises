#9. Write a function which takes input string from the user as argument and the character also taken 
#by the user as the argument and remove all the occurences of that character from the string. Also if 
#the given character is not present in the string your function should raise the exception stating that 
#“Given character is not present in the string. Please try with a new one”


def replacement(str1):
    str3=" "
    for i in range(len(str1)):
        if str1[i]!=str2:
            str3=str3+str1[i]
    return str3
    #print(str3)
        
str1=input("Enter the string: ")
str2=input("Enter the character: ")

Final_value=replacement(str1)
print(Final_value)