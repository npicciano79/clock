#digital clock 
import time
from datetime import datetime, time
from time import gmtime
import tkinter as tk


r=tk.Tk()
r.title('Clock')
r.geometry("420x150")
text_font=("Helvetical", 30,'bold')
background='#add8e6'
c_label=tk.Label(r,font=text_font,bg=background)
c_label.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)


def clock():
    
    now=datetime.now().strftime('%H:%M:%S %m/%d/%Y')
    #convert hour from military to standard
    n_hour=int(now.split(':')[0])
    setting="PM"
    if n_hour<12:
        setting="AM"
    elif n_hour>12:
        n_hour=n_hour-12
    
    min=now.split(':')[1]
    sec=now.split(':',2)[1]
    
    t_now=str(n_hour)+":"+min+":"+sec+" "+setting
        
    #print(f"time: {t_now} ")
    c_label.config(text=t_now)
    c_label.after(200,clock)
    
  

if __name__=="__main__":
    clock()    
    r.mainloop()





    




    