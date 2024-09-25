# - Write a program that takes a list of student names as input, sorts the names in alphabetical order, 
# and prints the sorted list.


num_of_students = int(input("Enter the number of students: "))
student_names = []

for i in range(num_of_students):
    student_names.append(input(f"Enter the name of student {i + 1}: "))

student_names.sort()
print(student_names)
