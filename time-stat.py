import os , sys
import time


#now= datetime.datetime.now().hour
now = time.strftime("%H:%M")
if now == '09:00' or now =='11:51' :
    #exec (open("./path/to/script.py").read(), globals())
    os.system('C:\Users\silent\Desktop\python-3.5.2.exe')
else:
    print 'not yet'
