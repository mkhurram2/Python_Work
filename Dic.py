countries_with_capital = dict(
    pakistan = "Islamabad",
    india = "New Delhi",
    chinan = "Beijing",
    afghanistan = "Kabul",
    iran = "Tehran"

)
print(countries_with_capital)
    
countries_with_capital = dict()
countries_with_capital["pakistan"] = "Islamabad"
countries_with_capital["india"] = "New Delhi"
countries_with_capital["china"] = "Beijing"
countries_with_capital["afghanistan"] = "Kabul"
countries_with_capital["iran"] = "Tehran"

print(countries_with_capital)

new_dic = {    "pakistan" : "Islamabad",
    "india" : "New Delhi",
    "chinan" : "Beijing",
    "afghanistan" : "Kabul",
    "iran" : "Tehran"
    
    }

print(new_dic)


employee_details = {101: 'Ali', 102: 'Ahmed', 103: 'khurram'}
print(employee_details[101])
print(employee_details[102])
print(employee_details[103])
print(employee_details.get(101))

print(employee_details.keys())
print(employee_details.items())

employee_details1 = employee_details.fromkeys([101,102,103])
print(employee_details1)

key = ["name","age","year"]
employee_details2=dict.fromkeys(key,0)
print(employee_details2)
employee_details2["name"]="Khurram"
employee_details2["age"]=44
employee_details2["year"]=2024
employee_details2["phone"]=321866941
employee_details2.update({"name":"Ali"})
employee_details2.update({"name2":"Khurram"})
print(employee_details2)




subjects= {
    "Math": [90,80,95,65],
    "Science" : [95,86,90,60],
    "English" : [96,60,92,70]
}

print(f"Subjects with numbers: {subjects}")

subjects["Math"].append(50)
subjects["Science"].append(75)
subjects["English"].append(60)


employee_details1 = {101: 'Ali', 102: 'Ahmed', 103: 'khurram'}

employee_details2 = employee_details1  # Shallow

employee_details1.update({"101":"Ali2"})
print(employee_details1)
print(employee_details2)

employee_details1 = {101: 'Ali', 102: 'Ahmed', 103: 'khurram'}

employee_details2= employee_details1.copy() # Deep:

employee_details1.update({"101":"Ali2"})
print(employee_details1)
print(employee_details2)