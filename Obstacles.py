from random import random,randint
from tkinter import *
from tkinter import *

window=Tk()
window.geometry("800x800")
sky=Canvas(window,width=800,height=400)
sky.pack()
class stars:
    def __init__(self,canvas:Canvas):
        self.starsx=randint(0,800)
        self.starsy=randint(0,400)
        diameter=randint(0,3)
        self.image=canvas.create_oval(self.starsx,self.starsy,self.starsx+diameter,self.starsy+diameter)
for i in range(400):
    stars(sky)
window.mainloop()