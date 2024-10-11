import datetime
import random
from tabulate import tabulate
import mysql.connector as co

hostname = 'localhost'
username = 'root'
password = 'rajmahal151'
database = 'sjh'


def DSE_MENU():
    while True:
        print("\t\t-------------------------------------------------------------------------")
        print("\t\t*******Welcome to Hospital Management System*******")
        print("\t\t-------------------------------------------------------------------------")
        print("\n\t\t * * ** D I S E A S E  M E N U   * * ** ")
        print("\t\t-------------------------------------------------------------------------")
        print("1 :  Add Disease ")
        print("2 :  Show Disease Details")
        print("3 :  Search Disease")
        print("4 :  Delete Disease")
        print("5 :  Update Disease Details")
        print("6 :  Return to MAIN MENU...")
        print("\t\t-------------------------------------------------------------------------")
        choice = int(input("Enter Your Choice 1-6 :"))
        if choice == 1:
            disease_details()
        elif choice == 2:
            show_disease_details()
        elif choice == 3:
            search_disease_details()
        elif choice == 4:
            delete_disease_details()
        elif choice == 5:
            edit_disease_details()
        elif choice == 6:
            return
        else:
            print("_______Error : Invalid Choice try again...._______")
            conti = input("Press any key return to MAIN - MENU..")


def disease_details():
    try:
        mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
        cursor = mycon.cursor()
        disease = input('Enter Disease: ')
        charges = int(input('Charges per Day: '))
        query = "INSERT INTO `disease`(`name`, `charges`) VALUES ('{}','{}')" \
            .format(disease, charges)
        cursor.execute(query)
        cursor.close()
        mycon.commit()
        mycon.close()
        print('_______Record has been added in Disease Table_______')
    except:
        print('_______Error: while adding Disease_______')


def show_disease_details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    cursor.execute("select * from disease")
    data = cursor.fetchall()

    patient_data = [[]]

    for row in data:
        patient_data.append([row[0], row[1], row[2]])
    print(tabulate(patient_data, headers=['NO#', 'Name', 'Charges']))


def search_disease_details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac = input('Enter Disease ID: ')
    st = "select * from disease where id='%s'" % (ac)
    cursor.execute(st)
    data = cursor.fetchall()
    patient_data = [[]]

    if len(data) > 0:
        for row in data:
            patient_data.append([row[0], row[1], row[2]])
        print(tabulate(patient_data, headers=['NO#', 'Name', 'Charges']))
    else:
        print('_______NO DATE to DISPLAY_______')
    cursor.close()
    mycon.commit()
    mycon.close()


def delete_disease_details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac = input('Enter Disease ID: ')
    st = "delete from disease where id='%s'" % (ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('_______Disease Deleted Successfully_______')


def edit_disease_details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()

    print("1: Edit Name")
    print("2: Edit Charges")
    print("4: Return")
    print("\t\t-------------------------------------------------------------------------")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        edit_name()
    elif choice == 2:
        edit_charges()
    elif choice == 3:
        return
    else:
        print("_______Error: Invalid Choice try again....._______")
        conti = "press any key to return to"


def edit_name():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac = input('Enter Disease ID: ')
    nm = input('Enter Correct Name: ')
    st = "update disease set name='%s' where id='%s'" % (nm, ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('_______Name Updated Successfully_______')


def edit_charges():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac = input('Enter Disease ID: ')
    nm = input('Enter Correct Charges: ')
    st = "update disease set charges='%s' where id='%s'" % (nm, ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('_______Charges Update Successfully_______Name')


def edit_id():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac = input('Enter Admission No: :')
    nm = input('Enter Correct Phone#: ')
    st = "update disease set ch='%s' where adno='%s'" % (nm, ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('_______ID Updated Successfully_______')