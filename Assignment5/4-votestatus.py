# - Take the user age.
#  -- If the age is 18 or above:
#  -- Ask if they have a nationality of "Pakistani".
#    ---If yes, print "You are eligible to vote."
#    ---If no, print "Please obtain a valid ID to vote."

UserAge = int(input("Enter a Age: "))

if UserAge >= 18:
    nationalitychk = str(input("please confirm, You have 'Pakistani nationality' (yes/no): "))
    if nationalitychk == 'yes':
        print("You are eligible to vote.")
    elif nationalitychk == 'no':
        print("Please obtain a valid ID to vote.")
    else:
        print("Enter a Invalid Answer")
else:
    print("You are not eligible for vote as Your Age is less then 18")