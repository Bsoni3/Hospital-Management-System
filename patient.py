import datetime
import random
from tabulate import tabulate
import patient
import mysql.connector as co

hostname = 'localhost'
username = 'root'
password = 'rajmahal151'
database = 'sjh'

def ADM_MENU():
    while True:
        print("\t\t-------------------------------------------------------------------------")
        print("\t\t*******Welcome to Hospital Management System*******")
        print("\t\t-------------------------------------------------------------------------")
        print("\n\t\t * * ** A D M I S S I O N  M E N U   * * ** ")
        print("\t\t-------------------------------------------------------------------------")
        print("1 :  Add Patient ")
        print("2 :  Show Patient Details")
        print("3 :  Search ")
        print("4 :  Deletion")
        print("5 :  Update Patient Details")
        print("6 :  Return to MAIN MENU...")
        print("\t\t-------------------------------------------------------------------------")
        choice=int(input("Enter Your Choice 1-6 :"))
        if choice==1:
            patient.patient_details()
        elif choice==2:
            patient.show_patient_details()
        elif choice==3:
            patient.search_patient_details()
        elif choice==4:
            patient.delete_patient_details()
        elif choice==5:
            patient.edit_patient_details()
        elif choice==6:
            return
        else:
           print("_______Error : Invalid Choice try again...._______")
           conti=input("Press any key return to MAIN - MENU..")

def patient_details():
    # try:
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    pname=input('Enter Patient Name: ')
    age=int(input('Enter Patient Age: '))
    address=input('Enter Address: ')
    phon=int(input('Enter Phone Number: '))
    print('SELECT DISEASE:-')

    cursor.execute("select * from disease")
    data = cursor.fetchall()
    disease_list = []
    for row in data:
        disease_list.append([row[1]])

    if len(disease_list)>0:
        for d in range(len(disease_list)):
            print(d+1,' for ', disease_list[d])
        disease = int(input('Enter Disease#: '))
        while(disease>len(disease_list) or disease<=0):
            print('Invalid choice, enter between 1-',len(disease_list))
            disease = int(input('Enter Disease# again: '))
        ds = str(disease_list[disease-1])[2:-2]

        cursor.execute("select * from doctor where `specialization` = '%s'"%(ds))
        data = cursor.fetchall()
        doctor_list = []
        for row in data:
            doctor_list.append([row[1]])

        if len(doctor_list)>0:
            query = "INSERT INTO `patient`(`name`, `age`, `address`, `phone`, `disease`, `doctor`, `room`, `admit_date`, `recovery_date`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')" \
                .format(pname, age, address, phon, ds, str(random.choice(doctor_list))[2:-2], random.randint(1, 20),
                        datetime.datetime.today().strftime('%Y-%m-%d'), '')
            cursor.execute(query)
            cursor.close()
            mycon.commit()
            mycon.close()
            print('_______Record has been added in Patient Table_______')
        else:
            print('____NO DOCTOR available for', ds)
            print('____Hire staff fisrt___:)')
    else:
        print('_________Sorry no disease and doctor found, please add staff first:)________')

    # except:
    #     print('_______Error: while adding patient_______')

def show_patient_details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    cursor.execute("select * from patient")
    data=cursor.fetchall()

    patient_data = [[]]

    for row in data:
        patient_data.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]])
    print(tabulate(patient_data,
                   headers=['Admin_NO', 'Name', 'Age', 'Address', 'Phone', 'Disease', 'Doctor', 'Room', 'Admit_Date',
                            'Recovery_Date']))

def search_patient_details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac=input('Enter Admission Number')
    st="select * from patient where adno='%s'"%(ac)
    cursor.execute(st)
    data=cursor.fetchall()
    patient_data = [[]]

    if len(data)>0:
        for row in data:
            patient_data.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]])
        print(tabulate(patient_data,
                       headers=['Admin_NO', 'Name', 'Age', 'Address', 'Phone', 'Disease', 'Doctor', 'Room',
                                'Admit_Date',
                                'Recovery_Date']))
    else:
        print('_______NO DATE to DISPLAY_______')
    cursor.close()
    mycon.commit()
    mycon.close()
    
def delete_patient_details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac=input('Enter Admission No: ')
    st="delete from patient where adno='%s'"%(ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('_______Data Deleted Successfully_______')
    
def edit_patient_details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    
    print("1: Edit Name")
    print("2: Edit Address")
    print("3: Edit Phone Number")
    print("4: Return")
    print("\t\t-------------------------------------------------------------------------")
    choice=int(input("Enter your choice: "))
    if choice==1:
        patient.edit_name()
    elif choice==2:
        patient.edit_address()
    elif choice==3:
        patient.edit_phno()
    elif choice==4:
            return
    else:
        print("_______Error: Invalid Choice try again....._______")
        conti="press any key to return to"
        
def edit_name():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac=input('Enter Admission No: :')
    nm=input('Enter Correct Name: ')
    st="update patient set name='%s' where adno='%s'"%(nm,ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('_______Name Updated Successfully_______')
    
def edit_address():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac=input('Enter Admission No :')
    nm=input('Enter Correct Address: ')
    st="update patient set address='%s' where adno='%s'"%(nm,ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('_______Address Update Successfully_______Name')
    
def edit_phno():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac=input('Enter Admission No: :')
    nm=input('Enter Correct Phone#: ')
    st="update patient set phone='%s' where adno='%s'"%(nm,ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('_______Phone# Updated Successfully_______')