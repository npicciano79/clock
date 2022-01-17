#digital clock 
#C:/Users/npicc/Documents/python/python.exe c:/Users/npicc/Documents/Coding/projects/clock/clock.py
import time
from datetime import datetime, time
from time import gmtime
import tkinter as tk

r=tk.Tk()
r.title('Clock')
r.geometry("420x150")
time_font=("ds-digital", 50,'bold')
day_font=("ds-digital", 20)
background='#000000'
c_label=tk.Label(r,font=time_font,bg=background,foreground='#00FF00')
c_label.place(relx=0.05, rely=0.05, relheight=0.6, relwidth=0.9)
date_label=tk.Label(r,font=day_font,bg=background,foreground='#00FF00')
date_label.place(relx=0.05, rely=0.65, relheight=0.2, relwidth=0.5)
day_label=tk.Label(r,font=day_font,bg=background,foreground='#00FF00')
day_label.place(relx=0.55, rely=0.65, relheight=0.2, relwidth=0.40)




def clock():
    now=datetime.now().strftime('%H:%M:%S %m/%d/%Y')
    time,date=now.split()
    day_index=datetime.today().weekday()
    #print(f"date{date} time{time}")
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

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
    
    date_label.config(text=date)
    day_label.config(text=days[day_index])
    r.after(1000,clock)





clock()
r.mainloop()





    




    