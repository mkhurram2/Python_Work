# 1. *Create a function* that takes an array, an index, and a value as parameters. 
# Inside the function, use the insert method to insert the value at the specified index in the array. 
# Return the modified array.
def insert_value_at_index(arr, index, value):
  arr.insert(index, value)
  return arr

userlist = ['Ali','Ahmed', 'Kamran']
print(f"without change of list = {userlist}")
print(f"Modified list = {insert_value_at_index(userlist,2,'khurram')}")