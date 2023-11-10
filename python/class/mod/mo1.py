# import math
# # import mod2 
# # a=int(input("enter a number"))
# # b=int(input("enter a number"))

# # mod2.add(a,b)
# print("cos(1)=",math.cos(1))
# print(math.sin(1))
# print(math.sqrt(10))
# print(math.factorial(10))


import platform,os,getpass
from datetime import date 
# import arch


# print(os.getcwd()) 
print(platform.system())
print(platform.architecture())
print(platform.processor())
today = date.today() 
print(getpass.getuser())

print("Today's date is", today) 
# print(arch.)