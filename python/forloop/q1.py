# a=int(input('enter the limit'))
# sum=0
# for i in range(a):
#     b=int(input("enter the elements"))
#     sum+=b
# print(sum)
   

# count the no of duplicate elements in a list
a=[1,2,3,3,2,1,3,4,]
# c=set(a)
# print(c)
for i in a:
    
    b=a.count(i)
    if b>1:   
        print("element =",i,'duplicate=',a.count(i))
        
# x=set(a)
# print(x)

    
    

        

