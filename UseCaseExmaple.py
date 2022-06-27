from tkinter import *
from tkinter import ttk
import tkinter.font as font

import GenFunctions as gfunc ###

#Creating WINDOW for hosting FRAMES
root = Tk()
root.title('Example')
root.resizable(False, False)
root.geometry("365x150")

#Creating FRAMES for hosting WIDGETS
signIn_frame = LabelFrame(root) #Signing in

#misc variables
pass_dot = '\u2022' #UNICODE for the password dot

#WIDGET DICTIONARIES (GLOBAL to access anytime)
#Button features
button_widg_dict = {
            'master':None,
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
#for label features
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
#Entry features
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
#GRID features
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

#Creating hide frame function
#Used to hide previous frame so that new frame can safely come on screen
def hideFrame(frame):
    try:
        frame.pack_forget()
        #print(f'Frame Hidden')
    except (TypeError, AttributeError):
        pass
        #print(f'Err: No Frame Found <<{AttributeError}>>')
    finally:
        return

def SignIn(frame):
    #Hiding any previous frame
    hideFrame(frame=frame)



