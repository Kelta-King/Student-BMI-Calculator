import os
from Actions import operations as op

def main():
    
    # Getting data from csv file
    dirname = os.path.dirname(__file__)

    filename = os.path.join(dirname, 'DataHolders/students_sample.csv')
    # Getting data from csv file
    f = open(filename, "r")

    # It has all the records in each list
    datalist = f.readlines()

    # Objest for storing the students records
    students = []

    # Looping to copy data in students with BMI value
    i = 0
    for line in datalist:

        line = line.split(",")
        # For handling the first entry of list
        if(i == 0):
            i += 1
            line.append("BMI")

        else:
            # Here in csv, the height in cm. So, convert it to meter
            bmi = op.calculateBMI(line[2], line[3])
            line.append(bmi)

        students.append(line)

    # Now we have students object ready with BMI values
    # Iteration to perform the tasks
    while True:

        # Getting the task number
        x = op.getOperationNumber()

        # Printing the bmi values of all students
        if(x == 1):
            pass

        # Getting all overweight students
        elif(x == 2):
            pass

        # Getting all healthy students
        elif(x == 3):
            pass
            
        # Updating the height and weight of student
        elif(x == 4):
            pass

        else:
            if(input("Incorrect input given. Press 'q' to quit:") == "q"):
                break

    f.close()
    

if __name__=="__main__":
    main()