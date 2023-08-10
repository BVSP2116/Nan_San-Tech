import mysql.connector as sql
db=sql.connect(host="localhost", user="root", passwd="mysql", database="Project")
if db.is_connected()==False:
    print("Cannot connect to the Database")
cursor=db.cursor()

def First():
    print("\n ")
    print("/t /t /t NAN_SAN TECHNOLOGIES")
    print('/n')
    print('TASK MANAGER')
    print('------------')
    print('1.ADMIN')
    print('2.USER')
    print('3.EXIT')
    a=int(input('Enter your Choice(1,2,3): '))
    if a==1:
        Admin()
    elif a==2:
        User()
    elif a==3:
        Exit()                                    
    else:
        print("Retry")
        First()
        
def Exit():
    print("Exited Successfully")
    return

def Admin():
    def a_view():
        b="select User_ID,User_Name from Users"
        cursor.execute(b)
        data=cursor.fetchall()
        if data == None:
           print('NO USERS AVAILABLE!!')
        else:
            for row in data:
                print(row)
                
    def a_delete():
        c=input("Are you sure you want to delete permanently(y/n):")
        if (c=="Y" or c=="y"):
            uid=int(input("Enter the user id:"))
            del1="DELETE FROM USERS WHERE USER_ID='{}' ".format(uid)
            cursor.execute(del1)
            db.commit()
            print("Deleted Successfully")
        elif(c=="n" or c=="N"):
            print("User details not deleted")
        else:
            print("Try again")
            a_delete()
    def count_comp():
        b='select count(User_ID) from taskcomp group by Completion_Status where Comp_status=="Completed"'
        cursor.execute(b)
        data=cursor.fetchall()
        print("The total users who COMPLETED their tasks are: ",data)
        return data
    def count_ong():
        b='select count(User_ID) from taskcomp group by Completion_Status where Comp_status=="Ongoing"'
        cursor.execute(b)
        data=cursor.fetchall()
        print("The total users whose tasks are ONGOING are: ",b)
        return data
    def count_notyet():
        b='select count(User_ID) from taskcomp group by Completion_Status where Comp_status=="Not Yet Started"'
        cursor.execute(b)
        data=cursor.fetchall()
        print("The total users whose tasks are NOT YET STARTED are: ",b)
        return data
    def count_disc():
        b='select count(User_ID) from taskcomp group by Completion_Status where Comp_status=="Discarded"'
        cursor.execute(b)
        data=cursor.fetchall()
        print("The total users who have DISCARDED their tasks are: ",b)
        return data
    
        #mains#
    print("\n -----------------------") 
    print("  ADMIN MENU")
    print("-----------------------")
    print("1.View  ")
    print("2.Delete")
    print("3.Count Users w.r.t their Current Completion Status")
    print("4.Exit")
    a=int(input("Enter your choice(1,2,3,4,5): "))
    if a==1:
        a_view()
        Admin()
    elif a==2:
        a_delete()  
        Admin()
    elif a==3:
      count_comp()
      count_ong()
      count_notyet()
      count_disc()
      Admin() 
    elif a==4:                  
        Exit()
    else:
        print("Retry")
        Admin()
        First()
       
def User():
    def U_Create():
        mail=input("Enter you mail id: ")
        pas=input('Create a Password: ')
        recheck=input("Retype your Password: ")
        if pas==recheck:
            print('Successfully created Mail ID.....Enter Further details!!')
            b=int(input("User_id: "))
            c=input("Enter User_Name: ")
            m=mail
            pwd=pas
            ins="insert into Users values({},'{}','{}','{}'".format(b,c,m,pwd)
            cursor.execute(ins)
            db.commit()
            print('User Added to NAN_SAN TECHNOLOGIES!!')
        else:
            print("Retry Again!!")
            U_Create()

    def Exist_User():
        mail=input("Enter you mail id: ")
        pas=input('Enter your Password: ')
        b="select User_Mail_ID from users"
        cursor.execute(b)
        data=cursor.fetchall()
        if mail in data:
            c="select Password from users"
            cursor.execute()
            data=cursor.fetchall()
            if c in pas:
                print('SUCCESSFULLY LOGGED IN TO TASK MANAGER!!')
            else:
                print('Password is Incorrect.... Try Again!!')
                Exist_User()
        else:
            print('You have entered an Incorrect Mail ID!!!')
            z=input("Do you want to Create a New account(y/n): ")
            if (z=="Y" or z=="y"):
                U_Create()
            elif(z=="n" or z=="N"):
              print('Try Again')
              Exist_User()
                   
        
        def create():
            task_id=int(input('Enter Unique Task ID: '))
            task_name = input("Enter the Task name: ")
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            task_details = input("Enter task details: ")
            P_Level=input('Enter the Priority Level(1-10)')
            ins="insert into tasks(Task_ID,Task_Name,task_Details,Due_Date,Priority_level) values({},'{}','{}','{}','{}',)".format(task_id,task_name,task_details,due_date,P_Level)
            cursor.execute(ins)
            db.commit()
            print('TASK HAS BEEN ADDED SUCCESSFULLY!!!')
            
        def update_status():
            task_id=input('Enter the Task ID to change the Status: ')
            Comp_Status= input('Completed/Inprogress/Yet to Start/Discarded: ')
            sql="update tasks set Completion_Status='{}' where task_id={}".format(Comp_Status,task_id)
            cursor.execute(sql)
            db.commit()
            print('TASK STATUS UPDATED SUCESSFULLY!!')
        
        def view():
            view="select * from tasks"
            cursor.execute(view) 
            data=cursor.fetchall()
            for row in data:
                print("\n",row)
            
        def delete_user():
            b=int(input("User id to be deleted:"))
            c=input("Are you sure you want to delete permanently(y/n):")
            if (c=="Y" or c=="y"):
                del1="DELETE FROM Users WHERE User_ID={}". format(b)             
                cursor.execute(del1)
                db.commit()
                print("Deleted Successfully")
            elif(c=="n" or c=="N"):
                print("User details not deleted")
            else:
                print("Try again")
                delete_user()  
           
            def delete_task():
                b=input('Enter the User ID: ')
                c=input('Enter Task ID: ')
                d=input('Are you Sure you want to delete the task?(y/n): ')
                if (d=="Y" or d=="y"):
                    del1="DELETE FROM tasks WHERE Task_ID={}". format(b)             
                    cursor.execute(del1)
                    db.commit()
                    print("Deleted Successfully")
                elif(c=="n" or c=="N"):
                    print("Task not deleted")
                else:
                    print("Try again")
                    delete_task()  
                
        
        def edit():
            task_id=int(input('Enter your Task ID: '))
            task_name = input("Enter the task name: ")
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            task_details = input("Enter task details: ")
            P_Level=input('Enter the Priority Level(1-10)')
            edit="update tasks set Task_Name='{}',Task_Details='{}',Due_Date='{}',Priority_Level='{}' where user_ID={}".format(task_name,task_details,due_date,P_Level,task_id)
            cursor.execute(edit)
            db.commit()
            
            ## After Signing in...        
        print("1.Create a Task:  ")
        print("2.Update Task Status: ")
        print("3.Display all tasks: ")
        print("4.Edit the Task: ")
        print('5.Delete the task: ')
        print("6.Logout")
        b=int(input("Enter your choice(1,2,3,4,5,6): "))
        if b==1:
            create()
            Exist_User()
        elif b==2:
            update_status()  
            Exist_User()
        elif b==3:
            view()
            Exist_User()
        elif b==4:                  
            edit()
            Exist_User()
        elif b==5:
            delete_user()
            Exist_User()
        elif b==6:
            User()
        else:
            print("Retry")
            Exist_User()
    ##MAINS##
    print("\n -----------------------") 
    print("  USER MENU")
    print("-----------------------")
    print('1. Create User: ')
    print("2. Login as Existing User: ")
    print("3.Move to Main MEnu")
    a=int(input('Enter your Choice: '))
    if a==1:
        U_Create()
        User()
    elif a==2:
        Exist_User()
        User()
    elif a==3:
        First()

First()
db.close()

