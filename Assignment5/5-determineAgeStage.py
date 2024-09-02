# Write a program that takes the age of a person as input 
# and determines whether they are a child (0-12 years), teenager (13-19 years), adult (20-59 years), 
# or senior citizen (60 years and above)

age = int(input("Enter a Age of Person: "))
if age >=1 and age <=12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20 and age <= 59:
    print("Adult")
elif age >= 60 and age <= 125:
    print("Senior Citizen")
else:
    print("Entered Invalid Age")