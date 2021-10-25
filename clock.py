#digital clock 
from datetime import datetime, time
from time import gmtime
import tkinter as tk
#from tkinter.constants import S



def clock():

    
    now=datetime.now().strftime('%H:%M:%S %d-%m-%Y')
    #print(now)


    
    r=tk.Tk()
    r.title('Clock')
    r.geometry("420x150")
    text_font=("Helvetical", 30,'bold')
    background='#add8e6'
    cclock=tk.Label(r,text=now,bg=background, font=text_font)
    cclock.grid(row=3,column=1)

    
    r.mainloop()





    



if __name__=="__main__":
    clock()
    