print("****Calculation of the area of a rectangle****")

def areaOfRectangle(len_rect:int, wid_rect:int)->int:
    Area = len_rect * wid_rect
    return Area
len_rect = int(input("enter the length of Rectangle = "))
wid_rect = int(input("enter the width of Rectangle = "))

print ("Area of rectagle is = ",areaOfRectangle(len_rect, wid_rect) )