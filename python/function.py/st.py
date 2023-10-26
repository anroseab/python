student={}

reg=100
st=[]
tea=[]
store=[]
teacher=[]
stor=[]
teache=[]
while True:
    print("1:student","2:Teacher","3:view student","4:view teachers","5:assign teacher","6:class","7:exit")
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
        st.append(student.copy())

    if choice==2:
        name=input("enter ur name")
        tea.append(name)
        # clas=int(input("enter class"))
        # tea.append(clas)
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
           
                if i["name"]==stu:
                #   for j in tea:
                    i['teacher']=tea[j]
         else:
              print("the student is not found")  
        print(st)
    if choice==6:

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
       print(st) 
               
    if choice==7:
        exit()

