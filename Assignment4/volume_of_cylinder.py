print("****calculates the volume of a cylinder****")
def valOfCyl(r:int,h:int)->float:
    pi=3.14
    v = pi * (r**2) * h
    return v

r = int(input("enter the Radius of cylinder = "))
h = int(input("enter the Height of cylinder = "))


print (f"olume of a cylinder is = {(valOfCyl(r,h)):.2f}")