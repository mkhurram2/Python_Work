# Implement a simple shopping cart program using an array. 
# Create functions to add items, remove items, and update quantities using array methods. 
# Print the cart's contents after each operation.

def add_item(cart, item, quantity):
  cart.append([item, quantity])
  print(f"Added {quantity} {item}(s) to the cart.")  # print addition item with its qanatity
  print_cart(cart)  # print funcation call for card item print

def remove_item(cart, item):
  if cart==[]:
    print("list is already empty, unable to remove")
  else:
      for count in range(len(cart)):        
        if cart[count][0] == item:
          print(f"Removed {cart[count][1]} {cart[count][0]}(s) from the cart.")
          cart.pop([count][0])
          print_cart(cart)
          break
        else:
          if count == len(cart)-1:
            print("Item not Found")
          
def update_quantity(cart, item, new_quantity):
  for i in range(len(cart)):
    if cart[i][0] == item:
      old_quantity = cart[i][1]
      cart[i][1] = new_quantity
      print(f"Updated {item} quantity from {old_quantity} to {new_quantity}.")
      print_cart(cart)
      return
  print(f"{item} not found in the cart.")
  
def print_cart(cart):
  if not cart:
    print("Your cart is empty.")
  else:
    print("Your cart contains:")
    for item in cart:
      print(f"-> {item[1]} {item[0]}(s)")

# calling
shopping_cart = []
add_item(shopping_cart, "Apple", 5)
add_item(shopping_cart, "Banana", 3)
remove_item(shopping_cart, "Apple")
update_quantity(shopping_cart, "Banana", 5)