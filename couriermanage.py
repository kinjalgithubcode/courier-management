from tkinter import *
from tkinter import messagebox as ms
from tkinter import ttk
import sqlite3
import random
from tkinter import Button
import tkinter

#Database

with sqlite3.connect('record123.db')as db:
    c=db.cursor()
try:
    c.execute('CREATE TABLE IF NOT EXISTS user(username TEXT NOT NULL,password TEXT NOT NULL,mobile TEXT NOT NULL);')
except:
    pass
db.commit()
db.close()

class main:
    def __init__(self,master):
        self.master=master

        self.username=StringVar()
        self.password=StringVar()
        self.n_username=StringVar()
        self.n_password=StringVar()
        self.n_reg=StringVar()
        self.n_mobile=StringVar()
        self.mobile11=StringVar()
        self.widgets()

    def login(self):

        with sqlite3.connect('record123.db')as db:
            c=db.cursor()

        #Find the correct user

        find_user=('SELECT * FROM user WHERE username=? and password=?')
        c.execute(find_user,[(self.username.get()),(self.password.get())])
        result=c.fetchall()

        if result:
            self.track1()
        else:
            ms.showerror('Oops!','Check the username again')
    def new_user(self):
        with sqlite3.connect('record123.db')as db:
            c=db.cursor()
        if self.n_username.get()!='' and self.n_password.get()!='' and self.n_mobile.get()!='':
           find_user=('SELECT * FROM user WHERE username=?')
           c.execute(find_user,[(self.n_username.get())])

           if c.fetchall():
               ms.showerror('Error!','Username is already taken.')
           else:
               insert='INSERT INTO user(username,password,mobile)VALUES(?,?,?)'
               c.execute(insert,[(self.n_username.get()),(self.n_password.get()),(self.n_mobile.get())])
               db.commit()

               ms.showinfo('Congrats!','Account Created!')
               self.log()

        else:
            ms.showerror('Error!','Please Enter the details.')

    def consignment(self):
        try:
            with sqlite3.connect('record123.db')as db:
                c=db.cursor()

            #Find user if there is any take proper action
            find_user=('SELECT * FROM user WHERE mobile=?')
            c.execute(find_user,[(self.mobile11.get())])
            result=c.fetchall()

            if result:
                self.track()
                self.crff.pack_forget()
                self.crf.pack_forget()
                self.head['text']=self.username.get()+'\n youre product Details'
                self.consi.pack()
            else:
                ms.showerror('Ooops','Mobile Number Not Found')
        except:
            ms.showerror('Oops','Mobile Number Not Found ')

    def track1(self):
        self.logf.pack_forget()
        self.consi.pack_forget()
        self.head['text']=self.username.get()+'\n Product Tracking information'
        self.crff.pack()


    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text']='Login'
        self.logf.pack()

    def create(self):
        self.n_username.set('')
        self.n_password.set('')
        self.logf.pack_forget()
        self.head['text']='Open your Account'
        self.crf.pack()

    def track(self):
        self.logf.pack_forget()
        self.head['text']=self.username.get()+'\n Tracking the Product'

        self.crf.pack()

    def widgets(self):
            self.head=Label(self.master,text='LOGIN THE PAGE',font=('Calibri',18),pady=15)
            self.head.pack()

            self.logf=Frame(self.master,padx=50,pady=50)
            self.logf.configure(background='skyblue')

            Label(self.logf,text='Username:',font=('',12),pady=4,padx=4,bg='Skyblue').grid(sticky=W)
            Entry(self.logf,textvariable=self.username,bd=3,font=('',15)).grid(row=0,column=1)
            Label(self.logf,text='Password:',font=('',12),pady=4,padx=4,bg='Skyblue').grid(sticky=W)
            Entry(self.logf, textvariable=self.password, bd=3, font=('', 15),show='*').grid(row=1, column=1)
            Button(self.logf,text='Login',background='lightgrey',bd=4,font=('',13),padx=5,pady=5,command=self.login).grid(row=12,column=0)
            Button(self.logf, text='New Registration', background='lightgrey', bd=4, font=('', 13), padx=5, pady=5,
                   command=self.create).grid(row=12, column=1)

            self.logf.pack()


            self.crf=Frame(self.master,padx=60,pady=60,bg='lightgreen')
            Label(self.crf,text='Username',font=('Calibri',15),padx=5,pady=5,bg='lightgreen').grid(sticky=W)
            Entry(self.crf,textvariable=self.n_username,bd=3,font=('',15)).grid(row=0,column=1)

            Label(self.crf, text='Password', font=('Calibri', 15), padx=5, pady=5, bg='lightgreen').grid(sticky=W)
            Entry(self.crf, textvariable=self.n_password, bd=3, font=('', 15),show='*').grid(row=1, column=1)

            Label(self.crf, text='Mobile No', font=('Calibri', 15), padx=5, pady=5, bg='lightgreen').grid(sticky=W)
            Entry(self.crf, textvariable=self.n_mobile, bd=3, font=('', 15)).grid(row=2, column=1)

            Label(self.crf, text='Registration No', font=('Calibri', 15), padx=5, pady=5, bg='lightgreen').grid(sticky=W)
            Entry(self.crf, textvariable=self.n_reg, bd=3, font=('', 15)).grid(row=3, column=1)

            Label(self.crf, text='Email Id', font=('Calibri', 15), padx=5, pady=5, bg='lightgreen').grid(sticky=W)
            Entry(self.crf, bd=3, font=('', 15)).grid(row=4, column=1)

            Label(self.crf,text='Gender:',font=('Calibri',15),padx=5,pady=5,bg='lightgreen').grid(sticky=W)
            var=IntVar()
            R1=Radiobutton(self.crf,text='Male',variable=var,value=1,bg='lightgreen').grid(row=5,column=1)
            R2 = Radiobutton(self.crf, text='Female', variable=var, value=2, bg='lightgreen').grid(row=5, column=2)


            Button(self.crf,text='Create My Account',background='lightgrey',bd=2,font=('Calibri',13),padx=8,pady=8,command=self.new_user).grid(row=11,column=0)
            Button(self.crf, text='Back to Login', background='lightgrey', bd=2, font=('Calibri', 13), padx=8,
                   pady=8, command=self.log).grid(row=11, column=2)


            self.crff = Frame(self.master, padx=80, pady=80, bg='lightgreen')

            Label(self.crff, text='Reference No:', font=('Calibri', 15), padx=5, pady=5, bg='lightgreen').grid(sticky=W)
            Entry(self.crff, bd=3, font=('Calibri', 15)).grid(row=0, column=1)

            Label(self.crff, text='Mobile No:', font=('Calibri', 15),
                  padx=5, pady=5, bg='lightgreen').grid(sticky=W)
            Entry(self.crff, bd=3, textvariable=self.mobile11, font=('Calibri', 15)).grid(row=1, column=1)
            Button(self.crff, text='Track', background='steelBlue', bd=2, font=('Calibri', 13), padx=6, pady=6,
                   command=self.consignment).grid(row=4, column=0)


            self.consi=Frame(self.master,padx=80,pady=80,bg='lightgreen')
            Label(self.consi,text='Product Id',font=('Calibri',13),bg='lightgreen').grid(sticky=W)
            Label(self.consi,text=random.randint(500000,99994216),font=('Calibri',13),bg='lightgreen').grid(row=0,column=1)
            #L=['Shoes','Laptop','Ipad','Baby Shampoo','Shirt','Jeans','Kurtas','Book','Saree','Watch']
            #f=random.randint(0,9)
            L=['shoes','Laptop']
            f=random.randint(0,1)
            Label(self.consi,text='Product is:',font=('Calibri',13),bg='lightgreen').grid(sticky=W)
            Label(self.consi,text=L[f],font=('Calibri',13),bg='lightgreen').grid(row=1,column=1)
            Label(self.consi, text='Status:', font=('Calibri', 13), bg='lightgreen').grid(sticky=W)
            Label(self.consi, text='Pending,On the way', font=('Calibri', 13), bg='lightgreen').grid(row=2, column=1)
            Label(self.consi,font=('Calibri',13),text='Thank You',bg='lightgreen').grid(row=5,column=0)

            Button(self.consi,text='Back',background='lightgrey',bd=2,font=('',13),command=self.track1).grid(row=6,column=0)
            Button(self.consi, text='Exit', background='lightgrey', bd=2, font=('', 13), command=self.iexit).grid(
                row=6, column=1)

    def iexit(self):
                self.iexit = tkinter.messagebox.askyesno("Couriermanagement", "Are you sure exit this project",
                                                         parent=self.master)
                if self.iexit > 0:
                    self.master.destroy()
                else:
                    return


if __name__=='__main__':
   root=Tk()
   root.title('Tracking the Product')
   root.geometry('1350x750+0+0')
   main(root)

   root.mainloop()







