print("****converts a temperature from Fahrenheit to Celsius****")
f = float(input("enter a fahrenheit = "))
c= (f - 32) * 5/9
print("Output: ",f,"°F (Fahrenheit) =",round(c,2),"°C (Celsius )")

print("****converts a temperature from Celsius to Fahrenheit****")
c = float(input("enter a Celsius = "))
f= (9/5) *  c + 32
print("Output: ",c,"°C (Celsius ) =",round(f,2),"°F (Fahrenheit)")