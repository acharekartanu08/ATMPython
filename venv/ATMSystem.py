from tkinter import *
import mysql.connector as my
from tkinter import messagebox
def checkb():
    con = my.connect(host="localhost", user="root", password="root", database="demo")
    cur = con.cursor()
    q="select amt from info where card=%s"%cn
    cur.execute(q)
    r=cur.fetchone()
    cblb.config(text=str(r))
    con.close()
def withwo():
    try:
        con = my.connect(host="localhost", user="root", password="root", database="demo")
        cur = con.cursor()
        q="select amt from info where card=%s"%cn
        cur.execute(q)
        r=cur.fetchone()
        if int(wde.get())<=r[0]:
            b=r[0]-int(wde.get())
        else:
            raise Exception
        q="update info set amt=%s where card=%s"
        v=(b,cn)
        cur.execute(q,v)
        con.commit()
        con.close()
        wdw.destroy()
    except ValueError:
        messagebox.showerror("Error","Enter Only Numbers")
    except Exception:
        messagebox.showerror("Error","Do not have enough balance")
        wdw.destroy()
def withdw():
    global wde,wdw
    wdw=Tk()
    wdw.geometry("300x200")
    Label(wdw,text="Enter Amount:").place(x=10,y=30)
    wde=Entry(wdw,width=25)
    wde.place(x=100,y=30)
    wdb=Button(wdw,text="WITHDRAW",command=withwo)
    wdb.place(x=120,y=70)
    wdw.mainloop()
def depo():
    try:
        con = my.connect(host="localhost", user="root", password="root", database="demo")
        cur = con.cursor()
        q="select amt from info where card=%s"%cn
        cur.execute(q)
        r=cur.fetchone()
        b=r[0]+int(de.get())
        q="update info set amt=%s where card=%s"
        v=(b,cn)
        cur.execute(q,v)
        con.commit()
        con.close()
        dw.destroy()
    except ValueError:
        messagebox.showerror("Error","Enter Only Numbers")

def depw():
    global de,dw
    dw=Tk()
    dw.geometry("300x200")
    Label(dw,text="Enter Amount:").place(x=10,y=30)
    de=Entry(dw,width=25)
    de.place(x=100,y=30)
    db=Button(dw,text="DEPOSIT",command=depo)
    db.place(x=120,y=70)
    dw.mainloop()
def chgpo():
    con = my.connect(host="localhost", user="root", password="root", database="demo")
    cur = con.cursor()
    q="update info set cpin=%s where card=%s"
    v=(int(cpe.get()),cn)
    cur.execute(q,v)
    con.commit()
    con.close()
    cpw.destroy()
    ow.destroy()

def changepw():
    global cpe, cpw
    cpw = Tk()
    cpw.geometry("300x200")
    Label(cpw, text="Enter New Pin").place(x=10, y=30)
    cpe = Entry(cpw, width=25)
    cpe.place(x=100, y=30)
    cpb = Button(cpw, text="CHANGE PIN", command=chgpo)
    cpb.place(x=120, y=70)
    cpw.mainloop()

def qt():
    ow.destroy()
    mw.destroy()
def opw():
    global cblb,ow
    ow=Tk()
    ow.geometry("300x300")
    cblb=Label(ow,text="Check Balc")
    cblb.place(x=10,y=130)
    wb=Button(ow,text="WITHDRAW",command=withdw)
    wb.place(x=200,y=40)
    dp=Button(ow,text="DEPOSIT",command=depw)
    dp.place(x=200,y=90)
    cbl=Button(ow,text="CHECK BALANCE",command=checkb)
    cbl.place(x=200,y=140)
    chp=Button(ow,text="CHANGE PIN",command=changepw)
    chp.place(x=200,y=190)
    cbt=Button(ow,text="EXIT",command=qt)
    cbt.place(x=200,y=240)
    ow.mainloop()
def valid1():
    global cn
    try:
        con=my.connect(host="localhost",user="root",password="root",database="demo")
        cur=con.cursor()
        cn=int(ecn.get())
        cp=int(ecp.get())
        q="select card,cpin from info"
        cur.execute(q)
        r=cur.fetchall()
        for i in r:
            if i[0]==cn and i[1]==cp:
                opw()
                break
        else:
            messagebox.showerror("Error","enter wrong infomation")
    except ValueError:
        messagebox.showerror("Error", "Enter only numbers")
def adduo():
    con = my.connect(host="localhost", user="root", password="root", database="demo")
    cur = con.cursor()
    q="insert into info values(%s,%s,%s)"
    v=(int(aue1.get()),int(aue2.get()),int(aue3.get()))
    cur.execute(q,v)
    con.commit()
    con.close()
    auw.destroy()
def adduw():
    global aue1,aue2,aue3,auw
    auw=Tk()
    auw.geometry("300x200")
    Label(auw,text="Enter Card Number").place(x=10,y=10)
    aue1=Entry(auw,width=15)
    aue1.place(x=150,y=10)
    Label(auw,text="Enter Card Pin").place(x=10,y=40)
    aue2=Entry(auw,width=15)
    aue2.place(x=150,y=40)
    Label(auw,text="Enter Amount").place(x=10,y=70)
    aue3=Entry(auw,width=15)
    aue3.place(x=150,y=70)

    aub=Button(auw,text="ADD USER",command=adduo)
    aub.place(x=130,y=100)
def mainw():
    global ecn,ecp,mw
    mw=Tk()
    mw.geometry("300x300")
    Label(mw,text="ATM SYSTEM").place(x=100,y=50)
    Label(mw,text="Enter Card Number").place(x=10,y=100)
    ecn=Entry(mw,width=15)
    ecn.place(x=140,y=100)
    Label(mw,text="Enter Card Pin").place(x=10,y=130)
    ecp=Entry(mw,width=15)
    ecp.place(x=140,y=130)
    mb1=Button(mw,text="SUBMIT",command=valid1)
    mb1.place(x=90,y=170)
    mb2=Button(mw,text="ADD USER",command=adduw)
    mb2.place(x=150,y=170)
    mw.mainloop()
mainw()
