#Given a list [1,2,1,5,9,10,2,2,7,5,3,10,8,9,15,17,21,16,17,90] find the difference between the 
#length of the list and the count of unique elements in the list

list_val=[1,2,1,5,9,10,2,2,7,5,3,10,8,9,15,17,21,16,17,90]

len_list=len(list_val)
print("The length of the string is: ",len_list)

list_item=[]
count=0

for i in list_val:
    if i not in list_item:
        count+=1
        list_item.append(i)
print("No of unique items are:", count)

