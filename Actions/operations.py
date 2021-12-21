
def calculateBMIAll(datalist):
    
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
            bmi = calculateBMI(line[2], line[3])
            line.append(bmi)

        students.append(line)
    
    return students

def calculateBMI(height, weight):

    height = (float(height)/100)
    weight = float(weight)
    bmi = (weight / (height * height))

    return bmi

def getOperationNumber():
    try:
        return int(input("Enter operation:\n1) Get all student's bmi \n2) Get all overweight students \n3) Get all healthy students \n4) Update details \nYour Input:"))
    
    except:
        return 'q'