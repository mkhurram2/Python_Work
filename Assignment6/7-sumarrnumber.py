# *Create a function* that takes an array of numbers as a parameter. 
# Use a while loop to calculate and return the sum of all the numbers in the array.

def sumofarr (list):
    sum:int = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum

list: int = [1,5,9,6]
print(f"The sum of list = {sumofarr(list)}")