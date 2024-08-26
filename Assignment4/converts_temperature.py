print("****converts a temperature from Fahrenheit to Celsius****")

def fToc(f:float)->float:
    c= (f - 32) * 5/9
    return c
def cTof(c:float)->float:
    f= (9/5) *  c + 32
    return f

f = float(input("enter a fahrenheit = "))
outputfToc:str = f"output: {f} °F (Fahrenheit) = {round(fToc(f),2)} °C (Celsius )"
print(outputfToc)
#print("Output: ",f,"°F (Fahrenheit) =",round(fToc(f),2),"°C (Celsius )")

print("****converts a temperature from Celsius to Fahrenheit****")

c = float(input("enter a Celsius = "))
outputcTof = f"Output: {c} °C (Celsius) = {round(cTof(c),2) } °F (Fahrenheit)"
print(outputcTof)
#print("Output: ",c,"°C (Celsius) =",round(cTof(c),2),"°F (Fahrenheit)")