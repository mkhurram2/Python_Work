print("****Calculates the percentage****")

def perctage(n:int,d:int)->float:
    per = n / d * 100
    return per
n=int(input("enter the obtain number (Numerator) = "))
d=int(input("enter the total number (Denominator) = "))

print("The percentage is = per",round(perctage(n,d),2),"%")