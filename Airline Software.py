#simple app

from tkinter import *
import math
import sys
import tkinter.messagebox

import gspread
from oauth2client.service_account import ServiceAccountCredentials


session=0
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Charity-Donators-052dc76e6d4e.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Donators').sheet1
donators = sheet.get_all_records()



#APP
gui=Tk()
gui.geometry("600x420+200+200")
Tops=Frame(gui,width=100,height=20,bd=4,relief="raise")
Tops.grid(row=4, column=1)
gui.title("DESTINATION AIRLINES")
mlabel=Label(text="DESTINATION AIRLINES",fg="red",bg="white").grid(row=0, column=1)



row = []
rte=sheet.col_values(4)

rte.pop(0)
session=0

for i in range(0,len(rte)):
    session=session+1
session=session+1
print("Your current session ID is #"+str(session))

seats=152
if session>1:
    seats=sheet.col_values(8)
    seats=int(seats[-1])
    
print(seats)

def calculation():
    p=sheet.col_values(6)
    totalch=0
    p.pop(0)
    for i in range (0,len(p)):
        totalch=totalch + int(p[i])
    children=childt.get()
    adults=adultt.get()
    
    totch=chidren*60
    totad=adults*120
    total=totad+totch
    global seats
    if seats-(children+adults)<0:
        print("Sorry, but there are not enough seats on this plane for that many people")
    else:
        seats=seats-(children+adults)
    
    row.append(name.get())
    row.append(adultt.get())
    row.append(childt.get())
    row.append(totad)
    row.append(session)
    row.append(totch)
    row.append(total)
    row.append(seats)
    row.append(usernamee.get())
    row.append(passworrd.get())
    sheet.insert_row(row, session+1)
    tkinter.messagebox.showinfo("Cost","Total cost for tickets = "+str(totalch))
    gui.destroy()
    print("The results can be viewed at: https://docs.google.com/spreadsheets/d/16dQYMSsqWlipyiZz3tePlmFrBKVhQlC9Lvgp_2pg-Ko/edit?usp=sharing")
    return


def helpmenu():
    helpmenu=Tk()
    helpmenu.geometry("1200x1200+500+500")
    helpmenu.title("HELPMENU")
    info=Label(helpmenu, text="""Welcome to the helpmenu!! \n The purpose of this code is to input data and store it in a excel spreadsheet file. The data is for a airline companies and people are buying tickets for flights. 
                  Inputs are string and variable only. There are no possible inputs for float values.
                  \nPLEASE MAKE SURE TO HAVE AN ACTIVE INTERNET CONNECTION.
                  \nPossible errors include inputting float values for child tickets, this should always be a POSITIVE INTEGER!
                  \nPrices are as follows:
                  \nPrice for and adult ticket:	£120
                  \nPrice for a child ticket:	£60""")

    info.pack()
    helpmenu.mainloop()
    

    
name=StringVar()
childt=IntVar()
adultt=IntVar()
usernamee=StringVar()
passworrd=StringVar()


scale=Scale(gui,variable=childt, orient=HORIZONTAL)
scale2=Scale(gui,variable=adultt, orient=HORIZONTAL)
scale.grid(column=1, row=7)
scale2.grid(column=1, row=8)


label=Label(gui)
label.grid(column=3, row=3)

#LABELS
mlabel1=Label(text="FULL NAME",fg="red",bg="cyan").grid(row=1, column=0)

mlabe2=Label(text="CHILD TICKETS",fg="red",bg="cyan").grid(row=2, column=0)

mlabe3=Label(text="ADULT TICKETS",fg="red",bg="cyan").grid(row=3, column=0)

mlabe4=Label(text="USERNAME",fg="red",bg="cyan").grid(row=4, column=0)

mlabe5=Label(text="PASSWORD",fg="red",bg="cyan").grid(row=5, column=0)


#ENTRIES
Name=Entry(gui,font=("arial", 18,"bold"),textvariable=name, width=21, bd=4, justify="left")
Name.grid(row=1, column=1)

childticks=Entry(gui,font=("arial", 18,"bold"),textvariable=childt, width=21, bd=4, justify="left")
childticks.grid(row=2, column=1)

adultticks=Entry(gui,font=("arial", 18,"bold"),textvariable=adultt, width=21, bd=4, justify="left")
adultticks.grid(row=3, column=1)

username=Entry(gui,font=("arial", 18,"bold"),textvariable=usernamee, width=21, bd=4, justify="left")
username.grid(row=4, column=1)

password=Entry(gui,font=("arial", 18,"bold"),textvariable=passworrd, width=21, bd=4, justify="left")
password.grid(row=5, column=1)


#BUTTONS
mbutton=Button(gui,text="CALCULATE THE WAGE", command=calculation).grid(row=8, column=0)
mbutton2=Button(gui,text="cancel", command=gui.destroy).grid(row=7, column=0)
button1=Button(gui, text="HELP MENU", command=helpmenu).grid(column=3, row=2)

tkinter.messagebox.showinfo("WARNING","PLEASE MAKE SURE TO HAVE A ACTIVE INTERNET CONNECTION!")


gui.mainloop()
