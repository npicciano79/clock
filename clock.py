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
c_label.grid(row=3,column=1)




def clock():
    
    now=datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    c_label.config(text=now)
    c_label.after(200,clock)

    
    
    #cclock=tk.Label(r,text=now,bg=background, font=text_font)
    

if __name__=="__main__":
    clock()    
    r.mainloop()





    




    