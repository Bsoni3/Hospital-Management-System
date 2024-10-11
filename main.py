import mysql.connector as co

hostname = 'localhost'
username = 'root'
password = 'rajmahal151'
database = 'sjh'

print("\t\t-------------------------------------------------")
print("\t\t*******Welcome to Hospital Management System*******")
print("\t\t-------------------------------------------------")
print("\n\t\t*******Shri Jain Hospital - M A I N  M E N U*******")
print("\t\t-------------------------------------------------")
print('')
print('')
print('')
print("Your'nt LOGGED IN yet, PLEASE LOGIN first")

login=False
while not login:
    name = input("Enter UserName: ")
    passw = input("Enter Password: ")

    mycon = co.connect(host=hostname, user=username, passwd=password, db=database)
    cursor = mycon.cursor()
    cursor.execute("select * from user where name='%s' and password='%s'" % (name, passw))
    data = cursor.fetchone()
    if data:
        import main_menu
    print("\t\t-------------------------------------------------")
    print("USERNAME/PASSWORD Invalid! Try Again")

    cursor.close()
    mycon.commit()
    mycon.close()



