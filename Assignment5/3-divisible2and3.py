# Whether it is divisible by both 2 and 3 or anyone of them 
# or not divisible by both check all the cases and print statement for each case.

num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
  print(num, "is divisible by both 2 and 3")
elif num % 2 == 0:
  print(num, "is divisible by 2 but not by 3")
elif num % 3 == 0:
  print(num, "is divisible by 3 but not by 2")
else:
  print(num, "is not divisible by either 2 or 3")
