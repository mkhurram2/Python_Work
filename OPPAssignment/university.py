class university:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.teachers = []
        self.students = []
        self.sessions = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def add_session(self, session):
        self.sessions.append(session)

    def __str__(self):
        return f"University: {self.name}\nLocation: {self.location}"

class human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Teacher(human):
    def __init__(self, name, age, gender, subject, experience):
        super().__init__(name, age, gender)
        self.subject = subject
        self.experience = experience

class Student(human):
    def __init__(self, name, age, gender, roll_number):
        super().__init__(name, age, gender)
        self.roll_number = roll_number

class Session:
    def __init__(self, session_name, start_time, end_time, teacher, students):
        self.session_name = session_name
        self.start_time = start_time
        self.end_time = end_time
        self.teacher = teacher
        self.students = students

# Example usage
University = university("Panaversity", "Faisalabad, Pakistan.")

teacher1 = Teacher("Naveed Sarwar", 35, "Male", "Computer Science", 5)
teacher2 = Teacher("Abu Hurairah", 28, "Male", "Computer Science", 3)
University.add_teacher(teacher1)
University.add_teacher(teacher2)

student1 = Student("Muhammad Khurram", 20, "Male", 101)
student2 = Student("Muhammad Hassan", 22, "Male", 102)
student3 = Student("Muhammad Hussain", 23, "Male", 103)
student4 = Student("Ayesha", 21, "Female", 104)
University.add_student(student1)
University.add_student(student2)
University.add_student(student3)
University.add_student(student4)

session1 = Session("Cloud Native Generative, Agentic, and Robotic AI Engineer", "10:00 AM", "01:00 PM", teacher2, [student3, student4])
University.add_session(session1)

session2 = Session("Cloud Native Generative, Agentic, and Robotic AI Engineer", "02:00 PM", "06:00 PM", teacher1, [student1, student2])
University.add_session(session2)


print(University)

print(f"\nTotal Teachers in {University.name}:")
for teacher in University.teachers:
    print(teacher.name)
print(f"\nTotal Students in {University.name}:")
for student in University.students:
    print(student.name)

print("\nSessions:")
for session in University.sessions:
    print(f"\nSession Name: {session.session_name}")
    print(f"Start Time: {session.start_time}")
    print(f"End Time: {session.end_time}")
    print(f"Teacher: {session.teacher.name}")
    print("Students:")
    for student in session.students:
        print(f"- {student.name}")
    

