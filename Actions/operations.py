
def calculateBMI(height, weight):

    height = (float(height)/100)
    weight = float(weight)
    bmi = (weight / (height * height))

    return bmi