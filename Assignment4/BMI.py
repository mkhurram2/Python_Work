print("****calculates the BMI through Metric Formula****")

def bmi(h:float,w:float)->float:
    bmi = w / (h ** 2)
    return bmi
h = float(input("enter the height (in meters) = "))
w = float(input("enter the weight (in kilograms) = "))

print ("BMI is = ",round(bmi(h,w),2) )