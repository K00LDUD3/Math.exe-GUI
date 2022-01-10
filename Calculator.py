from tkinter import *
import tkinter.font as font
from types import NoneType



root = Tk()
root.title('Calculator')

class Calc:
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
        #check type of widg (button, label, textbox, frame), then call a function to create that specific widg
        if type.upper() == 'BUTTON':
            self.b_dict_init(widg_d = widg_dict)
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
    
    def createB(self, dict, text):
        self.button = Button(None)
        return

    def b_dict_init(self, widg_d):
        self.wd = {
            #button config params
            'act_bg':widg_d['act_bg'],
            'act_fg':widg_d['act_fg'],
            'bg':widg_d['bg'],
            'fg':widg_d['fg'],
            'border':widg_d['border'],
            'font':widg_d['font'],
            'height':widg_d['height'],
            'highl_color':widg_d['highl_color'],
            'image':widg_d['image'],
            'justify':widg_d['justify'],
            'padx':widg_d['padx'],
            'pady':widg_d['pady'],
            'relief':widg_d['relief'],
            'underline':widg_d['underline'],
            'w':widg_d['w'],
            'wraplength':widg_d['wraplength'],
        }


        
        

root.mainloop()