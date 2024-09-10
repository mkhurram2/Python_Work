# Implement a program that takes a list of temperatures in Celsius as input from the user. 
# Convert each temperature to Fahrenheit using the formula F = (C * 9/5) + 32 and 
# store the converted temperatures in an array. Use a while loop to perform the conversion for each temperature.

clist=[]
flist=[]
count: int = 0
for i in range(2):
    clist.insert (i,int(input(f"{i+1}-Enter temperatures in Celsius =")))

while count <= len(clist)-1:
    flist.insert (count, ((clist[count] * 9/5) + 32))
    count += 1
print(f"Celsius = {clist}")
print(f"Fahrenheit = {flist}")
