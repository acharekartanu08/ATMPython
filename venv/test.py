from tkinter import *

class ATM:
    def insertpin():
        conn = m.connect(host="localhost", user="root", password="Tanu@81296", database="demo")
        cur = conn.cursor()
        pin=int(ce1.get())
        p = "select * from bank_details"
        cur.execute(p)
        r1 = cur.fetchall()
        for j in r1:
            if (pin == j[1]):
                atm.profile()
            else:
                messagebox.askokcancel("message", "Please enter valid PIN number.")

    def maina(self):
        global e1,win
        win=Tk()
        win.title("ATM")
        win.geometry("400x400")
        l1=Label(win,text="Welcome to ATM")
        l1.place(x=80,y=50)
        l2=Label(win,text="Card Number:")
        l2.place(x=50,y=120)
        e1 = Entry(win, width=15)
        e1.place(x=150, y=120)
        b1=Button(win,text="insert card")
        b1.place(x=160,y=160)

        win.mainloop()

a = ATM()
a.maina()