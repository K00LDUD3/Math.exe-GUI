#Importing required libs and mods
from tkinter import *
from tkinter import ttk
import Special_Numbers as spn
import tkinter.font as font
import random
import math
import GenFunctions as gfunc

#Creating WINDOW for hosting FRAMES
root = Tk()
root.title('Math.exe')
#root.resizable(False, False)
root.geometry("365x150")


#Creating FRAMES for hosting WIDGETS
initSignInUp_frame = LabelFrame(root) #Signing in or signing up
signIn_frame = LabelFrame(root) #Signing in 
signUp_frame = LabelFrame(root) #Signing up

homescreen_frame = LabelFrame(root) #Main screen

editProfile_frame = LabelFrame(root) #Editing profile
delProf_frame = LabelFrame(root) #Deleting account
changeUser_frame = LabelFrame(root) #Changing username
changePass_frame = LabelFrame(root) #Changeing Password

calcMenu_frame = LabelFrame(root) #Calculator menu for selecting various calculators
normCalc_frame = LabelFrame(root) #Normal calc with buttons
quadCalc_frame = LabelFrame(root) #Quadratic equation calc
baseCalc_frame = LabelFrame(root) #Base-N calc
vectCalc_frame = LabelFrame(root) #Vector calc
basicFuncCalc_frame = LabelFrame(root) #Basic function calc (HCF, LCM, factorial)

specNum_frame = LabelFrame(root) #Spec number programs

initGG_frame = LabelFrame(root) #Guessing game menu
guessG_frame = LabelFrame(root) #Guessing game 


#GLOBAL vars for using across methods
is_guest = True
no_tries = 0
calc_button_list = []


#Creating hide frame function
#Used to hide previous frame so that new frame can safely come on screen
def hideFrame(frame):
    try:
        frame.pack_forget()
        print(f'Frame Hidden')
    except (TypeError, AttributeError):
        print(f'Err: No Frame Found <<{AttributeError}>>')
    finally:
        return
    
def initSignInUp(frame):
    hideFrame(frame)

    #Resetting is_guest
    global is_guest
    is_guest = True 

    #Defining button DICTIONARIES for BUTTONS
    signInUp_b_dic = {
        'master':initSignInUp_frame,
        'act_bg':'blue',
        'act_fg':'yellow',
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
        'w':15,
        'wraplength':None
    }

    #Defining grid() DICTIONARIES for grid func
    signInUp_g_dic = {
        'column':0,
        'row':0,
        'cspan':1,
        'rspan':1,
        'padx':10,
        'pady':10,
        'ipadx':2,
        'ipady':2
    }

    #row 1
    b_signIn = gfunc.GenFunc('button', signInUp_b_dic, 'Sign In', signInUp_g_dic)

    #row 2
    signInUp_g_dic['row'] = 1
    b_guest = gfunc.GenFunc('button', signInUp_b_dic, 'Sign Up', signInUp_g_dic)
    
    #row 3
    signInUp_g_dic['row'] = 2
    b_guest = gfunc.GenFunc('button', signInUp_b_dic, 'Continue As Guest', signInUp_g_dic)
    b_guest.widg.config(command= lambda: homescreen(initSignInUp_frame))

    #Showing FRAME
    initSignInUp_frame.pack()
    return

def homescreen(frame):
    hideFrame(frame)

    #Defining button DICTIONARIES for BUTTONS
    homescreen_b_dic = {
        'master':homescreen_frame,
        'act_bg':'blue',
        'act_fg':'yellow',
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
        'w':15,
        'wraplength':None
    }
    homescreen_g_dic = {
        'column':0,
        'row':0,
        'cspan':1,
        'rspan':1,
        'padx':10,
        'pady':10,
        'ipadx':2,
        'ipady':2
    }

    #Row 1
    b_specNum = gfunc.GenFunc('button', homescreen_b_dic, 'Special Numbers', homescreen_g_dic)
    homescreen_g_dic['column'] = 1
    b_guessG = gfunc.GenFunc('button', homescreen_b_dic, 'Guessing Game', homescreen_g_dic)
    b_guessG.widg.config(command= lambda: initGG(homescreen_frame))
    #Row 2
    homescreen_g_dic['row'] = 1
    homescreen_g_dic['column'] = 0
    b_signOut = gfunc.GenFunc('button', homescreen_b_dic, 'Sign Out', homescreen_g_dic)
    b_signOut.widg.config(command= lambda: initSignInUp(homescreen_frame))
    homescreen_g_dic['column'] = 1
    b_calc = gfunc.GenFunc('button', homescreen_b_dic, 'Calculators', homescreen_g_dic)

    #Row 3
    homescreen_g_dic['row'] = 2
    homescreen_g_dic['column'] = 0
    global is_guest
    if not(is_guest):
        b_editProf = gfunc.GenFunc('button', homescreen_b_dic, 'Edit Profile', homescreen_g_dic)

    homescreen_frame.pack()
    return

def initGG(frame):
    hideFrame(frame)

    initGG_l_dic = {
        'master':initGG_frame,
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
        'w':20,
        'wraplength':None
    }
    initGG_b_dic = {
        'master':initGG_frame,
        'act_bg':'blue',
        'act_fg':'yellow',
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
    initGG_g_dic = {
        'column':1,
        'row':0,
        'cspan':1,
        'rspan':1,
        'padx':10,
        'pady':10,
        'ipadx':0,
        'ipady':0
    }

    diff_list = [
        'Easy',
        'Medium',
        'Hard',
        'Insane',
        'God',
        'FOODMEN'
    ]

    #Row 1
    b_go = gfunc.GenFunc('button', initGG_b_dic, 'GO', initGG_g_dic)
    diff_list = [(str(i)+'. '+diff_list[i]+ ' Level') for i in range(len(diff_list))]
    combo = ttk.Combobox(initGG_frame, values= diff_list, state= 'readonly', width=20)
    combo.bind('<<ComboboxSelected>>', lambda event: diff_expl(l_range, combo.get()))
    combo.grid(row=0, column=0)
    combo.current(0)

    #Row 2
    initGG_g_dic['column'] = 0
    initGG_g_dic['row'] = 1
    l_range = gfunc.GenFunc('label', initGG_l_dic, '', initGG_g_dic)
    initGG_g_dic['column'] = 1
    b_back = gfunc.GenFunc('button', initGG_b_dic, 'Cancel', initGG_g_dic)

    diff_expl(l_range, combo.get())

    initGG_frame.pack()
    return
#Explaining ranges of difficulty
def diff_expl(label_obj, choice):
    choice = choice.split(' ')[1].lower()
    if choice == 'easy':
        label_obj.widg.config(text='set range')
    elif choice == 'medium':
        label_obj.widg.config(text='set range')
    elif choice == 'hard':
        label_obj.widg.config(text='set range')
    elif choice == 'insane':
        label_obj.widg.config(text='set range')
    elif choice == 'god':
        label_obj.widg.config(text='set range')
    elif choice == 'foodmen':
        label_obj.widg.config(text='set range')
    return

initSignInUp(None)
#Showing WINDOW
root.mainloop()

