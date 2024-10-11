# -*- coding: utf-8 -*-
import main_menu
import report
import mysql.connector as co

hostname = 'localhost'
username = 'root'
password = 'rajmahal151'
database = 'sjh'


def gr_rep():
    while True:
        print("\t\t-------------------------------------------------")
        print("\t\t*******Welcome to Hospital Management System*******")
        print("\t\t-------------------------------------------------")
        print("\n\t\t*******GRAPHICAL REPORT*******")
        print("1 : Age Wise Patient Details")
        print("2 : Disease Wise Patient Details")
        print("3 : Date Wise Earning")
        print("4 : Disease Wise Earning")
        print("5 : Doctor Wise Work Effort")
        print("6 : Patient Wise Earning")
        print("7 : Return")
        print("\t\t-------------------------------------------------")
        choice = int(input("Enter Your Choice :"))
        if choice == 1:
            awpd()
        elif choice == 2:
            dwpd()
        elif choice == 3:
            edwpd()
        elif choice == 4:
            sdwpd()
        elif choice == 5:
            dpd()
        elif choice == 6:
            ewpd()
        elif choice == 7:
            return
        else:
            print("Error: Invalid Choice try again......")
            conti = input("press any key to continue")


def awpd():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    cursor.execute("select distinct(age) from patient group by age")
    data = cursor.fetchall()
    clas = []
    for row in data:
        clas.append(row[-1])
    print('Distinct Age:', clas)
    cursor.execute("select count(age) from patient group by age")
    data = cursor.fetchall()
    no_o_p = []
    for row in data:
        no_o_p.append(row[-1])
    print('Patient Age:', no_o_p)
    
    import matplotlib.pyplot as plt
    import numpy as np

    y = np.array(no_o_p)
    val=np.arange(len(clas))
    plt.bar(val,height=no_o_p)
    plt.xticks(val,clas)
    plt.xlabel('Patients Age')
    plt.ylabel('No. Of Patients')
    plt.title('Age Wise Patient Details')
    plt.show()


def dwpd():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    cursor.execute("select distinct(disease) from patient group by disease")
    data = cursor.fetchall()
    ssn = []
    for row in data:
        ssn.append(row[-1])
    print('Distinct disease:', ssn)
    cursor.execute("select count(disease) from patient group by disease")
    data = cursor.fetchall()
    no_o_ssn = []
    for row in data:
        no_o_ssn.append(row[-1])
    print('Number of Disease :', no_o_ssn)
    import matplotlib.pyplot as pl
    import numpy as np
    val1=np.arange(len(ssn))
    
    pl.bar(val1,height=no_o_ssn)
    pl.xticks(val1,ssn)
    pl.xlabel('Diseases')
    pl.ylabel('No. Of Patients')
    pl.title('Disease Wise Patient Details')
    pl.show()
    


def ewpd():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    cursor.execute("select name,bill from patient where bill!='None'")
    data = cursor.fetchall()
    ssn = []
    name = []
    for row in data:
        name.append(row[0])
        ssn.append(row[-1])
    print('Distinct disease:', ssn)
    import matplotlib.pyplot as pl
    print(pl.pie(ssn, labels=name))
    pl.show()


def edwpd():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    cursor.execute("select recovery_date, bill from patient where bill!='None' group by recovery_date")
    data = cursor.fetchall()
    ssn = []
    name = []
    for row in data:
        name.append(row[0])
        ssn.append(row[-1])
    print('Distinct disease:', ssn)
    import matplotlib.pyplot as pl
    print(pl.pie(ssn, labels=name))
    pl.show()


def sdwpd():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    cursor.execute("select disease, bill from patient where bill!='None' group by disease")
    data = cursor.fetchall()
    ssn = []
    name = []
    for row in data:
        name.append(row[0])
        ssn.append(row[-1])
    print('Distinct disease:', ssn)
    import matplotlib.pyplot as pl
    print(pl.pie(ssn, labels=name))
    pl.show()


def dpd():
    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    cursor.execute("select doctor, count(bill) from patient where bill!='None' group by doctor")
    data = cursor.fetchall()
    ssn = []
    name = []
    for row in data:
        name.append(row[0])
        ssn.append(row[-1])
    print('Distinct disease:', ssn)
    import matplotlib.pyplot as pl
    print(pl.pie(ssn, labels=name))
    pl.show()


if __name__ == "__main__":
    dpd()