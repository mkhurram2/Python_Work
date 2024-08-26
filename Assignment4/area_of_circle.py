print("****Calculates the area of the cube****")
def areaOfCircle (rad)->float:
    pi=3.14
    AreaOfCircle = pi*rad**2
    return AreaOfCircle

rad = int(input(" Enter the Radius of Circle = "))

print ("Area of Circle is = ", round(areaOfCircle(rad),2))