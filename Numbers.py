#Here are some operations with numbers

import math
import random

x = 123 + 222
print(x) #Expected output: 345

x = 1.5 * 4
print(x) #Expected output: 6.0

x = 2**100 #100th power of 2
print(x)

x = len(str(2**1000000)) #How many digits are there?
print(x)


x = math.pi
print(x)

x = math.sqrt(625) #Square root of 625
print(x)



x = random.random() #A number double between 0 and 1
print(x)

x = random.choice([1 , 2, 3, 4])
print(x)