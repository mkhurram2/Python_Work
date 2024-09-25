# Write a Python program to create a list of 5 numbers. Add an element to the list, 
# remove one element, and find the maximum and minimum number in the list.

numlist = [10,8,30,25,60]
numlist.append(5)
numlist.pop(0)
numlist.sort()

print(f"Minimum Number from is {numlist[0]}")
print(f"maximum Number from is {numlist[len(numlist)-1]}")