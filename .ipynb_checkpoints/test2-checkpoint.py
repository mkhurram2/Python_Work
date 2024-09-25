#num1=int(input("enter a number which table is required: "))
#for i in range(1,11):
#    print(f"{num1} * {i} = {i * num1}")

#studlist: list[str] = ['ali','Kamran','Ahmed']

print(f"I pakistan ")

print("I love \n \"pakistan\"")

stname = "M Khurram"
fname = "M Afzal"
age: int = 44
edu = "BCS"

print(f"I pakistan @ {age} ")

card: str = f"""
Statudent Card:
Statudent Name: %s
F Name: %s
age: %d
Education: %s

"""% (stname, fname, age, edu)

print(card)

card: str = """
Statudent Card:
Statudent Name: {0}
F Name: {1}
age: {3}
Education: {2}

""".format (stname, fname , edu , age) # We can not change the default sequence otherwise get wrong value position 
#           1       2       4       3
print(card)

card: str = """
Statudent Card:
Statudent Name: {a}
F Name: {b}
age: {d}
Education: {c}

""".format (a=stname, b=fname , c=edu , d=age) # We can not change the default sequence otherwise get wrong value position 

print(card)

name:str="     'muhammad       khurram'        "
print(name.lstrip())
print(name.rstrip())
name:str="     'muhammad       khurram'        "
print(name.strip())

import re
name:str="     'muhammad       khurram'        "
name1:str = re.sub(' {2,100}',' ', name).strip()
print(name1)

#!pip install    pandas
#import pandas as pd

#table = pd.read_html('https://www.w3schools.com/python/python_operators.asp')
#table(0)


x = b"Hello"    # bytes
print(x)
x = bytearray(5)    # bytearray
print(x)
x = memoryview(bytes(5))        # memoryview
print(x)

chk=chr(65)
print(chk)

code=ord('A')
print(code)         # out is 65

chrlist: list[str] =["a","b","c","d","f"]
print(chrlist[-4::2])

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])

print(thislist[2:])
print(thislist[-4:-1])

thislist1 = ["apple", "banana", "cherry"]
thislist1[1:2] = ["blackcurrant", "watermelon"]
print(thislist1)

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]