import mysql.connector as sql
db=sql.connect(host="localhost", user="root", passwd="mysqlpassword", database="patient")
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
            del="DELETE FROM USERS WHERE USER_ID={} ".format(uid)
            cursor.execute(del)
            db.commit()
            print("Deleted Successfully")
        elif(c=="n" or c=="N"):
            print("User details not deleted")
        else:
            print("Try again")
            a_delete()
    def count_comp():
        b='select count(User_ID) from Users group by Completion_Status'
        cursor.execute(b)
        data=cursor.fetchall()
        db.commit()
    def count_ong():
    def count_notyet():
    def count_disc():
        
def User():
    def Create():
        b=int(input("User_id:"))
        c=input("Enter User_Name:")
        ins=insert into User values({},'{}').format(b,c)
        cursor.execute(ins)
        db.commit()
        print('User Added to NAN_SAN TECHNOLOGIES!!')
    def Exist_User():
        b=int(input("User_id:"))
        c=input("Enter User_Name:")
        print('SUCCESSFULLY CONNECTED TO TASK MANAGER!!')
        
        def create():
            task_name = input("Enter the task name: ")
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            task_details = input("Enter task details: ")
            P_Level=input('Enter the Priority Level(1-10)')
            ins="insert into tasks(task_name,task_details,due_date,Priority_level) values('{}','{}','{}','{}',)".format(task_name,task_details,due_date,Plevel)
            cursor.execute(ins)
            db.commit()
            print('TASK HAS BEEN ADDED SUCCESSFULLY!!!')
            
        def update_status():
            task_name=input('Enter the Task Name to change the Status: ')
            Comp_Status= input('Completed/Inprogress/Yet to Start/Discarded: ')
            sql="update tasks set Completion_Status='{}' where task_name='{}' and user_name='{}'".format(Comp_Status,task_name,use)
            cursor.execute(sql)
            db.commit()
            print('TASK STATUS UPDATED SUCESSFULLY!!')
        
        def view():
            id=input("VIEW THE TASKS ASSIGNED:")
            view="select * from patient"
            cursor.execute(view)
            data=cursor.fetchall()
            for row in data:
                print("\n",row)
            
            
            
        
        
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        