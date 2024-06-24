import pickle
from datetime import datetime
def log_add(name,x):
    data=open('log.txt','a+')
    if x==1:
        now=datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        data.write(name +' '+'made a sale')
        data.write(' ')
        data.write(dt_string)

        data.write('\n')
    elif x==2:
        now=datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        data.write(name +' '+'ADDED A NEW PRODUCT')
        data.write(' ')
        data.write(dt_string)
        data.write('\n')
    elif x==3:
        now=datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        data.write(name +' '+'UPDATED THE WAREHOUSE RECORDS')
        data.write(' ')
        data.write(dt_string)
        data.write('\n')
    elif x==4:
        now=datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        data.write(name +' '+'ADDED A NEW ADMIN')
        data.write(' ')
        data.write(dt_string)
        data.write('\n')
