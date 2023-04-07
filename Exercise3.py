#Given a tuple (“Msys”, “Technologies”, “2007”), add “Python” at the end of this tuple and the 
#output should also be in the form of tuple. Make a note that tuples are immutable in nature so you 
#need to find some idea to make modification and print the updated tuple.

#option 1
exe3_tuple=("Msys", "Technologies", "2007")
#can concatenate a tuple with one element if you want to add an item to it
exe3_append=exe3_tuple + ('python',)
print(exe3_append)
print("------------------------------------")

#option 2

exe3_tuple=("Msys", "Technologies", "2007")
# Python conversion for list and tuple to one another
con_list = list(exe3_tuple)
print(con_list)
print(type(con_list))

# Add items by using insert (), insert has to parameter one is index and value
con_list.insert( 3,'python')
print(con_list)
print(type(con_list))
# Use tuple to convert a list to a tuple ().
con_tuple = tuple(con_list)
print(con_tuple)
print(type(con_tuple))