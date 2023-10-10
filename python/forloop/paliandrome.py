# x=input("enter a number")
# # x=101
# if x==x[::-1]:
#     print("True")
# else:
#     print("False")


# merge sort
# list1=[1,3,5]
# list2=[2,4,6]
# list3=list1+list2
# list3.sort()
# print(list3)

# duplicate
# a=[1,2,6,6,8,8]
# b=set(a)
# c=list(b)
# print(len(c))
# c.sort()
# print(c)




# lenght of last word
# a='qeqerw dakroai jnahusdf www'
# b=a.split()
# c=b[-1]
# print(len(c))

# 206 reverse
# li=[1,2,3,4,8]
# # b=li[-1]
# print(li)
# b=li[::-1]
# print(b)


# 217
# a=[1,2,3,1]
# b=set(a)
# if a==b:
#     print("false")
# else:
#     print("true")


# 27 remove
# num=[1,1,2,3,1]
# value=1
# for i in num:
#     if i==value:
#         num.remove(i)
# print("lenght",len(num))
# print(num)


#  414
# a=list(input("enter a list"))
# a.remove(max(a)) 
# print(a)    


# 
# a=list(input("enter a list"))
# b=[]
# for i in a:
#     if i in range(i,a+1,2):
#         print(b.append())
       



# 
# s=['h','e',"l",'o']
# s.reverse()
# print(s)

# a=[1,2,3,4,5]
# b=[]
# target=6
# for i in  a:
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==target:
            
#             print("True")
#         else:
#             print("false")


# 434
# a='hello, hi we wewfds'
# b=a.split()
# print(len(b))

# 392
# a='abc'
# target='qwabc'
# for i in a:
#         x=0
# if i in target:
#         print("true")
# else:
#         print("false")


# 414
# a=[1,2]
# if len(a)>2:
#   b=max(a)
#   a.remove(b)
#   c=max(a)
#   a.remove(c)
#   print(max(a))
# else:
#   print(max(a))



# 231
# n=int(input("enter a number"))
# while (n % 2 == 0): 
#      n = n/2
# if n==1:
#         print("true")
# else:
#         print("false")


# 342
# n=int(input("enter a number"))
# while (n % 2 == 0): 
#      n = n/4
# if n==1:
#         print("true")
# else:
#         print("false")


# # li='ABABAABBBBAB'
# a=li.count('A')
# b=li.count('B')
# if a==b:
#     print("balanced")
# else:
#     print("unbalanced")



# 191
# a='000000000010101001010111111'
# print(a.count('1'))

# 326
# n=int(input("enter a number"))
# while (n % 3== 0): 
#      n = n/3
# if n==1:
#         print("true")
# else:
#         print("false")

# s=input("enter a input")
# s='{}[]()'
# s.split()
# if s=='[]':
#     print("true")
# elif s=='{}':
#     print("true")
# elif s=='()':
#     print("true")
# else:
#     print("false")


# 2235
# n=int(input("enter a number"))
# v=int(input("enter a number"))
# c=n+v
# print(c)

# 2733
# a=[1,2,3,4,8,5]
# if len(a)>2:
#   b=max(a)
#   a.remove(b)
#   c=min(a)
#   a.pop(c)
#   print(max(a))
# else:
#   print("-1")


# a=[1,1,1,1,2,3,4,44,5,3]
# b=len(a)
# for i in range(b):
#      if a.count(i)>b/2:
#          print(i) 
