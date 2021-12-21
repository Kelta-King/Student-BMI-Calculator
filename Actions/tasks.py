
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