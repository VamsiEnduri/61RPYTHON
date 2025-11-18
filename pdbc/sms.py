import mysql.connector
db_connection=mysql.connector.connect(
    host="localhost",
    user="root",
    database="61r_pdbc",
    password="Vamsi@1231310"
)

curObject=db_connection.cursor()
def get_student():
    wantedStu=input("enter student name here to get :--  ")
    curObject.execute("select * from students where s_name=%s",(wantedStu,))
    data=curObject.fetchone()
    print(data,"data")

def update_student():
    updatingSTuId=input("enter id hetre to update the student   ")
    query="update students set s_age=%s,s_branch=%s where s_id=%s"
    curObject.execute(query,(29,"ece",updatingSTuId))
    db_connection.commit()
    print("student detals updated successfully..........")

def delete_student():
    deletingSTuId=input("enter id here to delete the student   ")
    deletingStName=input("enter deleting student name :----")
    query="select * from students"
    curObject.execute(query)
    allData=curObject.fetchall()
    print(allData,"alldata")

    for i in allData:
        for j in i:
            if j == deletingSTuId :
                query="delete from students where s_name=%s and s_id=%s"
                curObject.execute(query,(deletingStName,deletingSTuId))
                db_connection.commit()
                print("student detals deleetd successfully..........")
            else:
                print("stduent not found with given id")  
                break;  


def add_student():
    s_id=input("enter id here :-- ")
    s_name=input("enter name here :-- ").strip().lower()
    s_age=int(input("enter age here :-- "))
    s_year=int(input("enter year of student here :-- "))
    s_branch=input("enter branch name :-- ").strip().lower()

    query="insert into students (s_id,s_name,s_age,s_year,s_branch) values (%s,%s,%s,%s,%s)"
    curObject.execute(query,(s_id,s_name,s_age,s_year,s_branch))
    db_connection.commit()
    print("student added successfullyyy.............")

def upload_task():
    task_no=int(input("enetr task number :-- "))
    task_topic=input("enter task topic :--   ")
    task_file=input("enter drive link of task :--  ")
    task_date=input("enter date of task here :---   ")
    query="insert into tasks (t_id,t_topic,s_file,s_date) values (%s,%s,%s,%s)"
    curObject.execute(query,(task_no,task_topic,task_file,task_date))
    db_connection.commit()
    print("task added successfully........")

def upload_recording():
    re_no=int(input("enetr task number :-- "))
    re_topic=input("enter task topic :--   ")
    re_file=input("enter drive link of task :--  ")
    re_date=input("enter date of task here :---   ")
    query="insert into recordings (r_id,r_topic,r_file,r_date) values (%s,%s,%s,%s)"
    curObject.execute(query,(re_no,re_topic,re_file,re_date))
    db_connection.commit()
    print("recording added successfully........")

def get_tasks():
    curObject.execute("select * from tasks")
    data=curObject.fetchall()
    print(data,"all tasks")

def get_recordings():
    curObject.execute("select * from recordings")
    data=curObject.fetchall()
    print(data,"all recordings")    

def upload_taskByStu():
    s_id=int(input("enter s_id here :-- "))
    t_id=int(input("enter t_no here :-- "))
    t_file=input("paste task drive link :--  ")
    query="insert into tasksByStudnets (s_id,t_id,t_file) values (%s,%s,%s)"
    curObject.execute(query,(s_id,t_id,t_file))
    db_connection.commit()
    print("task upload successfully by student with id",s_id)


def getTasksPerStudent():
    s_id=int(input("enter students id to fetch all tasks of him "))
    query="select   students.s_id,tasksByStudnets.t_id,tasksByStudnets.t_file   from students join tasksByStudnets on students.s_id =tasksByStudnets.s_id  where students.s_id=%s "
    curObject.execute(query,(s_id,))
    data=curObject.fetchall()
    print(data,"all task by student with id",s_id)

while True:
    print("choose yr role ;--")
    print("1.wanna login as admin ;--")
    print("2.wanna login as student ;--")
    role=input("enetr yr role here :--  like 1 r 2")
    if role == "2":
        print("choose yr features as yr are student :---  ")
        print("1. get tasks")
        print("2.get recordings")
        print("3.upload tasks")
        print("4.get attenance")
        print("5.get interview kit")

        op=input("enetr the feature you want to proceed with :-- ")
        if op == "1":
            get_tasks()
        if op == "2":
            get_recordings()   

        if op == "3":
            upload_taskByStu()

        if op == "4":
            get_att()

        if op == "5":
            get_interviewKit()             




    if role == "1":
        print("choose below options as admin :-- ")
        print("1.add student")
        print("2.get student")
        print("3.update student")
        print("4.delete student")
        print("5.add task")
        print("6.upload class recordings")
        print("7.fetch individual studnets tasks")

        op=int(input("enetr yr option number here :--- "))
    
        if op == 1:
            add_student()
        if op == 7:
            getTasksPerStudent()
        if op == 2 :
            get_student()   
        if op==3:
            update_student()  
        if op == 4:
            delete_student()     
        if op==5:
            upload_task()   

        if op==6:
            upload_recording
