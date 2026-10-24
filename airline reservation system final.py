print("---------AIRLINE RESERVATION SYSTEM------------")
import os
import platform
import mysql.connector
# Establishing the database connection
mydb = mysql.connector.connect(host="localhost", user="root", passwd="161916", database='airplane', charset="utf8")
mycursor = mydb.cursor()

def registercust():
    L = []
    custno = int(input('Enter customer no: '))
    L.append(custno)
    name = input('Enter name: ')
    L.append(name)
    addr = input('Enter address: ')
    L.append(addr)
    jr_date = input('Enter date of journey(YYYY-MM-DD): ')
    L.append(jr_date)
    destination = input('Enter destination: ')
    L.append(destination)
    cust = tuple(L)
    sql = 'INSERT INTO pdata(custno, custname, addr, jrdate, destination) VALUES (%s, %s, %s, %s, %s)'
    mycursor.execute(sql, cust)
    mydb.commit()

def ticketprice():
    L = []
    cno = int(input('Enter customer no: '))
    L.append(cno)

    print('We have the following classes for you:')
    print('1. First class--->Rs.6000/ per person')
    print('2. Business class--->Rs.4000/ per person')
    print('3. Economy class--->Rs.2000/ per person')

    x = int(input('Enter your choice: '))
    n = int(input('Enter No.of Passengers: '))
    
    if x == 1:
        print('You have opted First class.')
        s = 6000 * n
    elif x == 2:
        print('You have opted Business class.')
        s = 4000 * n
    elif x == 3:
        print('You have opted Economy class.')
        s = 2000 * n
    else:
        print('Please select a valid class type.')
        return  # Exit the function if the choice is invalid

    L.append(s)
    print('Your ticket charge is Rs.', s, '\n')
    print('Extra luggage charge Rs.100 per kg')
    y = float(input('Enter your weight of extra luggage(in kgs): '))
    z = y * 100
    L.append(z)
    tkt = tuple(L)
    print('Your Total bill is:', s + z, '\n')
    g_tot = s + z
    L.append(g_tot)
    sql = "INSERT INTO tkt (custno, tkt_tot, lug_tot, g_tot) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql, tkt)
    mydb.commit()

def dis():
    custno = int(input("Enter the customer number whose bill to be viewed: "))
    sql = "SELECT pdata.custno, pdata.custname, pdata.addr, pdata.destination, tkt.tkt_tot, tkt.lug_tot, g_tot FROM pdata INNER JOIN tkt ON pdata.custno = tkt.custno WHERE tkt.custno = %s"
    rl = (custno,)
    mycursor.execute(sql, rl)
    res = mycursor.fetchall()
    for x in res:
        print(x)

def dispall():
    sql = "SELECT pdata.custno, pdata.custname, pdata.addr, pdata.destination, tkt.tkt_tot, tkt.lug_tot, g_tot FROM pdata INNER JOIN tkt ON pdata.custno = tkt.custno"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    print("The Customer details are as follows:")
    for x in res:
        print(x)

def Menuset():
    print('Enter 1: To enter customer data.')
    print('Enter 2: For ticket amount.')
    print('Enter 3: Display customer-wise Details.')
    print('Enter 4: Display All Details.')
    print('Enter 5: Exit')
    userinput = int(input('Enter your choice: '))
    if userinput == 1:
        registercust()
    elif userinput == 2:
        ticketprice()
    elif userinput == 3:
        dis()
    elif userinput == 4:
        dispall()
    elif userinput == 5:
        quit()
    else:
        print('Enter the correct choice.')
    Menuset()

def runagain():
    runagn = input('\nWant to run again? y/n: ')
    while runagn.lower() == 'y':  # Ensure case-insensitive comparison
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')
        Menuset()
        runagn = input('\nWant to run again? y/n: ')

Menuset()
runagain()
