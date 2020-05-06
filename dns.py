#!/usr/bin/python3
import socket
from tkinter import *
import tkinter as tk

m = tk.Tk()
m.configure(bg='#372081')
m.title("DNS Resolver by SH1ELD TECH INFOSEC SOLUTIONS PVT. LTD.")
m.geometry('500x500+500+300')
photo = PhotoImage(file='/root/shield/index.png')
label = Label(m, image=photo).place(x=95,y=40)
inp = StringVar()
addr = StringVar()

def resolve(event=None):
	a = inp.get()
	try:
		addr = socket.gethostbyname(a) 
		g = Label(m, text="" + addr,width=30).place(x=180,y=321)
	except socket.gaierror:
		h = "There was an Error Resolving Host"
		g = Label(m, text="" + h,width=30).place(x=180,y=321)

a = Label(m, text="Enter Hostname:").place(x=60,y=262)
e = Entry(m, bd=3, width=30, textvariable=inp).place(x=180,y=260)
b = Label(m, text="IP Address:").place(x=95,y=320)
c = Button(m, text ="Submit", command=resolve).place(x=220,y=380)
m.bind('<Return>',resolve)
m.mainloop()









