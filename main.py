import os
from Actions import operations as op
from Actions import tasks as ts

def main():
    
    # Getting data from csv file
    dirname = os.path.dirname(__file__)

    filename = os.path.join(dirname, 'DataHolders/students_sample.csv')
    # Getting data from csv file
    f = open(filename, "r")

    # It has all the records in each list
    datalist = f.readlines()

    # Objest for storing the students records
    students = op.calculateBMIAll(datalist)

    # Now we have students object ready with BMI values
    # Iteration to perform the tasks
    while True:

        # Getting the task number
        x = op.getOperationNumber()

        # Printing the bmi values of all students
        if(x == 1):
            ts.printAllStudents(students)

        # Getting all overweight students
        elif(x == 2):
            ts.printAllOverweight(students)

        # Getting all healthy students
        elif(x == 3):
            ts.printAllHealthy(students)
            
        # Updating the height and weight of student
        elif(x == 4):
            # Editing will be done on the basis of roll numbers
            try:

                # Getting roll number
                num = input("Enter the roll number:")

                # Getting the student with roll number
                obj = [student for student in students if student[0] == num]

                # If more than one student exist with same roll number then we will raise exception
                if(len(obj) == 1):
                    ts.updateStudent(num, students, obj)
                    
                    dirname = os.path.dirname(__file__)

                    # Cleaning file first
                    open(filename, 'w').close()

                    # Opening for writing
                    file1 = open(filename, 'a')

                    # Writing in the file
                    for student in students:
                        str = student[0]+", "+student[1]+", "+student[2]+", "+student[3]           
                        file1.write(str)

                    # Closing the file
                    file1.close()

                elif(len(obj) == 0):
                    print("Incorrect roll number")
                else:
                    print("Sorry, more than one student with same roll number")
                

            except:
                print("something went wrong. Let's try again...")

        else:
            if(input("Incorrect input given. Press 'q' to quit:") == "q"):
                break

    f.close()
    

if __name__=="__main__":
    main()