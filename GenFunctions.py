from tkinter import *
import tkinter.font as font
from tkinter import ttk
from tkinter.ttk import *
'''
TKINTER - supports few widgets 
TTK - supports lotta widgets BUT it doesnt support grid, pack and place so tkinter is used along with it
'''

theme = 'xpnative' #Setting the theme (Inbuilt themes)
class GenFunc:
    widg = None #Current widget
    text = ''
    wd = {} #Widget Dictionary containing features 
    gd = {} #Grid Dictionary containing placement info
    def __init__(self, type, widg_dict, text, grid_dict): #Constructor
        #Assigning param variables to class variables
        #SELF keyword is python equivalent of THIS in java
        self.text = text
        self.wd = widg_dict
        self.gd = grid_dict
        '''
        GRID dictionary parameters
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

        #checking type of widg (button, label, textbox), then call a function to create that specific widget
        if type.upper() == 'BUTTON':
            self.createB()
        elif type.upper() == 'LABEL':
            self.createL()
        elif type.upper() == 'ENTRY':
            self.createE()
        else:
            print('err: widget unidentified')
        return

    #Generating a BUTTON using parameters/features stored in a dictionary
    def createB(self):
        s=ttk.Style(master=None) #Setting a theme
        s.theme_use(theme)
        self.widg = Button(
            master= self.wd['master'],
            text=self.text,
            #activebackground= self.wd['act_bg'], '''ACTIVE BACK/FORE GROUND doesnt work with xpnative theme'''
            #activeforeground= self.wd['act_fg'],
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
        Use these KEYS for the features
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

    #Generating a LABEL using parameters/features stored in a dictionary
    def createL(self):
        s=ttk.Style(master=None)
        s.theme_use(theme)
        self.widg = Label(
            master= self.wd['master'],
            text=  self.text,
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

    #Generating a ENTRY (aka textbox) using parameters/features stored in a dictionary
    def createE(self):
        s=ttk.Style(master=None)
        s.theme_use(theme)
        self.widg = Entry(
            master= self.wd['master'],
            textvariable= self.text,
            width= self.wd['w'],
            bd= self.wd['bd'],
            background= self.wd['bg'],
            foreground= self.wd['fg'],
            font= self.wd['font'],
            insertofftime= self.wd['insertofftime'],
            insertontime= self.wd['insertontime'],
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