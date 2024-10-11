import main_menu
import dr_data
import mysql.connector as co
import datetime
import random
from tabulate import tabulate

hostname = 'localhost'
username = 'root'
password = 'rajmahal151'
database = 'sjh'

def DR_MENU():
    while True:
        #admission.clrscreen()
        print("\t\t-------------------------------------------------------------------------")
        print("\t\t*******Welcome to Hospital Management System*******")
        print("\t\t-------------------------------------------------------------------------")
        print("\n\t\t * * ** D O C T O R  M E N U   * * ** ")
        print("\t\t-------------------------------------------------------------------------")
        print("1 :  Add Dr. Record ")
        print("2 :  Show Dr. Details")
        print("3 :  Search Dr. Records")
        print("4 :  Delete Dr. Records")
        print("5 :  Edit Dr. Records")
        print("6 :  Return to MAIN MENU...")
        print("\t\t-------------------------------------------------------------------------")
        choice=int(input("Enter Your Choice 1-6 :"))
        if choice==1:
            dr_data.Add_Records()
        elif choice==2:
            dr_data.Show_Dr_Details()
        elif choice==3:
            dr_data.Search_Dr_Details()
        elif choice==4:
            dr_data.Delete_Dr_Details()
        elif choice==5:
            dr_data.Edit_Dr_Details()
        elif choice==6:
            return
        else:
           print("Error : Invalid Choice try again....")
           conti=input("Press any key return to MAIN - MENU..")

def Add_Records():
#    try:
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    #  ()
    drname=input('Enter Doctor Name : ')
    drqualf=input('Enter Doctor Qualification : ')
    drage=input('Enter Age : ')
    drphon=input('Enter Phone No : ')
    drsalary=input('Enter Salary : ')
    print('SELECT',drname,"'s specialized DISEASE:-")

    cursor.execute("select * from disease")
    data = cursor.fetchall()
    disease_list = []
    for row in data:
        disease_list.append([row[1]])

    if len(disease_list) > 0:
        for d in range(len(disease_list)):
            print(d + 1, ' for ', disease_list[d])
        disease = int(input('Enter Disease#: '))
        while (disease > len(disease_list) or disease <= 0):
            print('Invalid choice, enter between 1-', len(disease_list))
            disease = int(input('Enter Disease# again: '))
        ds = str(disease_list[disease - 1])[2:-2]
    
        query="INSERT INTO `doctor`(`name`, `qualification`, `age`, `phone`, `salary`, `date_joined`, `specialization`) VALUES('{}','{}','{}','{}','{}','{}','{}')"\
            .format(drname,drqualf,drage,drphon,drsalary,datetime.datetime.today().strftime('%Y-%m-%d'), ds)
        #
        cursor.execute(query)
        cursor.close()
        mycon.commit()
        mycon.close()
        print('_______Record has been added in Doctor Table_______')
    else:
        print('____NO Disease available, register first_____')
#    except:
#        print('_______Error: while adding Doctor_______')

def Show_Dr_Details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    cursor.execute("select * from doctor")
    data=cursor.fetchall()

    patient_data = [[]]

    for row in data:
        patient_data.append([row[0], row[1], row[2], row[7], row[3], row[4], row[5], row[6]])

    print(tabulate(patient_data,
                   headers=['ID', 'Name', 'Qualification', 'Specialization', 'Age', 'Phone', 'Salary', 'Date Joined']))


def Search_Dr_Details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac=input('Enter Doctor ID: ')
    st="select * from doctor where id='%s'"%(ac)
    cursor.execute(st)
    data=cursor.fetchall()

    patient_data = [[]]

    for row in data:
        patient_data.append([row[0], row[1], row[2], row[7], row[3], row[4], row[5], row[6]])

    print(tabulate(patient_data,
                   headers=['ID', 'Name', 'Qualification', 'Specialization', 'Age', 'Phone', 'Salary', 'Date Joined']))
    
def Delete_Dr_Details():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac=input('Enter Doctor ID: ')
    st="delete from doctor where id='%s'"%(ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('____Doctor Deleted Successfully____')
    
def Edit_Dr_Details():
    
    print("1: Edit Dr. Name")
    print("2: Edit Qualifications")
    print("3: Edit Age")
    print("4: Edit Phone No.")
    print("5: Edit Salary")
    print("6: Return")
    print("\t\t-------------------------------------------------------------------------")
    choice=int(input("Enter your choice"))
    if choice==1:
        dr_data.edit_name()
    elif choice==2:
        dr_data.edit_qualf()
    elif choice==3:
        dr_data.edit_age()
    elif choice==4:
        dr_data.edit_phon()
    elif choice==5:
        dr_data.edit_sal()
    elif choice==6:
            return
    else:
        print("Error: Invalid Choice try again.....")
        conti="press any key to return to"
        
def edit_name():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac=input('Enter Doctor ID :')
    nm=input('Enter Correct Name: ')
    st="update doctor set name='%s' where id='%s'"%(nm,ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('_______Name Updated Successfully_______')
    
def edit_qualf():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac=input('Enter Doctor ID :')
    nm=input('Enter Correct Qualification')
    st="update doctor set qualification='%s' where id='%s'"%(nm,ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('_______Qualification Updated Successfully_______')

def edit_age():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac=input('Enter Doctor ID :')
    nm=input('Enter Correct Age')
    st="update doctor set age='%s' where id='%s'"%(nm,ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('_______Age Updated Successfully_______')

def edit_phon():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac=input('Enter Doctor ID :')
    nm=input('Enter Correct Phone# :')
    st="update doctor set phone='%s' where id='%s'"%(nm,ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('_______Phone# Updated Successfully_______')

def edit_sal():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    ac=input('Enter Doctor ID :')
    nm=input('Enter Correct Salary')
    st="update doctor set salary='%s' where id='%s'"%(nm,ac)
    cursor.execute(st)
    cursor.close()
    mycon.commit()
    mycon.close()
    print('_______Salary Updated Successfully_______')

