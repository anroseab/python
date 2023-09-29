# a=int(input('enter  a grade'))
# if  a>=90:
#     print('A')
# elif a>=80:
#     print('B')
# elif a>=70:
#     print('C')
# elif a>=0:
#     print('D')
# else:
#     print('f')

# 2
# a=int(input('enter  1st number'))
# b=int(input('enter  2nd number'))
# c=(input('enter a operator'))
# if c == "+":
#   m=a+b
#   print(m)
# elif c == "-":
#    n=a-b
#    print(n)
# elif c == "*":
#    j=a*b
#    print(j)
# elif c == "/":
#    t=a/b
#    print(t)
# else:
#    print("invalid entry")


# 3
# a=int(input('enter a number'))
# if a<=2:
#     print('infant')
# elif a<=12:
#     print('child')
# elif a<=19:
#     print('Teenager')
# elif a<=64:
#     print('Adult')
# else:
#     print('senior')

# 7
# a=int(input('enter a number(1-7)'))
# if a==1:
#     print('Sund')
# elif a==2:
#     print('mon')
# elif a==3:
#     print('tue')
# elif a==4:
#     print('wed')
# elif a==5:
#     print('thu')
# elif a==6:
#     print('fri')
# elif a==7:
#     print('satu')
# else:
#     print('invalid entry')

# 4
# weight=int(input("enter your weight"))
# height=int(input("enter your height"))
# bmi=weight/height
# if bmi<18.5:
#     print("under weight")
# elif bmi<24.9:
#     print("normal weight")
# elif bmi<29.9:
#     print("overweight")
# else:
#     print("Obesity")

# 8
a=(input('enter a character'))
if (a.isdigit()):
    print('digit')
elif a.upper or a.lower:
    print('alphabet')
else:
    print("special chara")
# print(a.isdigit())

# print(a.isalnum())


# 9
# a=str(input('enter a color'))
# b='yellow'
# c='green'
# d='red'
# if a in b:
#     print("proceed with caution")
# elif a in c:
#     print("go")
# elif a in d:
#     print('stop')
# else:
#     print("invalid color")

# 6
# a=int(input('enter a 1st number'))
# b=int(input('enter a 2st number'))
# c=int(input('enter a 3st number'))
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# elif c>a and c>b:
#     print(c)
# else:
#     print("they are eqaul")



# 10
# a=int(input('enter a time'))
# if a>=5 and a<=11.59:
#     print('good morning')
# elif a>=12  and a<=16.59:
#     print('good afternoon')
# elif a>=17  and a<=20.59:
#     print('good evening')
# elif a>=21 and a<=24:
#     print("Good night")
# elif a<=4.59:
#     print("Good night")
# else:
#     print("invalid")

# discount 
# a=int(input('enter your puchase amount'))
# if a>=100:
#     am=((10/100)*a)
#     print("dicount",am)
#     print("amount=",a-am)
# elif a>=50:
#     amount=((5/100)*a)
#     print("dicount",amount)
#     print("amount=",a-amount)
# else:
#     print(a)


# # leap 
# a=int(input('enter an year'))
# if a in range(0,3000,4) :
#     print('leap year')
# else:
#     print('not a leap year')


# number=44
# a=int(input("guess a num"))
# if number<a:
#     print('too high')
# elif number>a:
#     print("too low")
# elif number==a:
#     print('correct')

# tem
# tem=float(input("enter the temperature"))
# unit=str(input("enter the unit (fahrenheit or celsius)"))
# if unit=='fahrenheit':
#     f=(tem*1.8)+32
#     print("the fahrenheit temperature is ",f)
# elif unit=='celsius':
#     f=(tem-32)/1.8
#     print("the celsius temperature is ",f)
