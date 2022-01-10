from tkinter import *
import tkinter.font as font
from types import NoneType



root = Tk()
root.title('Calculator')

class Calc:
    text = ''
    wd = {} #Widget Dictionary
    gd = {
            'column':None,
            'row':None,
            'cspan':None,
            'rspan':None,
            'padx':None,
            'pady':None,
            'ipadx':None,
            'ipady':None
        }
    #frame = None
    def __init__(self, type, widg_dict, text, grid_dict) -> None:
        self.text = text
        self.wd = widg_dict
        #check type of widg (button, label, textbox, frame), then call a function to create that specific widg
        if type.upper() == 'BUTTON':
            pass
        elif type.upper() == 'LABEL':
            pass
        elif type.upper() == 'TEXTBOX':
            pass
        elif type.upper() == 'FRAME':
            pass
        else:
            print('err: widget unidentified')
            return
        pass
    
    #Gen 
    def createB(self):
        self.button = Button(
            master= self.wd['frame'],
            activebackground= self.wd['act_bg'],
            activeforeground= self.wd['act_fg'],
            text=self.text,
            width=self.wd['w'],
            height=self.wd['height'],
            font=self.wd['font'],
            highlightbackground=self.wd['highl_color'],
            background=self.wd['bg'],
            foreground=self.wd['fg'],
            justify=self.wd['justify'],
            padx=self.wd['padx'],
            pady=self.wd['pady'],
            wraplength=self.wd['wraplength'],
            relief=self.wd['relief'],
            underline=self.wd['underline']

        )
        self.button.grid(row=0, column=0)









frame = LabelFrame(root)
frame.pack()

widg_test_dict = {'frame':frame,
            'act_bg':None,
            'act_fg':None,
            'bg':None,
            'fg':None,
            'border':None,
            'font':None,
            'height':None,
            'highl_color':None,
            'image':None,
            'justify':None,
            'padx':None,
            'pady':None,
            'relief':None,
            'underline':None,
            'w':10,
            'wraplength':None}
widg_test = Calc('BUTTON', widg_test_dict, 'test', None)
widg_test.createB()

root.mainloop()