#digital clock 
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
    c_label.config(text=now)
    c_label.after(200,clock)
  

if __name__=="__main__":
    clock()    
    r.mainloop()





    




    