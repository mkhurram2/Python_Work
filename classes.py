class person:
    name = "" 
    age = 0
    def run(self):
        print("Running")
        print("tried")

person1 = person()
person1.name = "Muhammad Khurram"
person1.age = 45
print(person1.name)
print(person1.age)
person1.run()

person2 = person()
person2.name = "Muhammad Hassan"
person2.age = 12

print(person2.name)
print(person2.age)
person2.run()

class Persontop:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Persontop("John", 36)

print(p1.name)
print(p1.age) 


class car:
    def __init__(self,brand,engine):
        self.brand = brand
        self.engine = engine
    def start_engine(self):
       print(f"{self.brand} car starting")
       print(f"{self.brand} car started")

car1= car("BMW",2500)
print(car1.brand)
car1.start_engine()


class car:
    def __init__(self,brand,engine):
        self._brand = brand
        self.engine = engine
    def start_engine(self):
       print(f"{self._brand} car starting")
       print(f"{self._brand} car started")
    def get_brand(self):
       return self._brand

car1= car("BMW",2500)
print(car1.get_brand)
car1.start_engine()

class human:
   def __init__(self,name,age):
      self.name = name 
      self.age = age

human1 = human("khurram",44)
print(human1.name)
print(human1.age)

class student(human):
   def  __init__(self, name,age, roll_n0,class_name,section):
      super().__init__(name,age)
      self.roll_no = roll_n0
      self.class_name = class_name
      self.section = section

student_class = student("Ali",24,202,"BCS",2024)

print(student_class.name)


class student(human):
   def  __init__(self, name,age, roll_n0,class_name,section):
      human.__init__(self,name,age)
      self.roll_no = roll_n0
      self.class_name = class_name
      self.section = section

student_class = student("Ali",24,202,"BCS",2024)

print(student_class.name)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age) 


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)

class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def myfunc(self):
    print("hello my name is "+self.name)
p1=person("john",36)
p1.myfunc()

class person:
  def __init__(me,name,age):
    me.name=name
    me.age=age
  def myfunc(me2):
    print("hello my name is "+me2.name)
p1=person("john",36)
p1.myfunc()


#Inheritance Class Polymorphism

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()


class person1:
    def __init__(self,name="Khurram",age=44):
      self.__name = name
      self.__age =  age
    
    def persondata(self):
        print(f"The name of the person is = {self.__name} and age is {self.__age}")
      

personadd = person1()
personadd.__name = "Muhammad Khurram"
personadd.__age = 45
print(personadd.__name)
print(personadd.__age)
personadd.persondata()

