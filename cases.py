import datetime
import random
from tabulate import tabulate
import cases
import mysql.connector as co

hostname = 'localhost'
username = 'root'
password = 'rajmahal151'
database = 'sjh'


def CASES_MENU():
    while True:
        print("\t\t-------------------------------------------------------------------------")
        print("\t\t*******Welcome to Hospital Management System*******")
        print("\t\t-------------------------------------------------------------------------")
        print("\n\t\t * * ** C A S E S  M E N U   * * ** ")
        print("\t\t-------------------------------------------------------------------------")
        print("1 :  Add Patient to Recovery")
        print("2 :  Show Patient Details")
        print("3 :  Search ")
        print("4 :  Deletion")
        print("5 :  Return to MAIN MENU...")
        print("\t\t-------------------------------------------------------------------------")
        choice = int(input("Enter Your Choice 1-6 :"))
        if choice == 1:
            cases_details()
        elif choice == 2:
            show_cases_details()
        elif choice == 3:
            search_cases_details()
        elif choice == 4:
            delete_cases_details()
        elif choice == 5:
            return
        else:
            print("_______Error : Invalid Choice try again...._______")
            conti = input("Press any key return to MAIN - MENU..")


def cases_details():
    # try:
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac = input('Enter Admission No: :')

    cursor.execute("select disease, admit_date from patient where adno='%s'"%(ac))
    data = cursor.fetchone()
    d1 = datetime.datetime.strptime(data[1], "%Y-%m-%d")
    d2 = datetime.datetime.strptime(datetime.datetime.today().strftime('%Y-%m-%d'), "%Y-%m-%d")

    cursor.execute("select charges from disease where name='%s'" % (data[0]))
    data = cursor.fetchone()

    bill = (((d2 - d1).days)+1)*data[0]

    st = "update patient set recovery_date='%s', bill='%s' where adno='%s'" % (datetime.datetime.today().strftime('%Y-%m-%d'), bill, ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('_______Patient Recovered Successfully_______')


def show_cases_details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    cursor.execute("select * from patient where recovery_date=''")
    data = cursor.fetchall()

    patient_data = [[]]

    for row in data:
        patient_data.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
    print(tabulate(patient_data,
                   headers=['Admin_NO', 'Name', 'Age', 'Address', 'Phone', 'Disease', 'Doctor', 'Room', 'Admit_Date']))


def search_cases_details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac = input('Enter Admission Number')
    st = "select * from patient where adno='%s' and recovery_date='' " % (ac)
    cursor.execute(st)
    data = cursor.fetchall()
    patient_data = [[]]

    if len(data) > 0:
        for row in data:
            patient_data.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
        print(tabulate(patient_data,
                       headers=['Admin_NO', 'Name', 'Age', 'Address', 'Phone', 'Disease', 'Doctor', 'Room',
                                'Admit_Date']))
    else:
        print('_______NO DATE to DISPLAY_______')
    cursor.close()
    mycon.commit()
    mycon.close()


def delete_cases_details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac = input('Enter Admission No: ')
    st = "delete from patient where adno='%s' and recovery_date=''" % (ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('_______Data Deleted Successfully_______')

