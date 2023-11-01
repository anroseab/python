# 268

# a=[9,6,4,2,3,5,0,1]
# b=max(a)
# for i in range(b):
#     if i not in a:
#         print(i)
        
#17
# # letter={2:["a","b","c"]}
# # letter={2:["a","b","c"],3:'def',4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
# # a=['abc','def']
# # c=len(a)
# b=int(input("enter your choice"))
# # for i in range(c,):
# #     for j in a: 
# #       print(i[j])
# # for i in letter:
# #     print(i[2])




# # 17
# a=['abc','def']
# # c=a.split()
# b=len(a)
# # for i in a:
# # #    b.append(i[0])
# # print(b)

# for i in range(0,b+1):
#     for j in a:
#         print(j)
            
#  17       
# letter={0:'',1:"",2:'abc',3:'def',4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
# a=int(input("enter the number"))
# if a<=9:
  
#   num=letter[a]
#   for i in num:
#      print(i)

# elif a>9 and a<100:
#   b=a//10
#   c=a%10
#   num=letter[b]
#   num1=letter[c]
#   for i in num:
#      for j in num1:
#         print(i+j)
#      print("")
        
# elif a>99 and a<1000:
#    p=a//100
#    c=a%100
#    d=c//10
#    f=c%10
#    w=letter[p]
#    x=letter[d]
#    y=letter[f]
#    for i in w:
#       for j in x:
#          for k in y:
#             print(i+j+k)
#          print("")

# 371
# a=int(input("enter a number"))
# b=int(input("enter 2nd number"))
# c=(sum((a,b)))

# print(c)


# 29
# a=int(input("enter a number"))
# b=int(input("enter 2nd number"))
# c=a//b
# print(c)




# 34
# a=[5,7,7,8,8,10]
# b=[]
# target=8
# if target in a:
#       for i in range(0,len(a)):
#          if a[i]==target:
#                b.append(i)
#                print(b)    
# else:
#      print("[-1,-1]")



# 167
# a=[2,3,4,5,7]
# b=[]
# target=6
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==target:
#             b.append(i+1)
#             b.append(j+1)
#             print(b)

