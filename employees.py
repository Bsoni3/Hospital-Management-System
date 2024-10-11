import datetime
import random
from tabulate import tabulate
import mysql.connector as co

hostname = 'localhost'
username = 'root'
password = 'rajmahal151'
database = 'sjh'


def EMP_MENU():
    while True:
        print("\t\t-------------------------------------------------------------------------")
        print("\t\t*******Welcome to Hospital Management System*******")
        print("\t\t-------------------------------------------------------------------------")
        print("\n\t\t * * ** E M P L O Y E E  M E N U   * * ** ")
        print("\t\t-------------------------------------------------------------------------")
        print("1 :  Add Employee ")
        print("2 :  Show Employee Details")
        print("3 :  Search Employee")
        print("4 :  Delete Employee")
        print("5 :  Update Employee Details")
        print("6 :  Return to MAIN MENU...")
        print("\t\t-------------------------------------------------------------------------")
        choice = int(input("Enter Your Choice 1-6 :"))
        if choice == 1:
            employee_details()
        elif choice == 2:
            show_employee_details()
        elif choice == 3:
            search_employee_details()
        elif choice == 4:
            delete_employee_details()
        elif choice == 5:
            edit_employee_details()
        elif choice == 6:
            return
        else:
            print("_______Error : Invalid Choice try again...._______")
            conti = input("Press any key return to MAIN - MENU..")


def employee_details():
    try:
        mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
        cursor = mycon.cursor()
        name = input('Enter Employee Name: ')
        password1 = input('Password: ')
        query = "INSERT INTO `user`(`name`, `password`) VALUES ('{}','{}')".format(name, password1)
        cursor.execute(query)
        cursor.close()
        mycon.commit()
        mycon.close()
        print('_______Record has been added in Employee Table_______')
    except:
        print('_______Error: while adding Employee_______')


def show_employee_details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    cursor.execute("select * from user")
    data = cursor.fetchall()

    patient_data = [[]]

    for row in data:
        patient_data.append([row[0], row[1]])
    print(tabulate(patient_data, headers=['NO#', 'Name']))


def search_employee_details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac = input('Enter Employee ID: ')
    st = "select * from user where id='%s'" % (ac)
    cursor.execute(st)
    data = cursor.fetchall()
    patient_data = [[]]

    if len(data) > 0:
        for row in data:
            patient_data.append([row[0], row[1]])
        print(tabulate(patient_data, headers=['NO#', 'Name']))
    else:
        print('_______NO DATE to DISPLAY_______')
    cursor.close()
    mycon.commit()
    mycon.close()


def delete_employee_details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac = input('Enter Employee ID: ')
    st = "delete from user where id='%s'" % (ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('_______Employee Deleted Successfully_______')


def edit_employee_details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac = input('Enter Employee ID: ')
    nm = input('Enter Correct Name: ')
    try:
        st = "update user set name='%s' where id='%s'" % (nm, ac)
        cursor.execute(st)
        cursor.close()
        mycon.commit()
        mycon.close()
        print('_______Name Updated Successfully_______')
    except:
        print('Error:- While updating Employee Name')
