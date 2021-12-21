
import os

def printAllStudents(students):

    print("Students with BMI values are...")
    print(students[0])
    
    for i in range(1, len(students)):
        print(students[i])


def printAllOverweight(students):
    
    print("Over weight students are...")
    print(students[0])

    for i in range(1, len(students)):
        if(students[i][4] >= 25.0 and students[i][4] <= 29.9):
            print(students[i])


def printAllHealthy(students):

    print("Healthy students are...")
    print(students[0])
    
    for i in range(1, len(students)):
        if(students[i][4] >= 18.5 and students[i][4] <= 24.9):
            print(students[i])


def updateStudent(roll_number, students, obj):

    # Printing top things
    print(students[0])
    print(obj[0])

    # Getting new height and weights
    new_wight = float(input("Please enter new weight:"))
    new_height = float(input("Please enter new height:"))
    
    # Making object value compatible to strings
    obj[0][2] = str(new_height)
    obj[0][3] = str(new_wight) + "\n"

    # changing the students object value
    for student in students:
        if(student[0] == obj[0][0]):
            student = obj[0]
            break

                    
