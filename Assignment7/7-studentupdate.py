# Write a program to update the 'grade' value to 'A', and add 
# a new key-value pair for 'major' with the value 'Computer Science'.

student = {'name': 'John', 'age': 22, 'grade': 'B'}
print(f"Student Information: {student}")
student.update({"grade":"A", "major":"Computer Science"})
print(f"Updated Student Information: {student}")
