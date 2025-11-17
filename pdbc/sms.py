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
while True:
    print("choose below options")
    print("1.add student")
    print("2.get student")
    print("3.update student")
    print("4.delete student")

    op=int(input("enetr yr option number here :--- "))
    
    if op == 1:
        add_student()
    if op == 2 :
        get_student()   
    if op==3:
        update_student()  
    if op == 4:
        delete_student()      