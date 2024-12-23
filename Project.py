import random
from datetime import *
import mysql.connector as mc
import csv
import os

#Create Table and Database Functions
def table():
    mydb=mc.connect(host='localhost',user='root',passwd='amity',database='hotel')
    mc1=mydb.cursor()
    mc1.execute('create table booking(Customer_ID int primary key,Name varchar(1000),Address varchar(1000), Phone_No int(100),\
                Room_Type varchar(100), Price int, Room_No int, No_of_Days int,Restaurant_Charges int,Payment_Status varchar(100),\
                Check_In_Date date, Check_Out_Date date, Adhaar_No varchar(12), Food_Items varchar(100));')
    mydb.close()

def database():
    mydb=mc.connect(host='localhost',user='root',passwd='amity')
    mc1=mydb.cursor()
    mc1.execute('create database hotel;')
    mydb.close()
   
def room():
    print(" ")
    print("BOOKING ROOMS")
    print(" ")
    while True:
        n = input("Name: ")
        l=[]
        for i in n.split():
            l.append(i)
        if n!="" and all(x.isalpha() or x.isspace() for x in n):       #Checks input of name
            break
        else:
            print('Please enter correct Name')
            print()
            continue
    while True:
        p1 = input("Phone No.: ")
        if p1!="" and p1.isdigit() and len(p1)==10:       #Checks input of number
            break
        else:
            print('Please enter correct Phone Number')
            print()
            continue
    while True:
        add = input("Address: ")
        if add!="":
            break
        else:
            print('Please enter correct Address')        #Checks if address is empty or not
            print()
            continue
    while True:
        adh = input("Enter Adhaar No.: ")                   #Checks adhaar no. conditions
        if adh!="" and adh.isdigit() and len(adh)==12:
            break
        else:
            print('Please enter correct Adhaar Number')
            print()
            continue
    print()
    print("----SELECT ROOM TYPE----")
    print(" 1. Standard Non-AC")
    print(" 2. Standard AC")
    print(" 3. 3-Bed Non-AC")
    print(" 4. 3-Bed AC")
    print(("Press 0 for Room Prices"))
    while True:
        ch=input("-> ")
        if ch=='0':
            print(" 1. Standard Non-AC - Rs. 3500/day")
            print(" 2. Standard AC - Rs. 4000/day")
            print(" 3. 3-Bed Non-AC - Rs. 4500/day")
            print(" 4. 3-Bed AC - Rs. 5000/day")
            print()
            print("----SELECT ROOM TYPE----")
            print(" 1. Standard Non-AC")
            print(" 2. Standard AC")
            print(" 3. 3-Bed Non-AC")
            print(" 4. 3-Bed AC")
            print(("Press 0 for Room Prices"))
            continue
        elif ch=='1':
            print("Room Type- Standard Non-AC")
            print("Price- 3500/day")
            rt='Standard Non-AC'
            rp=3500
            break
           
        elif ch=='2':
            print("Room Type- Standard AC")
            print("Price- 4000/day")
            rt='Standard Non-AC'
            rp=4000
            break
           
        elif ch=='3':
            print("Room Type- 3-Bed Non-AC")
            print("Price- 4500/day")
            rt='Standard Non-AC'
            rp=4500
            break
           
        elif ch=='4':
            print("Room Type- 3-Bed AC")
            print("Price- 5000/day")
            rt='Standard Non-AC'
            rp=5000
            break
             
        else:
            print(" Please enter correct choice")
            continue
            print()
   
   
    while True:
        cind=input('Enter Check-in Date with "-" in between (DD-MM-YYYY): ')
        try:                                                                     #Checks date conditions like after today, input etc
            current=datetime.today()
            d2,m,y=cind.split('-')
            datetime(int(y), int(m), int(d2))
            if datetime(int(y), int(m), int(d2))>current:
                a=datetime(int(y), int(m), int(d2))
                pass
            else:
                1/0
            break
        except:
            print('Please enter correct check-in date')
            print()
            continue
    while True:
        coutd=input('Enter Check-out Date with "-" in between (DD-MM-YYYY): ')
        try:                                                                      #Checks if date is correct
            d3,m1,y1=coutd.split('-')
            datetime(int(y1), int(m1), int(d3))
            b=datetime(int(y1), int(m1), int(d3))
            c=b-a
            c=str(c)
            c=c.split(' ')
            c=int(c[0])
            if c > 0:                                                         #Checks if date is after check in
                print('Number of days: ',c)
            else:
                1/0
            break
        except:
            print('Please enter correct check-out date')
            print()
            continue
    mydb=mc.connect(host='localhost',user='root',passwd='amity',database='hotel')           #Add all details in sql table
    mc1=mydb.cursor()
    rn = random.randrange(301)
    cid = random.randint(1000,9999)
    mc1.execute('select * from booking;')
    myr=mc1.fetchall()
    l=[]
    l1=[]
    for x in myr:
        l.append(x)
    for i in l:
        l1.append(i[0])
    if cid in l1:                                                                                                 #Checks if customer id and room no is already in table
         rn = random.randrange(301)
         cid = random.randint(1000,9999)
    t=(cid,n,add,p1,rt,rp,rn,c,0,'Unpaid',a,b,adh,'No order till now')
    q='insert into booking values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    mc1.execute(q,t)
    mydb.commit()
    mydb.close()
    print("")
    print("***ROOM BOOKED SUCCESSFULLY***")
    print("Room No. - ",rn)
    print("Customer Id - ",cid)
    print("Total Room Cost - ",c*rp)
    print('')
    print("DISCLAIMER -> Booking will be confirmed ONLY when final BILL is PAID")
    print('')
    print('------------------------------------------------------------------------------')
    home()


def info():
    print("------ HOTEL ROOMS INFO ------")
    print("")
    print("STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water.\n")
    print("STANDARD AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water + Window/Split AC.\n")
    print("3-Bed NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
    print("Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water.\n")
    print("3-Bed AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water + Window/Split AC.\n\n")
    print()
    n=input('Press enter to go back\n')
    home()


def menu():
    a=input('Are you staying at the hotel ? (Y/N) : ')
    if a in ('N','n'):
        print('Sorry, but our restaurant is only available booked guests in our hotel')
        print()
        home()
    elif a in ('Y','y'):
        mydb=mc.connect(host='localhost',user='root',passwd='amity',database='hotel')
        mc1=mydb.cursor()
        mc1.execute('select * from booking;')
        myr=mc1.fetchall()
        l=[]
        l1=[]
        for x in myr:
            l.append(x)
        for i in l:                                                                  #Takes customer id values from sql
            l1.append(i[0])                                            
        ph=input("Customer Id: ")
        if ph.isdigit():
            if int(ph) in l1:
                Q='select Payment_Status from booking where Customer_ID=%s;'
                T=(ph,)
                mc1.execute(Q,T)
                for y in mc1:
                    status=y[0]                                              #Takes only payment status value from sql
                if status=='Unpaid':
                    q='select Restaurant_Charges from booking where Customer_ID=%s;'
                    q1='select Food_Items from booking where Customer_ID=%s;'
                    t=(ph,)
                    mc1.execute(q,t)
                    for x in mc1:
                        r=x[0]                                                        #Takes only rest. id value from sql
                    t=(ph,)
                    mc1.execute(q1,t)
                    for x in mc1:
                        f=x[0]
                    if f == 'No order till now':
                        f=''
                    else:
                        pass
                    print("Disclaimer: All selected food items are for LUNCH ONLY and SAME items will be provided EVERYDAY for the whole duration")
                    print("If you disagree please press 0 to exit")
                    print("-------------------------------------------------------------------------")
                    print("                           Hotel Monark")
                    print("-------------------------------------------------------------------------")
                    print("                            Menu Card")
                    print("-------------------------------------------------------------------------")
                    print(" 1  Regular Tea............. 20")
                    print(" 2  Masala Tea.............. 25")
                    print(" 3  Coffee.................. 25 ")
                    print(" 4  Cold Drink.............. 25")
                    print(" 5  Bread Butter............ 30")
                    print(" 6  Bread Jam............... 30")
                    print(" 7  Veg. Sandwich........... 50")
                    print(" 8  Veg. Toast Sandwich..... 50")
                    print(" 9  Cheese Toast Sandwich... 50")
                    print(" 10 Grilled Sandwich........ 50")
                    print(" 11 Tomato Soup............ 60")
                    print(" 12 Hot & Sour............. 60.")
                    print(" 13 Veg. Noodle Soup....... 60")
                    print(" 14 Sweet Corn............. 60")
                    print(" 15 Veg. Munchow........... 60")
                    print(" 16 Aloo Puri............. 60")
                    print("Press 0 -to end ")
                    while 1:
                        b=int(input(" -> "))
                        if b==1:
                            rs=20
                            r=r+rs
                            f=f+'1,'
                        elif b==2:
                            rs=25
                            r=r+rs
                            f=f+'2,'
                        elif b==3:
                            rs=25
                            r=r+rs
                            f=f+'3,'
                        elif b==4:
                            rs=25
                            r=r+rs
                            f=f+'4,'
                        elif b==5:
                            rs=30
                            r=r+rs
                            f=f+'5,'
                        elif b==6:
                            rs=30
                            r=r+rs
                            f=f+'6,'
                        elif b==7:
                            rs=50
                            r=r+rs
                            f=f+'7,'
                        elif b==8:
                            rs=50
                            r=r+rs
                            f=f+'8,'
                        elif b==9:
                            rs=50
                            r=r+rs
                            f=f+'9,'
                        elif b==10:
                            rs=50
                            r=r+rs
                            f=f+'10,'
                        elif b==11:
                            rs=60
                            r=r+rs
                            f=f+'11,'
                        elif b==12:
                            rs=60
                            r=r+rs
                            f=f+'12,'
                        elif b==13:
                            rs=60
                            r=r+rs
                            f=f+'13,'
                        elif b==14:
                            rs=60
                            r=r+rs
                            f=f+'14,'
                        elif b==15:
                            rs=60
                            r=r+rs
                            f=f+'15,'
                        elif b==16:
                            rs=60
                            r=r+rs
                            f=f+'16,'

                        elif b==0:
                            break
                        else:
                            print("Wrong Choice")
                    if len(f)==0:
                        f='No order till now'
                    print("Total bill of food: ",r)
                    t=(r,int(ph))                                                                                                   #Updates rest charcges in sql to new value+prev value
                    q='update booking set Restaurant_Charges=%s where Customer_ID=%s'
                    mc1.execute(q,t)
                    mydb.commit()
                    t=(f,int(ph))
                    q='update booking set Food_Items=%s where Customer_ID=%s'
                    mc1.execute(q,t)
                    mydb.commit()
                    mydb.close()
                    n=input('Press enter to go back\n')
                    home()
                else:
                    print('Payment has already been made for given Customer ID')
                    print()
                    home()
            else:
                print('Please enter correct Customer ID')
                print()
                home()
        else:
                print('Please enter correct Customer ID')
                print()
                home()
    else:
        print('Please enter correct option')
        print()
        home()

def pay():
    mydb=mc.connect(host='localhost',user='root',passwd='amity',database='hotel')
    mc1=mydb.cursor()
    mc1.execute('select * from booking;')
    myr=mc1.fetchall()
    l=[]
    l1=[]
    for x in myr:
        l.append(x)
    for i in l:
        l1.append(i[0])                                                       #Takes customer id values from sql
    c=input("Customer Id: ")
    if c.isdigit():
        if int(c) in l1:
            q='select * from booking where Customer_ID=%s;'                            
            t=(c,)
            mc1.execute(q,t)
            for x in mc1:                                                               #Takes various values from sql for final bill
                p=x[9]                                                                     #Checks payment status
                name=x[1]
                pn=x[3]
                add=x[2]
                rt=x[4]
                nd=x[7]
                ndt=x[5]*x[7]
                rn=x[6]
                rc=x[8]
                fi=x[13]
                total=x[5]*x[7]+x[8]
            print(" Payment Status: ",p)
            if p=='Unpaid':
                while True:
                    print(" --------------------------------")
                    print("  MODE OF PAYMENT")
                    print("  1- Paytm/PhonePe")
                    print("  2- Cash during Check-In")
                    x=int(input("-> "))
                    if x in (1,2):
                        break
                    else:
                        continue
                if x==1:
                    while True:
                        p1 = input("Paytm/PhonePe - Phone No.: ")
                        if p1!="" and p1.isdigit() and len(p1)==10:
                            break
                        else:
                            print('Please enter correct Phone Number')
                            print()
                            continue
                print(" --------------------------------")
                print("           Hotel Monark Bill")
                print(" Name: ",name,"\n Phone No.: ",pn,"\n Address: ",add)
                print("Room Type: ",rt,"\n Room Charges for ",nd,' days is: ',ndt,"\n Room Number: ",rn)
                print(" Restaurant Charges: ",rc)
                print('Ordered items - ',fi,' (Please refer to list below)')
                print('Food Items list :')
                print(" 1 - Regular Tea, 2 - Masala Tea,3 - Coffee, 4 - Cold Drink, 5 - Bread Butter, 6 - Bread Jam, 7 - Veg. Sandwich, 8 - Veg. Toast Sandwich")
                print(" 9 - Cheese Toast Sandwich, 10 - Grilled Sandwich, 11 - Tomato Soup, 12 - Hot & Sour, 13 - Veg. Noodle Soup, 14 - Sweet Corn, 15 - Veg. Munchow, 16 - Aloo Puri")
                print(" --------------------------------")
                print("Grand Total: ",total)
                print()
                print("Thank You")
                print(" --------------------------------")
                mydb=mc.connect(host='localhost',user='root',passwd='amity',database='hotel')
                mc1=mydb.cursor()
                t=('Paid',c)
                q='update booking set Payment_Status=%s where Customer_ID=%s'
                mc1.execute(q,t)
                mydb.commit()
                mydb.close()
            else:
                print("Payment has already been made")
        else:
            print("Invalid Customer Id")
            print()
            home()
    else:
        print("Invalid Customer Id")
        print()
        home()
    n=input('Press enter to go back\n')
    home()


def record():
    ch=input('Password: ')              #Password is digit 0
    if ch=='0':
        mydb=mc.connect(host='localhost',user='root',passwd='amity',database='hotel')
        mc1=mydb.cursor()
        mc1.execute('select * from booking')
        mc2=mc1.fetchall()
        l=[]
        last=[]
        notlast=[]
        space=[]
        l1=['S.No.','Customer Id','Name','Address',                                                    #Headings
            'Phone No.','Room Type','Room Price','Room No.',
            'No. of Days','Rest. Charges','Payment Status',
            'Check-In Date','Check-Out Date','Adhaar No.', 'Food Items']
        record=[]
        for i in mc2:
            i=list(i)
            l.append(i)
        x=len(l)
        for i in range(1,x+1):                                                                                    #For adding Serial No to table
                l[i-1].insert(0,i)  
        l.insert(0,l1)
        with open('Record.csv','w',newline='') as f:                                                #Writes a new csv file every time
            data=csv.writer(f)
            data.writerows(l)
            location=os.getcwd()                                                                                #Gets directory where csv file is in
            f.close()
        with open('Record.csv','r') as f:                                                                   #To read csv file
            data=csv.reader(f)
            for i in data:
                record.append(i)
        for i in record[-1]:
            i=str(i)
            i=i+'\n'
            last.append(i)
        record[-1]=last        
        for i in range(len(record[0])):
          for j in record[:-1]:
              if len(j[i])!=40:                                                                               #Imp. code that makes table in python
                    diff=40-len(j[i])
                    j[i]=j[i]+(' '*diff)+"||"
              else:
                    pass
        for i in range(len(record[0])):
          for j in record:
              print(j[i].lstrip(),end='')
        print()
        print('If table is not clear, please visit this location to get CSV file of the records')
        print(location+'\Record.csv')                                                               #Adds file name to directory to open file directly
        if len(l)==0:                                                                                            #Checks if there are no records
            print('No Records')
        n=input('Press enter to go back\n')
        home()
    else:
        print('Wrong password')
        print()
        home()
   
   
def cancel():
    mydb=mc.connect(host='localhost',user='root',passwd='amity',database='hotel')
    mc1=mydb.cursor()
    mc1.execute('select * from booking;')
    myr=mc1.fetchall()
    l=[]
    l1=[]
    for x in myr:
        l.append(x)
    for i in l:
        l1.append(i[0])                                                      #Takes customer id values from sql
    print()
    ph=input("Customer Id: ")
    q='select * from booking where Customer_ID=%s;'                            
    t=(ph,)
    mc1.execute(q,t)
    for x in mc1:
        p=x[9]
    if ph.isdigit():
        if int(ph) in l1:
            for x in l:
                if int(ph)==x[0]:
                    cind=x[10]
                    total=x[5]*x[7]+x[8]
                else:
                    pass
            current=date.today()
            try:                                                #Checks if check in date is past current date or not
                nod=(str(cind-current)).split(' ')
                nod=int(nod[0])                       #Calculates days before check in from current date
            except:
                print("Booking can't be cancelled anymore!")
                print()
                home()
            if p=='Paid':                               #Condition for refund or simple cancel
                if nod >= 10:
                    print('Total Booking Cost - ',total)
                    print('Refundable Amount for cancelling on or more than 10 days before Check-In = 80% of ',total)
                    while True:
                        print('Are you sure you want to delete your booking ? (Y/N) : ')                       #Final confirmation
                        ch=input('-> ')
                        if ch in ('N','n'):
                            home()
                        elif ch in('Y','y'):
                            q='delete from booking where Customer_ID=%s'
                            t=(ph,)
                            mc1.execute(q,t)
                            mydb.commit()
                            mydb.close()
                            print(0.8*total,' has been refunded successfully')
                            print()
                            break
                        else:
                            print('Please enter correct choice')
                            print()
                            continue
                elif nod >=5:
                    print('Total Booking Cost - ',total)
                    print('Refundable Amount for cancelling on or more than 5 days before Check-In = 50% of ',total)
                    while True:
                        print('Are you sure you want to delete your booking ? (Y/N) : ')
                        ch=input('-> ')
                        if ch in ('N','n'):
                            home()
                        elif ch in('Y','y'):
                            q='delete from booking where Customer_ID=%s'
                            t=(ph,)
                            mc1.execute(q,t)
                            mydb.commit()
                            mydb.close()
                            print(0.5*total,' has been refunded successfully')
                            print()
                            break
                        else:
                            print('Please enter correct choice')
                            print()
                            continue
                elif nod >= 1:
                    print('Total Booking Cost - ',total)
                    print('Refundable Amount for cancelling on or more than 1 day before Check-In = 0% of ',total)
                    while True:
                        print('Are you sure you want to delete your booking ? (Y/N) : ')
                        ch=input('-> ')
                        if ch in ('N','n'):
                            home()
                        elif ch in('Y','y'):
                            q='delete from booking where Customer_ID=%s'
                            t=(ph,)
                            mc1.execute(q,t)
                            mydb.commit()
                            mydb.close()
                            print('Unfortunately no amount can be refunded')
                            print()
                            break
                        else:
                            print('Please enter correct choice')
                            print()
                            continue
                   
            else:
                print('Total Booking Cost - ',total)
                while True:
                    print('Are you sure you want to delete your booking ? (Y/N) : ')
                    ch=input('-> ')
                    if ch in ('N','n'):
                        home()
                    elif ch in('Y','y'):
                        q='delete from booking where Customer_ID=%s'
                        t=(ph,)
                        mc1.execute(q,t)
                        mydb.commit()
                        mydb.close()
                        print()
                        break
                    else:
                        print('Please enter correct choice')
                        print()
                        continue
               
        else:
            print("Invalid Customer Id")
            print()
            home()
    else:
        print("Invalid Customer Id")
        print()
        home()
           
    print('Booking cancelled successfully')
    print()
    home()


def search():
    mydb=mc.connect(host='localhost',user='root',passwd='amity',database='hotel')
    mc1=mydb.cursor()
    print()
    print('Please Enter Search Criteria')
    print(' --------------------------------')
    print('1  - By Customer ID')
    print('2  - By Adhaar Number')
    print('0  - Exit to Main Menu')
    ph=input(" -> ")
    if ph in ('1','2','0'):
        if ph=='1':
            mc1.execute('select * from booking;')
            myr=mc1.fetchall()
            l=[]
            l1=[]
            for x in myr:
                l.append(x)
            for i in l:
                l1.append(i[0])                                 #Takes all customer Ids
            cid=input("Customer Id: ")
            if cid.isdigit():
                if int(cid) in l1:
                    t=(cid,)
                    mc1.execute('select * from booking where Customer_ID=%s;',t)
                    myr=mc1.fetchall()
                    l=[]
                    for i in myr:
                        l.append(i)
                   
                    n=l[0][1]                                     #All values get assigned
                    add=l[0][2]
                    phno=l[0][3]
                    rtype=l[0][4]
                    rp=l[0][5]
                    rno=l[0][6]
                    nod=l[0][7]
                    rc=l[0][8]
                    ps=l[0][9]
                    cind=l[0][10]
                    coutd=l[0][11]
                    fi=l[0][13]
                    tp=rp*nod+rc
                    print('Name - ',n)
                    print('Address - ',add)
                    print('Phone Number - ',phno)
                    print('Room Type - ',rtype)
                    print('Room Number - ',rno)
                    print('No. of Days - ',nod)
                    print('Check-In Date - ',cind)
                    print('Check-Out Date - ',coutd)
                    print('Room service - ',rc)
                    print('Ordered items - ',fi,' (Please refer to list below)')
                    print('Food Items list :')
                    print(" 1 - Regular Tea, 2 - Masala Tea,3 - Coffee, 4 - Cold Drink, 5 - Bread Butter, 6 - Bread Jam, 7 - Veg. Sandwich, 8 - Veg. Toast Sandwich")
                    print(" 9 - Cheese Toast Sandwich, 10 - Grilled Sandwich, 11 - Tomato Soup, 12 - Hot & Sour, 13 - Veg. Noodle Soup, 14 - Sweet Corn, 15 - Veg. Munchow, 16 - Aloo Puri")
                    print('Payment Satus - ',ps)
                    if ps=='Unpaid':
                        print('Please pay grand total of ',tp,' to confirm booking')
                    else:
                        pass  
                    search()
                else:
                    print('Invalid Customer ID')
                    search()
            else:
                print('Invalid Customer ID')
                search()

        elif ph=='2':
            mc1.execute('select * from booking;')
            myr=mc1.fetchall()
            l=[]
            l1=[]
            for x in myr:
                l.append(x)
            for i in l:
                l1.append(i[12])                                      #Takes all adhaar nos.
            adn=input("Adhaar No.: ")
            if adn.isdigit():
                if adn in l1:
                    t=(adn,)
                    mc1.execute('select * from booking where Adhaar_No=%s;',t)
                    myr=mc1.fetchall()
                    l=[]
                    for i in myr:
                        l.append(i)
                       
                    cid=l[0][0]                                     #All values get assigned
                    n=l[0][1]
                    add=l[0][2]
                    phno=l[0][3]
                    rtype=l[0][4]
                    rp=l[0][5]
                    rno=l[0][6]
                    nod=l[0][7]
                    rc=l[0][8]
                    ps=l[0][9]
                    cind=l[0][10]
                    coutd=l[0][11]
                    fi=l[0][13]
                    tp=rp*nod+rc
                    print('Customer ID - ',cid)
                    print('Name - ',n)
                    print('Address - ',add)
                    print('Phone Number - ',phno)
                    print('Room Type - ',rtype)
                    print('Room Number - ',rno)
                    print('No. of Days - ',nod)
                    print('Check-In Date - ',cind)
                    print('Check-Out Date - ',coutd)
                    print('Room service - ',rc)
                    print('Ordered items - ',fi,' (Please refer to list below)')
                    print('Food Items list :')
                    print(" 1 - Regular Tea, 2 - Masala Tea,3 - Coffee, 4 - Cold Drink, 5 - Bread Butter, 6 - Bread Jam, 7 - Veg. Sandwich, 8 - Veg. Toast Sandwich")
                    print(" 9 - Cheese Toast Sandwich, 10 - Grilled Sandwich, 11 - Tomato Soup, 12 - Hot & Sour, 13 - Veg. Noodle Soup, 14 - Sweet Corn, 15 - Veg. Munchow, 16 - Aloo Puri")
                    print('Payment Satus - ',ps)
                    if ps=='Unpaid':
                        print('Please pay grand total of ',tp,' to confirm booking')
                    else:
                        pass
                    search()
                else:
                    print('Invalid Adhaar No.')
                    search()
            else:
                print('Invalid Adhaar No.')
                search()
        else:
            print()
            home()
           
    else:
        print('Please enter correct option')
        search()
   
def home():
    try:                                                       #Creates database and table if they dont exist already
        database()
        table()
    except:
        pass
    print("WELCOME TO HOTEL MONARK")
    print("1  - Booking")
    print("2  - Rooms Info")
    print("3  - Menu Card")
    print("4  - Payment")
    print("5  - Record")
    print("6  - Cancel your Booking")
    print("7  - Search")
    print("0  - Exit")
    ch=input("-> ")
    if ch == '1':
        room()
             
    elif ch == '2':
        info()
   
    elif ch == '3':
        menu()
           
    elif ch == '4':
        pay()
       
    elif ch == '5':
        record()

    elif ch == '6':
        cancel()
       
    elif ch == '7':
        search()
       
    elif ch == '0':
        return
   
    else:
        print("Please enter correct choice")
        print()
        home()

home()