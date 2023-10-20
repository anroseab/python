student={}

reg=100
st=[]
tea=[]
store=[]
teacher=[]
while True:
    print("1:student","2:Teacher","3:view student","4:view teachers","5:exit")
    choice=int(input("enter your choice"))
    if choice==1:
        name=input("enter ur name")
        student["name"]=name
        age=int(input("enter ur age"))
        student["age"]=age
        cla=input("enter ur department")
        student["class"]=cla
        student["register_no"]=reg
        reg=reg+1
        st.append(student.copy())

    if choice==2:
        name=input("enter ur name")
        tea.append(name)
        clas=int(input("enter class"))
        tea.append(clas)
    if choice==3:
        print(st)
    if choice==4:
        print(tea)
    if choice==5:
        
        

        stu=input("enter the name of student")
        for i in st:
          store.append(i["name"])
        b=len(tea)
        for j in range(b):
           if stu in store:
             for i in st:
            #    print(stu)
                # print(i['name'])
                if i["name"]==stu:
                 
                 i['teacher']=tea[j]    
           print(st)
    if choice==6:
      for i in st:
          store.append(i["cla"])
      for j in tea:
          teacher.append(j['clas'])
      for k in store:
         for m in teacher:
            if k==m:
               
    if choice==6:
        exit()

