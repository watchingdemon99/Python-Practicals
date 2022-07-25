import mysql.connector
import tabulate as tab
from datetime import date


def ShowAll():
    cur.execute("SELECT * FROM PROJECT")
    data1 = cur.fetchall()
    cur.execute("DESC PROJECT")
    wheader = cur.fetchall()
    header = []
    for i in wheader:
        header.append(i[0])
    print(tab.tabulate(data1, headers=header))


def NameandAge():
    cur.execute("SELECT FIRST_NAME,MIDDLE_NAME,LAST_NAME,DOB FROM PROJECT")
    data2 = cur.fetchall()
    age = []
    data3 = []
    tdays = 365.2425
    for i in data2:
        age.append(int((date.today() - i[3]).days / tdays))
        data3.append(i[0] + " " + i[1] + " " + i[2])
    data4 = []
    for j in range(len(age)):
        data4.append((data3[j], age[j]))
    print(tab.tabulate(data4, headers=["NAME", "AGE"]))


def AddUser():
    prn = int(input("Input PRN:- "))
    fname = input("Input First Name:- ").upper()
    mname = input("Input Middle Name:- ").upper()
    lname = input("Input Last Name:- ").upper()
    tadrs = input("Input Address:- ").upper()
    mnum = int(input("Input Phone Number:- "))
    email = input("Input Email Id:- ").upper()
    dob = input("Input DOB in yyyy-mm-dd Format")
    cur.execute(
        "INSERT INTO PROJECT VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(prn, fname, mname, lname, tadrs,
                                                                                     mnum, email, dob))
    cnct.commit()
    ShowAll()


def DeleteUser():
    prn1 = int(input("Input PRN to delete records:- "))
    cur.execute("DELETE FROM PROJECT WHERE PRN='{}'".format(prn1))
    cnct.commit()


def UpdateUser():
    prn2 = int(input("Input PRN to update phone number and e-mail address"))
    mnum2 = int(input("Enter new mobile number"))
    email2 = input("Enter new email")
    cur.execute("UPDATE PROJECT SET MOBILE_NUMBER='{}',E_MAIL='{}' WHERE PRN='{}'".format(mnum2, email2, prn2))
    cnct.commit()
    ShowAll()


def AddColumCGPA():
    cur.execute("SELECT PRN FROM PROJECT")
    data4 = cur.fetchall()
    cur.execute("ALTER TABLE PROJECT ADD CGPA FLOAT")
    cnct.commit()
    for i in data4:
        x = len(str(i))
        i = list(i)
        fcgpa = float(input("Enter CGPA sequentially:- "))
        i = i[0:x - 1]
        cur.execute("UPDATE PROJECT SET CGPA='{}' WHERE PRN='{}'".format(fcgpa, i[0]))
        cnct.commit()
    ShowAll()


cnct = mysql.connector.connect(host="localhost", username="root", password="Leanest@0", database="PROJECT")
cur = cnct.cursor()
flag = True
disp = "Welcome to the Dr.Babasaheb Ambedkar Technological University's Database.\nPlease enter the number of the choice with which you want to proceed.\n1.Show Name and Age of all Students.\n2.Add a new student in database.\n3.Delete records of a student.\n4.Update/Change Mobile Number and Email of Student.\n5.Add CGPA of every student.\n6.Show all the details on database.\nx.Exit NOTE:- To exit press small letter x"
choice = "0"
while choice != "x":
    print(disp)
    choice = input("Enter your choice")
    if choice == "1":
        NameandAge()
    elif choice == "2":
        AddUser()
    elif choice == "3":
        DeleteUser()
    elif choice == "4":
        UpdateUser()
    elif choice == "5":
        AddColumCGPA()
    elif choice == "6":
        ShowAll()
    elif choice == "x":
        pass
    else:
        print("Please Enter a valid choice")
