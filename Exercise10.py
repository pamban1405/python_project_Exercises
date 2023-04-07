#In the given String -- ‘MsYs TecHNOlogiEs iS a gREat place To woRk’ find the count of 
#lowercase and uppercase letters.

Str_value='MsYs TecHNOlogiEs iS a gREat place To woRk'
strcount=len(Str_value)
print("Total number of the char in the string:",strcount)
lower=0
upper=0
for i in Str_value:
      if(i.islower()):
            lower+=1
            
      else:
            upper+=1
          
print("The number of lowercase characters is:",lower)
print("The number of uppercase characters is:",upper)