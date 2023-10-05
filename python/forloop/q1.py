# a=int(input('enter the limit'))
# sum=0
# for i in range(a):
#     b=int(input("enter the elements"))
#     sum+=b
# print(sum)
   

# count the no of duplicate elements in a list

# c=set(a)
# print(c)
# for i in a:
    
#     b=a.count(i)
#     if b>1:   
#         print("element =",i,'duplicate=',a.count(i))
        
# x=set(a)
# print(x)

a=[1,1,2,3,3,1]
c=0
d=[]
for i in set(a):
   
    b=a.count(i)
    
    if b>1:
        
        print(i,b)
        c+=b
        
print("total number of duplication",c)




        

