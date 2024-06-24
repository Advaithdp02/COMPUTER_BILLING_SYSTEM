from tkinter import *
from tkinter import ttk
import mysql.connector as ms
import pickle
from tkinter import messagebox
import random
import log_m
import startup

#=========VARIABLE========
l=[]
password=''
while True:
    password=input('enter MYsql password -> ')
    break
ch=input('SHOULD WE ADD computer_billing_sys MySQL DATABASE? ')
user=''
if ch in 'yY':
    startup.startupx(password)
auth=''
#==============FUNCTION=============
def check():
    global user
    global auth
    a=u_entry.get()
    y=p_entry.get()
    str(a)
    str(y)
    x=1
    with open('pd.dat','rb') as f:
        data=pickle.load(f)
        for i in range(len(data)):
            if a==data[i][0] and y == data[i][1]:#NOT EUAL FOR NEXT SIGN
                user=a
                auth=data[i][2]
                messagebox.showinfo("showinfo", "succesful")
                login.withdraw()
                top.deiconify()
                break
            else:
                print('failed entry')

def changed(self):
    global password
    x=category.get()
    mydb=ms.connect(host='localhost',user='root',passwd=password,database='computer_billing_sys')
    mc=mydb.cursor()
    mc.execute('select Name from {} ;'.format(x))
    data=mc.fetchall()
    x=[]
    try:
        for i in range(len(data)):
            x.append(data[i][0])
    except:
        pass
    val['values']=x


def add():
    global password
    global user
    mydb=ms.connect(host='localhost',user='root',passwd=password,database='computer_billing_sys')
    mc=mydb.cursor()
    cat=category.get()
    name=val.get()
    mc.execute('select price,sn_no from {} where name="{}"'.format(cat,name))
    data=mc.fetchall()
    x=data[0][0]
    price=x*eval(bqty.get())
    textarea.insert((10.0+float(len(l)-1)), f"{name}\t\t{bqty.get()}\t\t{price}\n")
    l.append([price,data[0][1],bqty.get(),cat])
def welcome():
    textarea.delete(1.0,END)
    textarea.insert(END,"\t \t COMPUTER SHOP")
    textarea.insert(END,f"\n\n==============================================")
    textarea.insert(END,f"\nCustomer Name:\t{name.get()}\t")
    textarea.insert(END,f"\nPhone Number:\t{number.get()}\t")
    textarea.insert(END,f"\n\n==============================================")
    textarea.insert(END,"\nProduct\t\tQTY\t\tPRICE")
    textarea.insert(END,f"\n==============================================\n")
    textarea.configure(font='arial 15')
def generate():
    x=[]
    for i in range(len(l)):
            x.append(l[i][0])
    bill_no=billNo()
    bill_no1=bill_no[:5]
    textAreaText = textarea.get(9.0,(11.0+float(len(x))))
    welcome()
    textarea.insert(END, textAreaText)
    textarea.insert(END, f"\nTotal Paybill Amount :\t\t      {sum(x)}")
    textarea.insert(END, f"\n\n======================================")
    textarea.insert(END,f"\n\nBill Number:\t {bill_no1}\t")
    log_m.log_add(user,1)
    op=messagebox.askyesno("Save bill","Do you want t o save the Bill?")
    if op>0:
        bill_details=textarea.get('1.0',END)
        f1=open(f"./Generated-bills/bills-{bill_no1}.txt","w")
        f1.write(bill_details)
        f1.close()

    else:
        return
    reduce()
def clear():
    textarea.delete(1.0,END)
    welcome()
def reduce():
    global password
    mydb=ms.connect(host='localhost',user='root',passwd=password,database='computer_billing_sys')
    mc=mydb.cursor()
    for i in range(len(l)):
        mc.execute('update {} set qty=qty-{} where sn_No="{}"'.format(l[i][3],l[i][2],l[i][1]))
        mydb.commit()
def billNo():
    f=open('billno.txt','r')
    data=f.readlines()

    x=data[random.randint(0,len(data))]

    f.close()
    with open('billno.txt','r+') as d:
        data.remove(x)
        d.truncate(0)
        d.seek(0)
        d.writelines(data)
    return x
def Exit():
    top.destroy()
    print('done')

def add_log():
    newadd.deiconify()

    Label(newadd,text='user name').pack()
    def add():

        with open('pd.dat','rb') as y:
            x=pickle.load(y)

        with open ('pd.dat','wb') as f:
            data=[usr.get(),passwd.get(),role.get()]
            x.append(data)

            pickle.dump(x,f)
    usr=Entry(newadd)
    usr.pack()
    Label(newadd,text='password').pack()
    passwd=Entry(newadd)
    role=ttk.Combobox(newadd)
    role['values']=['admin','employee']
    role.pack()
    passwd.pack()
    Button(newadd,text="ADD",command=add,width=20,height=10).pack()
    log_m.log_add(user,4)
def logtxt():
    textarealog.delete(1.0,END)
    with open('log.txt','r')as f:
        data=f.readlines()
    for i in range(len(data)):
        textarealog.insert(END,data[i])

def welcomex():
    txtarea.delete(1.0,END)
    txtarea.insert(END,f"\n\n======================================")
    txtarea.insert(END,"\nProduct\t\tQTY\t\tPRICE")
    txtarea.insert(END,f"\n======================================\n")
    txtarea.configure(font='arial 15 bold')
def clearx():
    txtarea.delete(1.0,END)
    welcomex()
def addx():
    mydb=ms.connect(host='localhost',user='root',passwd='password',database='computer_billing_sys')
    mc=mydb.cursor()
    mc.execute('select * from {};'.format(categoryx.get()))
    data=mc.fetchall()

    try:
        for i in range(len(data)):
            txtarea.insert((10.0), f"{data[i][1]}\t\t{data[i][2]}\t\t{data[i][3]}\n")
    except:
        pass
    log_m.log_add(user,2)
def new():
    def addx():
        mydb=ms.connect(host='localhost',user='root',passwd='password',database='computer_billing_sys')
        mc=mydb.cursor()
        cate=categoryz.get()
        a=sn.get()
        b=name.get()
        c=qty.get()
        d=price.get()

        print(a,b,c,d,cate)
        try:
            mc.execute('insert into {} values("{}","{}",{},{})'.format(cate,a,b,c,d))
            mydb.commit()
        except:
            mydb.rollback()
            print('error adding stuff')
        print('user added new item named',b)


    new=Toplevel(window)
    sn=Entry(new)
    name=Entry(new)
    qty=Entry(new)
    price=Entry(new)
    Label(new,text='sn').grid(row=1,column=2)
    sn.grid(row=1,column=1)
    Label(new,text='name').grid(row=2,column=2)
    name.grid(row=2,column=1)
    Label(new,text='qty').grid(row=3,column=2)
    qty.grid(row=3,column=1)
    Label(new,text='price').grid(row=4,column=2)
    price.grid(row=4,column=1)
    Label(new,text='select category',font=("ARIEL",15)).grid(row=6,column=1)
    categoryz=ttk.Combobox(new)
    mydb=ms.connect(host='localhost',user='root',passwd='password',database='computer_billing_sys')
    mc=mydb.cursor()
    mc.execute('show tables;')
    cat=mc.fetchall()
    category_list=[]
    try:
        for i in cat:
            category_list.append(i)
    except:
        pass
    categoryz['values']=category_list
    categoryz.grid(row=5,column=1)
    Button(new,text='add',command=addx).grid(row=5,column=2)
def update():
    def search():
        mydb=ms.connect(host='localhost',user='root',passwd='password',database='computer_billing_sys')
        mc=mydb.cursor()
        cat=categoryy.get()
        x=sn.get()
        try:
            mc.execute('select * from {} where sn_no ="{}"'.format(cat,x))
            data=mc.fetchall()
            name.insert(0,data[0][1])
            price.insert(0,data[0][3])
            qty.insert(0,data[0][2])
        except:
            print('error loading data')
    def updatex():
        a=sn.get()
        b=name.get()
        c=qty.get()
        d=price.get()
        cat=categoryy.get()

        try:
            mydb=ms.connect(host='localhost',user='root',passwd='password',database='computer_billing_sys')
            mc=mydb.cursor()
            mc.execute('update {} set name="{}",qty={},price={} where sn_no="{}"'.format(cat,b,c,d,a))
            mydb.commit()
        except:
            mydb.rollback()
            print('error')
        log_m.log_add(user,3)
    update=Toplevel(window)
    sn=Entry(update)
    name=Entry(update)
    qty=Entry(update)
    price=Entry(update)
    Label(update,text='sn').grid(row=1,column=2)
    sn.grid(row=1,column=1)
    Label(update,text='name').grid(row=2,column=2)
    name.grid(row=2,column=1)
    Label(update,text='qty').grid(row=3,column=2)
    qty.grid(row=3,column=1)
    Label(update,text='price').grid(row=4,column=2)
    price.grid(row=4,column=1)
    Label(update,text='select category',font=("ARIEL",15)).grid(row=6,column=1)
    categoryy=ttk.Combobox(update)
    mydb=ms.connect(host='localhost',user='root',passwd='password',database='computer_billing_sys')
    mc=mydb.cursor()
    mc.execute('show tables;')
    cat=mc.fetchall()
    category_list=[]
    try:
        for i in cat:
            category_list.append(i)
    except:
        pass
    categoryy['values']=category_list
    categoryy.grid(row=5,column=1)
    Button(update,text='update',command=updatex).grid(row=5,column=2)
    Button(update,text='search',command=search).grid(row=5,column=3)
def c_start():
    global auth

    if auth.lower()!='admin':
        messagebox.showwarning("warning","YOU ARE NOT AN ADMIN")
        return

    top.withdraw()
    choice.deiconify()
def choice_a():
    choice.withdraw()
    log.deiconify()
def choice_w():
    choice.withdraw()
    window.deiconify()
def back1():
    choice.withdraw()
    top.deiconify()
def back2():
    window.withdraw()
    choice.deiconify()
def back3():
    log.withdraw()
    choice.deiconify()
def refresh():
    logtxt()













#============DESIGN-STARTUP==================
top = Tk()
top.geometry('958x700')
top.configure(bg='#DAE9E4')
L1 = Label(top, text = "COMPUTER SHOP",fg = "#3C2E3D",
		 bg = "#FDAE85",
		 font = "Helvetica 35 bold italic",padx=320,pady=35)

L1.place(x = 0,y = 10)
l2 = Label(top, text ="CUSTOMER NAME",font = "Helvetica 16 bold ",fg = "#3D1053",
		 bg = "#FDAE85",width=19)
name=Entry(top)
l2.place(y=140,x=530)
name.place(y=140,x=710,width=250)
Label(top,text="PHONE NUMBER",font = "Helvetica 16 bold ",fg = "#3D1053",
		 bg = "#FDAE85",width=19).place(x=530,y=170)
number=Entry(top)
number.place(y=170,x=710,width=250)
Label(top,text="CATEGORY",font = "Helvetica 16 bold ",fg = "#3D1053",
		 bg = "#FDAE85",width=25).place(x=0,y=230)
Label(top,text="ITEM",font = "Helvetica 16 bold ",fg = "#3D1053",
		 bg = "#FDAE85",width=25).place(x=0,y=260)
#===============================DROPDOWN=========================
category=ttk.Combobox(top)
mydb=ms.connect(host='localhost',user='root',passwd=password,database='computer_billing_sys')
mc=mydb.cursor()
mc.execute('show tables;')
cat=mc.fetchall()
category_list=[]
try:
    for i in cat:
        category_list.append(i)
except:
    pass
category['values']=category_list
category.place(x=250,y=230,width=270)
category.bind('<<ComboboxSelected>>',changed)
val=ttk.Combobox(top)
val.place(x=250,y=260,width=270)
val.bind('<<ComboboxSelected>>')
Label(top,text="BUYING QTY.",font = "Helvetica 16 bold ",width=25,fg = "#3D1053",
		 bg = "#FDAE85").place(x=0,y=300)
bqty=Entry(top)
bqty.place(x=250,y=300,width=270)
add=Button(top,text='ADD',command=add,fg='#3D1053',bg='#8DCBCA')
clear=Button(top,text='CLEAR',command=clear,fg='#3D1053',bg='#8DCBCA')
generate=Button(top,text='GENERATE BILL',command=generate,fg='#3D1053',bg='#8DCBCA')
setting=Button(top,text='SETTING',command=c_start,fg='#3D1053',bg='#8DCBCA')
exitx=Button(top,text='EXIT',command=Exit,fg='#3D1053',bg='#8DCBCA')
add.place(x=35,y=370,width=150,height=120)
clear.place(x=335,y=370,width=150,height=120)
generate.place(x=35,y=510,width=150,height=120)
setting.place(x=335,y=510,width=150,height=120)
exitx.place(x=490,y=680)
texta=Frame(top)
texta.place(x=530,y=210,width=429,height=500)
bill_title=Label(texta,text='Bill Area',font='arial 15 bold',bd=7,relief=GROOVE,fg = "#3C2E3D",
		 bg = "#FDAE85",).pack(fill=X)
scrol_y=Scrollbar(texta,orient=VERTICAL)
textarea=Text(texta,yscrollcommand=scrol_y)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=textarea.yview)
textarea.pack()
welcome()
#==============LOGIN======================
login=Toplevel(top)
login.geometry("400x400")
login.configure(bg='white')
imglogin=PhotoImage(file='./images/lock.png')
x=Label(login)
x.place(x=0,y=100,height=300,width=370)
x.configure(image=imglogin)
label = Label(login,text="LOGIN",fg = "#3D1053",
		 bg = "#FDAE85",font = "Helvetica 35 bold ",padx=320,pady=15)
Label(login,text="user", fg = "#3D1053",
		 bg = "#FDAE85",width=7,height=2).place(x=30,y=100)
Label(login,text="password", fg = "#3D1053",
		 bg = "#FDAE85",width=7,height=2).place(x=30,y=150)
u_entry=Entry(login,text='user',fg='#3D1053',bg='#8DCBCA')
p_entry=Entry(login,show='*',fg='#3D1053',bg='#8DCBCA')
label.pack()
u_entry.place(x=100,y=100,height=30)
p_entry.place(x=100,y=150,height=30)
Button(login,text='Login',command=check,fg='#3D1053',bg='#8DCBCA').place(x=170,y=200,width=70,height=40)
Button(login,text='Exit',command=Exit,fg='#3D1053',bg='#8DCBCA').place(x=320,y=350,width=70,height=40)




#=================WAREHOUSE=======================
window=Toplevel(top)
window.configure(bg='#DAE9E4')
window.geometry('760x600')
categoryx=ttk.Combobox(window)
mydb=ms.connect(host='localhost',user='root',passwd=password,database='computer_billing_sys')
mc=mydb.cursor()
mc.execute('show tables;')
cat=mc.fetchall()
category_list=[]

try:
    for i in cat:
        category_list.append(i)
except:
    pass
categoryx['values']=category_list
categoryx.place(x=500,y=100)
txta=Frame(window)
txta.place(x=50,y=100,width=400,height=400)
txtarea=Text(txta)
txtarea.pack()
Label(window,text="WAREHOUSE",font = "Helvetica 35 bold italic",fg = "#3D1053",
		 bg = "#FDAE85",padx=320,pady=20).place(x=0,y=0)
Button(window,text='SEARCH',command=addx,width=10,height=5,fg='#3D1053',bg='#8DCBCA').place(x=500,y=140)
Button(window,text='CLEAR',command=clearx,width=10,height=5,fg='#3D1053',bg='#8DCBCA').place(x=630,y=140)
Button(window,text='UPDATE',command=update,width=10,height=5,fg='#3D1053',bg='#8DCBCA').place(x=500,y=240)
Button(window,text='NEW',command=new,width=10,height=5,fg='#3D1053',bg='#8DCBCA').place(x=630,y=240)
b3=PhotoImage(file='./images/back.png')
bgpic1=Button(window,height=60,width=80,command=back2,fg='#3D1053',bg='#8DCBCA')
bgpic1.place(x=670,y=540)
bgpic1.configure(image=b3)
welcomex()
#welcome()
#====================choice===================
choice=Toplevel(top)
choice.configure(bg='#DAE9E4')
choice.geometry('550x500')
admin=Button(choice,width=100,height=100,command=choice_a,fg='#3D1053',bg='#8DCBCA')
store=Button(choice,text='',width=100,height=100,command=choice_w,fg='#3D1053',bg='#8DCBCA')
c_img1=PhotoImage(file='./images/output-onlinepngtools.png')
c_img2=PhotoImage(file='./images/warehouse.png')
admin.configure(image=c_img1)
store.configure(image=c_img2)
admin.place(x=100,y=100)
store.place(x=350,y=100)
Label(choice,text='ADMIN',width=11,fg = "#3D1053",
		 bg = "#FDAE85").place(x=100,y=210)
Label(choice,text='WAREHOUSE',width=11,fg = "#3D1053",
		 bg = "#FDAE85").place(x=350,y=210)
back=PhotoImage(file='./images/back.png')
backx=Button(choice,width=100,height=60,command=back1)
backx.place(x=450,y=350)
backx.configure(image=back)
#==================log======================
log=Toplevel(top)
log.geometry('420x600')
log.configure(bg='#DAE9E4')
newadd=Toplevel(top)
newadd.geometry('300x170')
textalog=Frame(log)
textalog.place(x=0,y=0,width=420,height=300)
log_title=Label(textalog,text='LOG',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol_ylog=Scrollbar(textalog,orient=VERTICAL)
textarealog=Text(textalog,yscrollcommand=scrol_ylog)
scrol_ylog.pack(side=RIGHT,fill=Y)
scrol_ylog.config(command=textarealog.yview)
textarealog.pack()
logtxt()
Button(log,text='ADD USER',command=add_log,width=20,height=10).place(x=100,y=380)
Button(log,text='ADD USER',command=add_log,width=20,height=10).place(x=100,y=380)
newadd.withdraw()
Button(log,text='ADD USER',command=add_log,width=20,height=10).place(x=100,y=380)
b2=PhotoImage(file='./images/back.png')
bgpic=Button(log,height=60,width=80,command=back3)
bgpic.place(x=330,y=530)
bgpic.configure(image=b2)
Button(log,command=refresh,text="REFRESH").place(x=330,y=450)


choice.withdraw()
window.withdraw()
log.withdraw()
top.withdraw()
top.mainloop()
