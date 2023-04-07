#Take the input marks from user using input() function and find out the grade of the students. Note
#the grading will be in this manner – (100 – 91) – A1, (90-81) – A2, (80-71) – B1, (70-61) – B2, (60-
#51) – C1 (50-40) – C2 and less than 40 students will ‘Fail’. Also make sure user should input the 
#marks in the range 0<=marks<=100, if user will input some other marks in should print invalid 
#marks

Marks=int(input('Enter the mark of the student: '))

if (Marks>=91 and Marks<=100):
    print("Studnet grade is: A1")
elif (Marks>=81 and Marks<=90):
    print("Studnet grade is: A2")
elif (Marks>=71 and Marks<=80):
    print("Studnet grade is: B1")
elif (Marks>=61 and Marks<=70):
    print("Studnet grade is: B2")
elif (Marks>=51 and Marks<=60):
    print("Studnet grade is: C1")
elif (Marks>=40 and Marks<=50):
    print("Studnet grade is: C2")
else:
    print("Fail")