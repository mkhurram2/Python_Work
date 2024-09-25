# Given a list of fruits: ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango'], write a program to:
# Access the first, middle, and last element of the list.
# Change the second element to 'blueberry'.

fruitslist = ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'mango']


print(f" First Fruit from list is = {fruitslist[0]} ")

if len(fruitslist) % 2 == 0:
    print(f" Middle Fruit from list is = {fruitslist[len(fruitslist)//2 - 1]} and {fruitslist[len(fruitslist)//2] }")
else:
    print(f" Middle Fruit from list is = {fruitslist[len(fruitslist)//2]} ")

print(f" Last Fruit from list is = {fruitslist[len(fruitslist)-1]} ")






