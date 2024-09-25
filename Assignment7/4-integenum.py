# Write a program that takes a list of integers and prints:
# The first 3 elements
# The last 2 elements
# The entire list in reverse order

integer_numbers = [x for x in range(1,11)]
print(f"Full list of integers: {integer_numbers}")
print(f"The first 3 elements: {integer_numbers[0:3]}")
print(f"The last 2 elements: {integer_numbers[-2::1]}")
print(f"The entire list in reverse order: {integer_numbers[::-1]}")
