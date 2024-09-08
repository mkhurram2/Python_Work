# Write a program that uses a while loop to print the first 10 even numbers.
Numcount:int = 1
Evencount:int = 0
while Evencount <= 10 -1:
    if Numcount % 2 == 0:
        print(Numcount)
        Evencount += 1
        Numcount += 1
    else:
        Numcount +=1