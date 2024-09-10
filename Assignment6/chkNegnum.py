# *Write a program* that has an array of numbers; if the number is negative, 
# it should remove the negative number from the array.

list: int = [1,5,-9,-6,3]

print(f"before removal of Nagitive Number = {list}")

for i in range(len(list)):
    for ii in range(len(list)):
        if list[ii] < 0 :
            list.pop(ii)
            i=0
            break
        
print(f"After removal of Nagitive Number = {list}")
