import sys
from tkinter import *
import time

def times():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)

root = Tk()
root.geometry("400x200")
clock = label(root,font=("times",42,"bold"),bg="while")
clock.grid(row=2,column=2,pady=25,padx=100)
times()

digi = Label(root,text = "Digital Clock",font="times 15 bold")
digi.grid(row=0,column=2)

nota = label(root,text = "hours minutes seconds",font = "times 15 bold")
nota.grid(row=3,column=2)

root.mainloop()


