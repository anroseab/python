# a=int(input('enter a number'))

# for i in range(1,a+1):
#     for j in range(1,i):
#         print(j,end='')
#     for j in range(i,0,-1):
#         print(j,end='')
     
#     print('')
a=int(input('enter a number'))
print('*')
for i in range(1,a+1):
    
    for j in range(1,i):
        print(j,end='')
    for j in range(i,0,-1):
        print(j,end='', )
  
    print('')
