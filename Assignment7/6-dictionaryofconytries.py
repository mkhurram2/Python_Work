# - Create a dictionary where the keys are the names of 5 different countries and 
# the values are their capitals. Write a program to display all the countries and their capitals.
countries_with_capital = dict(
    Pakistan = "Islamabad",
    India = "New Delhi",
    China = "Beijing",
    Afghanistan = "Kabul",
    Iran = "Tehran"
)

for x, y in countries_with_capital.items():
    print(f"{y} is the capital of {x}")
    

