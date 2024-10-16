import utlis
import random
import math
import time
import os      # needs check
import my_modules.hello

my_modules.hello.greeting1()

utlis.greeting()

print(int(random.random()*100))

print(math.sqrt(16))
print(math.pi)
print(time.time())

start_time = time.time()
sum(range(1000000))
end_time = time.time()
print(f"Eecute time : {start_time - end_time}, seconds")



