def sumtotal(*num)-> int:
    return sum(num)

result = sumtotal(2,2)
print(f"Total Amount of sum is: {result}")


def reg(name: str,password: str,*directors:str, **offices: dict)-> None:
    print(f"{name}, {password}")
    for director in directors:
        print(director)
    for key, value in offices.items():
        print(key,value)
        
#Positional Argument
reg("ABC","123")
#keyword Argument
reg(password="123",name="ABC")
#directors are optional and may skip like in both above
reg("ABC","123", "Khurram", "Ali")
                #(unlimited oprtional argument etc directors like in above khurram and ali)

reg("ABC","123", "Khurram", "Ali",office_name_khi = "khi",office_name_fsd = "fsd", )
                                  #(unlimited keyword argument etc offices like in above khi office and lhr office)