num1= 2
num2 =3
if num1 == num2:
    print ("both numbers are equal")
elif num1>num2:
    print (f"{num1} is greater than {num2}")
else:
    print (f"{num2} is greater than {num1}")
print("Good Morning!")

for i in range(4):
    print(f"I am {i}")

for i in range(1,5):
    print(f"I I am {i}")

num3=int(input("enter a numer"))
total =0
for i in range(0,num3+1):
    total += i
    print(total)
print(total)

num4=0
while num4 <=5:
    print(f"num4 {num4}")
    num4 += 1

endnum = int(input("Enter number"))
num4=0
while num4 <=endnum:
    print(f"num4 {num4}")
    num4 += 1
