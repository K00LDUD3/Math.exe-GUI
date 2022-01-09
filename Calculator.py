from tkinter import *
import tkinter.font as font
from types import NoneType

from GUI_integration import createButton

root = Tk()
root.title('Calculator')

class Calc:
    #frame = None
    def __init__(self, f_par_dict, l_par_dict) -> None:
        self.frame = Frame(master=root)
        self.frame.pack(padx=5, pady=5)

        self.lab = Label(master=self.frame, text='Label', width=10, height=2, font=None, foreground=None, background=None, borderwidth=None, border=None, bg=None, fg=None, anchor=None)
        self.lab.grid(row=0, column=0, columnspan=4)

        self.button_l = []
    def createButton(self, frame, w, t, px, py, xcor, ycor, f):
        self.button = Button(master=frame, width=w, text=t, font=f)
        self.button.grid(row=xcor, column=ycor, padx=px, pady=py)
        return self.button
    
    def createLabel(self, frame, w, h, t, px, py, xcor, ycore, f, cspan, rspan, bg, fg, act_bg, act_fg, dis_bg, dis_fg, state, hig_bg, hig_fg):
        self.label = Label(master=frame)
        return



c = Calc(None, None)
c.createButton(c.frame, 10, 'hello', 10, 10, 1, 0, None)


for i in range(0,9):
    c.button_l.append(createButton(frame=c.frame, Text=i+1, ))
    pass
print(c.__dict__)
root.mainloop()