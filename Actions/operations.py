
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