# def add(a,b):
#     print(a+b)



 
import platform,psutil
  
 
print(f"Memory :{psutil.virtual_memory()}")
my_system = platform.uname()
 
print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}") 
print('The CPU usage is: ', psutil.cpu_percent(4))
print('RAM memory % used:', psutil.virtual_memory()[2])
print('RAM Used (GB):', psutil.virtual_memory()[3]/1000000000)


