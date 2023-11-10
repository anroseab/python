student={}
reg=100
st=[]
tea=[]
store=[]
teacher=[]
sto=[]
teache=[]

while True:
    print("1:student","2:Teacher","3.view","4:assign teacher","5:class","6:fees","7:teacher_st","8:fees_st","5:exit")
    choice=int(input("enter your choice"))
    if choice==1:
        name=input("enter ur name")
        student["name"]=name
        age=int(input("enter ur age"))
        student["age"]=age
        clas=int(input("enter class"))
        student['class']=clas
        student["register_no"]=reg
        reg=reg+1
        fe=12000
        student['fees_balance']=fe
        st.append(student.copy())

    if choice==2:
        name=input("enter ur name")
        tea.append(name)
        
    if choice==3:
        print(st)
    # if choice==4:
    #     print(tea)
    if choice==4:
        stu=input("enter the name of student")
        for i in st:
          store.append(i["name"])
        b=len(tea)
        for j in range(b):
         if stu in store:
             for i in st:
           
                if i["name"]==stu:
                #   for j in tea:
                    i['teacher']=tea[j]
         else:
              print("the student is not found")  
        for i in st:           
          print("-"*20)
          for j,k in i.items():
              print(j,":",k)
          print("-"*20)
    if choice==5:

       st_class=int(input("enter the class"))
       for i in st:
          store.append(i["class"])
   
       if st_class in store:
             for i in st:
           
                if i["class"]== st_class:
                   for n in tea:
                      
                     i['teacher']=tea[0]
                else:
                      i["teacher"]=tea[1]
       for i in st:           
          print("-"*20)
          for j,k in i.items():
              print(j,":",k)
          print("-"*20) 
               
    if choice==6:
        name=input("enter ur name")
        clas=int(input("enter your clas"))
        for i in st:
          store.append(i["class"])
        for i in st:
          store.append(i["name"])  
        if clas  in store:
          if name in store: 
           amount=int(input("enter the amount"))
           for i in st:
              if i["class"]==clas and i['name']==name:
                    i["paid"]=amount
                    i['fees_balance']=fe-amount
                 
                    if i['fees_balance']==0:
                       i['fees_balance']=0
           print(st)  
          else:
            print("student not fount")   
        else:
            print("student not fount")         
    if choice==7:
       teacher=input("enter the teacher name")
     
       if teacher in tea:
           for i in st:
              if i['teacher']==teacher:
                  teache.append(i['name'])
           print(teache)
    if choice==8:
       for i in st:
           
          #  nam.append(i['name'])
          #  paid.append(i['paid'])
          #  fees.append(i['fees_balance'])
           print("name:",i['name'], ',  paid:',i["paid"],", fees_balance:",i["fees_balance"])
    if choice==9:
         exit()

