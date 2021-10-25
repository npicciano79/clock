#digital clock 
from datetime import datetime, time
from time import gmtime
import tkinter as tk
from tkinter.constants import S


def clock():
    now=datetime.now().strftime('%H:%M:%S %d-%m-%Y')
    print(now)


    
    r=tk.Tk()
    r.title('Clock')
    r.mainloop()





    



if __name__=="__main__":
    clock()
    