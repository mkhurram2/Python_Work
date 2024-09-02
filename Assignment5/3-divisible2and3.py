# Whether it is divisible by both 2 and 3 or anyone of them 
# or not divisible by both check all the cases and print statement for each case.

startNum = int(input("Enter the start = "))
endNum = int(input("Enter the start = "))

if startNum < endNum :
    for i in range(startNum,endNum+1):
        if i % 2 == 0 and i % 3 == 0:
            print(f" {i} is divisible by both 2 and 3")
        else:
            print(f" {i} is not divisible by both 2 and 3")
else:
    print("Enter Rang is not correct")