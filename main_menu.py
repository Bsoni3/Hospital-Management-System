# -*- coding: utf-8 -*-
import main_menu
import sys
import patient
import dr_data
import disease
import report
import cases
import employees
import earnings
while True:
    #main_menu.clrscreen()
    print("\t\t-------------------------------------------------")
    print("\t\t*******Welcome to Hospital Management System*******")
    print("\t\t-------------------------------------------------")
    print("\n\t\t*******Shri Jain Hospital - M A I N  M E N U*******")
    print("1 :  Patient Admission & Details")
    print("2 :  Doctor Admission & Details")
    print("3 :  Disease & Details")
    print("4 :  Pending Cases ")
    print("5 :  Earnings ")
    print("6 :  Manage Employees ")
    print("7 :  Graphical Details ")
    print("8 :  Exit")
    print("\t\t-------------------------------------------------")
    choice=int(input("Enter Your Choice :"))
    if choice==1:
        patient.ADM_MENU()
    elif choice==2:
        dr_data.DR_MENU()
    elif choice==3:
        disease.DSE_MENU()
    elif choice==4:
        cases.CASES_MENU()
    elif choice==5:
        earnings.ERN_MENU()
    elif choice==6:
        employees.EMP_MENU()
    elif choice==7:
        report.gr_rep()
    elif choice==8:
        sys.exit(0)
    else:
        print("Error: Invalid Choice try again......")
        conti=input("press any key to continue")

        
    
