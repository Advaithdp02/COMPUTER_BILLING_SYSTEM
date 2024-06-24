import mysql.connector as ms

def startupx(password):
    mydb=ms.connect(host='localhost',user='root',passwd=password)
    mc=mydb.cursor()
    if mydb.is_connected():
        print("Connection to db established")
    else:
        print("Connection failed")
    mc.execute('show databases')
    x=mc.fetchall()
    if('computer_billing_sys',) in x:
        mc.execute('drop database computer_billing_sys')
        
    mc.execute('create database computer_billing_sys')
    mc.execute('use  computer_billing_sys')
    mc.execute('create table speaker(SN_NO varchar(5) PRIMARY KEY,NAME varchar(25),QTY int,PRICE INT);')
    mc.execute('insert into speaker values("S001","BOSS S1",50,900);')
    mc.execute('insert into speaker values("S002","BEATS Z15",30,650);')
    mc.execute('insert into speaker values("S003","SONY G21",35,545);')
    mc.execute('create table MONITOR(SN_NO varchar(5) PRIMARY KEY,NAME varchar(25),QTY int,PRICE INT);')
    mc.execute('insert into MONITOR values("M001","SAMSUNG V9",30,2500),("M002","SONY CURVED",15,6000),("M003","LG OLED",25,4500);')
    mc.execute('create table mouse(SN_NO varchar(5) PRIMARY KEY,NAME varchar(25),QTY int,PRICE INT);')
    mc.execute('insert into mouse values("M101","RAZOR pro",30,1200),("M102","SONY M5",15,600),("M103","GAMING PRO v2",25,3500);')
    mc.execute('create table keyboard(SN_NO varchar(5) PRIMARY KEY,NAME varchar(25),QTY int,PRICE INT);')
    mc.execute('insert into keyboard values("k001","RAZOR 240x",30,1200),("k002","SONY K4",15,600),("k003","GAMING PRO KEYBOARD",25,3500);')
    

    
    mydb.commit()
