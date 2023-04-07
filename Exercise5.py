#Given a dictionary {‘Msys Technologies’:’Sanjay Sehgal’, ‘Infosys’:’Salil Parekh’, 
#‘TCS’:’Rajesh Gopinathan’, ‘Wipro’:’Thierry Delaporte’} make a list of all the values associated 
# with keys in alphabetically sorted order.

#option1
'''owner_dic= {'Msys Technologies':'Sanjay Sehgal', 'Infosys':'Salil Parekh','TCS':'Rajesh Gopinathan', 'Wipro':'Thierry Delaporte'}
sortedic=sorted(owner_dic)
print(sortedic)'''


#option 2
myDict = owner_dic= {'Msys Technologies':'Sanjay Sehgal', 'Infosys':'Salil Parekh','TCS':'Rajesh Gopinathan', 'Wipro':'Thierry Delaporte'}
 
myKeys = list(myDict.keys())
myKeys.sort()
print(myKeys)
#sorted_dict=()
for i in myKeys:
    sorted_dict={i:myDict[i]}
    print(sorted_dict)
#sorted_dict = {i: myDict[i] for i in myKeys}
 
#print(sorted_dict)