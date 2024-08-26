print("****Convert a given number of seconds into minutes and seconds****")

def time_conv_min(sec1:int)->int:
    min1 = sec1 // 60
    return min1

def time_conv_sec(sec1:int)->int:
    r = sec1 % 60
    return r

sec1 = int(input("enter a second(s) = "))


output:str = f"output: {sec1} Second(s) = {time_conv_min(sec1)} Minutes(s) {time_conv_sec(sec1)} second(s)"
print(output)

#print("Output: ",sec1,"Second(s) = ",time_conv_min(sec1),"Minute(s)",time_conv_sec(sec1),"Scond(s)")