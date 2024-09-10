# Write a program to remove all the odd numbers from an array.

def removeodd(list):
    for i in range(len(list)):
        for ii in range(len(list)):
            if list[ii] % 2 != 0:
                list.pop(ii)
                i = 0
                break
    return list

list:int =[]
for i in range(1,21):
    list.insert(i,i)

print(f"List of numbers = {list}")
print(f"list After remove of odd numbers = {removeodd(list)}")
