bank={}
account_no=1201
li=[]
acc=[]

while True:
    print("1:create account ","2:view accound ","3:add balance","4:withdraw balance","5:exit")
    choice=int(input('enter your choice'))
    if choice==1:
        name=input("enter your name")
        bank["name"]=name
        age=int(input("enter your age"))
        bank["age"]=age
        contact=int(input("enter your phone number"))
        bank["contact"]=contact
        balance=0
        bank["balance"]=balance
        
        bank["Acc.no"]=account_no
        account_no=account_no+1
        li.append(bank.copy())
    elif choice==2:
          
          print(li)
    elif choice==3:
        account=int(input('enter your account number'))
        amount=int(input('enter your amount'))
        for i in li:
          acc.append(i['Acc.no'])
        # print(acc)
        if account in acc:
         for i in li:   
            if i['Acc.no']==account:
              i['balance']+=amount
        else:
               print("no account found")
       
    elif choice==4:
        account_no=int(input('enter your account number'))
        with_draw=int(input('enter with draw amount'))
        for i in li:
          acc.append(i['Acc.no'])
        #   print(acc)
        if account in acc:
         for i in li:   
            if i['Acc.no']==account:
              if i['balance']>=with_draw:
               i['balance']-=with_draw
        else:
            print("not posible")
    elif choice==5:
        exit()