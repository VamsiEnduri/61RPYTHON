from db_c import db_connection
a=db_connection
curObject=a.cursor()
def get_student():
    wantedStu=input("enter student name here to get :--  ")
    curObject.execute("select * from students where s_name=%s",(wantedStu,))
    data=curObject.fetchone()
    print(data,"data")

def update_student():
    updatingSTuId=input("enter id hetre to update the student   ")
    query="update students set s_age=%s,s_branch=%s where s_id=%s"
    curObject.execute(query,(29,"ece",updatingSTuId))
    a.commit()
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
                a.commit()
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
    a.commit()
    print("task added successfully........")

def upload_recording():
    re_no=int(input("enetr task number :-- "))
    re_topic=input("enter task topic :--   ")
    re_file=input("enter drive link of task :--  ")
    re_date=input("enter date of task here :---   ")
    query="insert into recordings (r_id,r_topic,r_file,r_date) values (%s,%s,%s,%s)"
    curObject.execute(query,(re_no,re_topic,re_file,re_date))
    a.commit()
    print("recording added successfully........")
