#digital clock 
#C:/Users/npicc/Documents/python/python.exe c:/Users/npicc/Documents/Coding/projects/clock/clock.py
import time
from datetime import datetime, time
from time import gmtime
import tkinter as tk


r=tk.Tk()
r.title('Clock')
r.geometry("420x150")
time_font=("calibri", 50,'bold')
day_font=("calibri", 20)
background='#000000'
c_label=tk.Label(r,font=time_font,bg=background,foreground='#FFFF00')
c_label.place(relx=0.05, rely=0.05, relheight=0.6, relwidth=0.9)
date_label=tk.Label(r,font=day_font,bg=background,foreground='#FFFF00')
date_label.place(relx=0.05, rely=0.65, relheight=0.2, relwidth=0.5)
day_label=tk.Label(r,font=day_font,bg=background,foreground='#FFFF00')
day_label.place(relx=0.55, rely=0.65, relheight=0.2, relwidth=0.40)


def clock():
    
    now=datetime.now().strftime('%H:%M:%S %m/%d/%Y')
    time,date=now.split()
    #print(f"date{date} time{time}")

    #convert hour from military to standard
    n_hour=int(time.split(':')[0])
    setting="PM"
    if n_hour<12:
        setting="AM"
    elif n_hour>12:
        n_hour=n_hour-12
    
    min=time.split(':')[1]
    sec=time.split(':',2)[1]
    
    t_now=str(n_hour)+":"+min+":"+sec+" "+setting
 
    #print(f"time: {t_now} ")
    c_label.config(text=t_now)
    c_label.after(10,clock)
    date_label.config(text='test')
    day_label.config(text='test')



if __name__=="__main__":
    clock()    
    r.mainloop()





    




    