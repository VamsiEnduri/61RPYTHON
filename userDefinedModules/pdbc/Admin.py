from AdminFeatures import add_student,get_student,update_student,delete_student,upload_task,upload_recording
def admin__():
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