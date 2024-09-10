# 5. *Create a function* that takes a positive integer as a parameter 
# and uses a while loop to calculate and return the factorial of that number.
 

def factorial (num):
    count:int = 1
    result:int = 1
    while count <= num:
        result = result * count
        count += 1
    return result

num = int(input("enter a number for take a factorial"))
print(f"The Factorial is = {factorial (num)}")

