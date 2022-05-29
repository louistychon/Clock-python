#simple clock program in Python

from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p") #sets up the format
    time_label.config(text=time_string)

    day_string = strftime("%A") #sets up the format
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y") #sets up the format
    date_label.config(text=date_string)

    window.after(1000,update) #for the update every second

window = Tk()

time_label = Label(window, font= ("Arial",50), fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(window, font= ("Arial",50), fg="#00FF00", bg="black")
day_label.pack()

date_label = Label(window, font= ("Arial",50), fg="#00FF00", bg="black")
date_label.pack()

update()

window.mainloop()