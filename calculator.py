import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
t=tkinter.Tk()
t.geometry('800x500')
t.title('Calculator')
def sum():
    k=int(d.get())
    h=int(d.get())
    p=k+h
    messagebox.showinfo('sum',str(p))
def mul():
    k=int(d.get())
    h=int(d.get())
    p=k*h
    messagebox.showinfo('sum',str(p))
def sub():
    k=int(d.get())
    h=int(d.get())
    p=k-h
    messagebox.showinfo('sum',str(p))
def div():
    k=int(d.get())
    h=int(d.get())
    p=k/h
    messagebox.showinfo('sum',str(p))
a=Label(t,text='Calculator',font=('arial',30),fg='black')
a.place(x=250,y=20)
b=Label(t,text='No 1',font=('arial',20))
b.place(x=60,y=120)
d=Entry(t,width=30)
d.place(x=500,y=130)
c=Label(t,text='No 2',font=('arial',20))
c.place(x=60,y=220)
f=Entry(t,width=30)
f.place(x=500,y=230)
btn=Button(t,text='*',command=mul)
btn.place(x=200,y=350)
btd=Button(t,text='-',command=sub)
btd.place(x=250,y=350)
bts=Button(t,text='+',command=sum)
bts.place(x=300,y=350)
btv=Button(t,text='/',command=div)
btv.place(x=350,y=350)
btk=Button(t,text='close')
btk.place(x=400,y=350)
t.mainloop()
