print("****Calculates the area of the cube****")
def areaOfCube(len_cube:int)->int:
    Area  = 6 * len_cube ** 2
    return Area

len_cube = int(input("enter the length of one side of the cube = "))

print ("Surface Area of cube is = ",areaOfCube(len_cube) ) 