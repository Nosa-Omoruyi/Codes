from tkinter import *
from tkinter.ttk import *

# importing strftime function to 
# retrieve system"s time
from time import strftime

# creating tkinter window
window = Tk()
window.title('Clock')

# This function is used to
# display time on the label 
def time():
    time_live = strftime('%H:%M:%S %p')
    lbl.config(text = time_live)
    lbl.after(1000, time)

#Styling the label wdget so that clock
# will look more attractive
lbl = Label(window, font = ('calibri', 40, 'bold'),
            background='purple',
            foreground='white')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')
time()

mainloop()