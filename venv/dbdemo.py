from tkinter import *
import mysql.connector as m

conn = m.connect(user="root",password="Tanu@81296",host="localhost")

cur = conn.cursor()

q = "create database Bank"

cur.execute(q)
conn.close()