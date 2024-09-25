# Write a Python program that removes all duplicates from a given list and prints the new list without duplicates.

list =[2,5,7,8,2,10,2,7,9,5]
print(f" Given List: {list}")
list.sort()

x=0
while x < len(list)-1:
    if list[x]==list[x+1]:
        list.remove(list[x])
        x=x-1
    else:
        x=x+1
        
print(f" List after remove duplicate: {list}")