print("****Calculate your age based on the current year and your birth year****")

def age_calc(curr_year:int,birth_year:int)->int:
    age = curr_year-birth_year
    return age

curr_year = int (input("Current the Year = "))
birth_year = int (input("enter the Birth Year = "))
print("Your age is = ",age_calc(curr_year,birth_year))
