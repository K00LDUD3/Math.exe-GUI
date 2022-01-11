from tkinter import *
import tkinter.font as font
from types import NoneType



root = Tk()
root.title('Calculator')

class GenFunc:
    widg = None
    text = ''
    wd = {} #Widget Dictionary
    gd = {}
    #frame = None
    def __init__(self, type, widg_dict, text, grid_dict) -> None:
        #Assigning param variables to class variables
        self.text = text
        self.wd = widg_dict
        self.gd = grid_dict
        '''
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
        '''

        #checking type of widg (button, label, textbox, frame), then call a function to create that specific widg
        if type.upper() == 'BUTTON':
            self.widg = Button()
            pass
        elif type.upper() == 'LABEL':
            self.widg = Label()
            pass
        elif type.upper() == 'ENTRY':
            self.widg = Entry()
            pass
        elif type.upper() == 'LABELFRAME':
            self.widg = LabelFrame()
            pass
        else:
            print('err: widget unidentified')
            return
        pass

    #Generating a BUTTON using parameters stored in a dictionary
    def createB(self):
        self.widg = Button(
            master= self.wd['master'],
            text=self.text,
            activebackground= self.wd['act_bg'],
            activeforeground= self.wd['act_fg'],
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
        self.widg.grid(
            column= self.gd['column'],
            row= self.gd['row'],
            columnspan= self.gd['cspan'],
            rowspan= self.gd['rspan'],
            padx= self.gd['padx'],
            pady= self.gd['pady'],
            ipadx= self.gd['ipadx'],
            ipady= self.gd['ipady']
        )
        '''
        button_widg_dict = {
            'master':Nones,
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
            'w':None,
            'wraplength':None
        }
        '''
        return

    #Generating a LABEL using parameters stored in a dictionary
    def createL(self):
        self.widg = Label(
            master= self.wd['master'],
            textvariable=  self.text,
            anchor=  self.wd['anchor'],
            background=  self.wd['bg'],
            foreground=  self.wd['fg'],
            bitmap=  self.wd['bitmap'],
            bd=  self.wd['bd'],
            font=  self.wd['font'],
            height=  self.wd['height'],
            image=  self.wd['image'],
            justify=  self.wd['justify'],
            padx=  self.wd['padx'],
            pady=  self.wd['pady'],
            relief=  self.wd['relief'],
            underline=  self.wd['underline'],
            width=  self.wd['w'],
            wraplength=  self.wd['wraplength']
        )
        self.widg.grid(
            column= self.gd['column'],
            row= self.gd['row'],
            columnspan= self.gd['cspan'],
            rowspan= self.gd['rspan'],
            padx= self.gd['padx'],
            pady= self.gd['pady'],
            ipadx= self.gd['ipadx'],
            ipady= self.gd['ipady']
        )
        '''
        lab_dict = {
            'master':None,
            'anchor':None,
            'bg':None,
            'bitmap':None,
            'bd':None,
            'font':None,
            'fg':None,
            'height':None,
            'image':None,
            'justify':None,
            'padx':None,
            'pady':None,
            'relief':None,
            'text':None,
            'textvar':None,
            'underline':None,
            'w':None,
            'wraplength':None
        }   
        '''
        return

    #Generating a ENTRY (aka textbox) using parameters stored in a dictionary
    def createE(self):
        self.widg = Entry(
            master= self.wd['master'],
            textvariable= self.text,
            width= self.wd['w'],
            bd= self.wd['bd'],
            background= self.wd['bg'],
            foreground= self.wd['fg'],
            font= self.wd['font'],
            insertofftime= self.wd['insertofftime'],
            insertontime= self.wd['insesrtontime'],
            highlightbackground= self.wd['highlbg'],
            highlightcolor= self.wd['highlcolor'],
            relief= self.wd['relief'],
            highlightthickness= self.wd['highthick'],
            cursor= self.wd['cursor'],
            xscrollcommand= self.wd['xscrollcommand']
        )
        self.widg.grid(
            column= self.gd['column'],
            row= self.gd['row'],
            columnspan= self.gd['cspan'],
            rowspan= self.gd['rspan'],
            padx= self.gd['padx'],
            pady= self.gd['pady'],
            ipadx= self.gd['ipadx'],
            ipady= self.gd['ipady']
        )
        '''
        entry_dict = {
            'master':None,
            'bd':None,
            'height':None,
            'width':None,
            'bg':None,
            'fg':None,
            'font':None,
            'insertofftime':None,
            'insertontime':None,
            'padx':None,
            'pady':None,
            'highthick':None,
            'charwidth':None,
            'relief':None,
            'yscrollcommand':None,
            'xscrollcommand':None,
        }
        '''
        return

'''-------------TESTING-------------'''
frame = LabelFrame(root)
frame.pack()

widg_test_dict = {
    'master':frame,
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
    'wraplength':None
}
            
grid_test_dict = {
    'column':0,
    'row':1,
    'cspan':1,
    'rspan':1,
    'padx':0,
    'pady':0,
    'ipadx':0,
    'ipady':5
}
widg_test = GenFunc(type='button', widg_dict=widg_test_dict, text='test', grid_dict=grid_test_dict)
widg_test.createB() 
print(str(widg_test.widg).split('!')[-1]) # getting type of widget

root.mainloop()