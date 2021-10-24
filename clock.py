#digital clock 
from datetime import datetime, time
import tkinter as tk
from tkinter.constants import S


def clock():
    hour=datetime.now().strftime('%H')
    print(hour)
     r=tk.Tk()
    r.title('Clock')


    r.mainloop()





    



if __name__=="__main__":
    clock()
    