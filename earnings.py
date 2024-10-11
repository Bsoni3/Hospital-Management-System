import datetime
import random
from tabulate import tabulate
import cases
import mysql.connector as co

hostname = 'localhost'
username = 'root'
password = 'rajmahal151'
database = 'sjh'


def ERN_MENU():
    while True:
        print("\t\t-------------------------------------------------------------------------")
        print("\t\t*******Welcome to Hospital Management System*******")
        print("\t\t-------------------------------------------------------------------------")
        print("\n\t\t * * ** E A R N I N G S  M E N U   * * ** ")
        print("\t\t-------------------------------------------------------------------------")
        print("\t\t-------------------------------------------------------------------------")

        mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
        cursor = mycon.cursor()
        cursor.execute("select * from patient where recovery_date!=''")
        data = cursor.fetchall()

        patient_data = [[]]

        for row in data:
            patient_data.append([row[0], row[1],row[10],(datetime.datetime.strptime(row[9], "%Y-%m-%d") - datetime.datetime.strptime(row[8], "%Y-%m-%d")).days,row[5], row[6], row[9]])
        print(tabulate(patient_data,
                       headers=['Admin_NO', 'Name', 'Total Bill','Stay(Days)','Disease', 'Doctor', 'Recovered_Date']))

        return
