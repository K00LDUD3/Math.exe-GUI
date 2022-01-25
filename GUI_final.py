from tkinter import *
#Importing required libs and mods
from tkinter import ttk
import Special_Numbers as spn
import tkinter.font as font
import random
import math
import GenFunctions as gfunc
import cmath
import mysql.connector
#from PIL import Image,ImageTk

#Connecting the Database
mydb = mysql.connector.connect(host="localhost", user="root" , password="shob25" , database="Math")

#Creating WINDOW for hosting FRAMES
root = Tk()
root.title('Math.exe')
#root.resizable(False, False)
root.geometry("365x150")
#photo = PhotoImage(file='Logo.png')
#root.iconphoto(False, photo)


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
is_guest = True #Used while checking if person is a guest or not
no_tries = 0 #Used in guessing game to count number of tries taken to guess the number
calc_button_list = [] #Used to encapsulate all calculator button objects
b1 = 2 #Base 1 in BaseN calculator (From what base)
b2 = 2 #Base 2 in BaseN calculator (To what base)
pass_dot = '\u2022'
calc_hist = [' ']
calc_ans = 0
current_user = ''
current_pass = ''

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
#Destroying label for showing explanation of special numbers as it creates problems once it opens the spn frame again
def destroySPNLab(label, frame):
    try:
        label.destroy()
        homescreen(frame)
    except:
        print('Unable to destroy label')
    finally:
        return

#Configuring root based on x-size, y-size and title
def configRoot(x, y, title):
    root.title(title)
    try:
        root.geometry(str(f'{x}x{y}'))
    finally:
        return
#Signing in or signing up
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
    b_signIn.widg.config(command= lambda: signIn(initSignInUp_frame))
    #row 2
    signInUp_g_dic['row'] = 1
    b_signUp = gfunc.GenFunc('button', signInUp_b_dic, 'Sign Up', signInUp_g_dic)
    b_signUp.widg.config(command= lambda: signUp(initSignInUp_frame))
    #row 3
    signInUp_g_dic['row'] = 2
    b_guest = gfunc.GenFunc('button', signInUp_b_dic, 'Exit', signInUp_g_dic)
    b_guest.widg.config(command= quit)

    #Showing FRAME
    initSignInUp_frame.pack()
    return

#Command for exit button
def quit():
    root.destroy()
    return
#For show/hide password
def switchButton(b1, b2):
    b1.place_forget()
    b2.place(relx=0.8)
    print('button switched')
    return
#Signing in
def signIn(frame):
    hideFrame(frame)

    #Setting is_guest as false
    global is_guest
    is_guest = False
    
    signIn_l_dic = {
        'master':signIn_frame,
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
        'w':15,
        'wraplength':None
    }
    signIn_b_dic = {
        'master':signIn_frame,
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
    signIn_e_dic = {
        'master':signIn_frame,
        'bd':None,
        'height':None,
        'w':20,
        'bg':None,
        'fg':None,
        'font':None,
        'insertofftime':None,
        'insertontime':None,
        'highlbg':None,
        'highlcolor':None,
        'cursor':None,
        'padx':None,
        'pady':None,
        'highthick':None,
        'charwidth':None,
        'relief':None,
        'yscrollcommand':None,
        'xscrollcommand':None,
    }
    signIn_g_dic = {
        'column':0,
        'row':0,
        'cspan':1,
        'rspan':1,
        'padx':10,
        'pady':10,
        'ipadx':0,
        'ipady':0
    }

    #Row 1
    l_user = gfunc.GenFunc('label', signIn_l_dic, 'Username:', signIn_g_dic)
    signIn_g_dic['column']+=1
    e_user = gfunc.GenFunc('entry', signIn_e_dic, StringVar(), signIn_g_dic)
    
    #Row 2
    signIn_g_dic['row']+= 1
    signIn_g_dic['column'] = 0
    l_pass = gfunc.GenFunc('label', signIn_l_dic, 'Password:', signIn_g_dic)
    signIn_g_dic['column']+=1
    e_pass = gfunc.GenFunc('entry', signIn_e_dic, '', signIn_g_dic)
    e_pass.widg.config(show=pass_dot)

    '''
    hide_photo = Image.open('Hide.png')
    resized_image= hide_photo.resize((20,12), Image.ANTIALIAS)
    hide_photo= ImageTk.PhotoImage(resized_image)

    show_photo = Image.open('Show.png')
    resized_image= show_photo.resize((20,12), Image.ANTIALIAS)
    show_photo= ImageTk.PhotoImage(resized_image)
    '''

    #Row 3
    signIn_g_dic['row']+= 1
    signIn_g_dic['column'] = 0
    signIn_g_dic['cspan'] = 2
    l_op = gfunc.GenFunc('label', signIn_l_dic, None, signIn_g_dic)
    signIn_g_dic['cspan'] = 1

    #Row 4
    signIn_b_dic['w'] = 15
    signIn_g_dic['row']+= 1
    signIn_g_dic['column'] = 0
    b_back = gfunc.GenFunc('button', signIn_b_dic, 'Back', signIn_g_dic)
    b_back.widg.config(command= lambda: initSignInUp(signIn_frame))
    signIn_g_dic['column']+=1
    b_signIn = gfunc.GenFunc('button', signIn_b_dic, 'Sign In', signIn_g_dic)
    b_signIn.widg.config(command= lambda: SignInVer(l_op, e_user.widg.get(), e_pass.widg.get()))
   
    signIn_frame.pack()
    return

#Signing in
def signUp(frame):
    hideFrame(frame)

    #Setting is_guest as false
    global is_guest
    is_guest = False

    signUp_l_dic = {
        'master':signUp_frame,
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
        'w':15,
        'wraplength':None
    }
    signUp_b_dic = {
        'master':signUp_frame,
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
    signUp_e_dic = {
        'master':signUp_frame,
        'bd':None,
        'height':None,
        'w':20,
        'bg':None,
        'fg':None,
        'font':None,
        'insertofftime':None,
        'insertontime':None,
        'highlbg':None,
        'highlcolor':None,
        'cursor':None,
        'padx':None,
        'pady':None,
        'highthick':None,
        'charwidth':None,
        'relief':None,
        'yscrollcommand':None,
        'xscrollcommand':None,
    }
    signUp_g_dic = {
        'column':0,
        'row':0,
        'cspan':1,
        'rspan':1,
        'padx':10,
        'pady':10,
        'ipadx':0,
        'ipady':0
    }

    #Row 1
    l_user = gfunc.GenFunc('label', signUp_l_dic, 'Username:', signUp_g_dic)
    signUp_g_dic['column']+=1
    e_user = gfunc.GenFunc('entry', signUp_e_dic, StringVar(), signUp_g_dic)
    
    #Row 2
    signUp_g_dic['row']+= 1
    signUp_g_dic['column'] = 0
    l_pass = gfunc.GenFunc('label', signUp_l_dic, 'Password:', signUp_g_dic)
    signUp_g_dic['column']+=1
    e_pass = gfunc.GenFunc('entry', signUp_e_dic, StringVar(), signUp_g_dic)
    e_pass.widg.config(show=pass_dot)
    
    #Row 3
    signUp_g_dic['row']+= 1
    signUp_g_dic['column'] = 0
    l_passConf = gfunc.GenFunc('label', signUp_l_dic, 'Confirm Password:', signUp_g_dic)
    signUp_g_dic['column']+=1
    e_passConf = gfunc.GenFunc('entry', signUp_e_dic, StringVar(), signUp_g_dic)
    e_passConf.widg.config(show=pass_dot)
    
    #Row 4
    signUp_g_dic['row']+= 1
    signUp_g_dic['column'] = 0
    signUp_g_dic['cspan'] = 2
    l_op = gfunc.GenFunc('label', signUp_l_dic, '', signUp_g_dic)
    signUp_g_dic['cspan'] = 1

    #Row 5
    signUp_g_dic['row']+= 1
    signUp_g_dic['column'] = 0
    b_back = gfunc.GenFunc('button', signUp_b_dic, 'Back', signUp_g_dic)
    b_back.widg.config(command= lambda: initSignInUp(signUp_frame))
    signUp_g_dic['column']+=1
    b_signUp = gfunc.GenFunc('button', signUp_b_dic, 'Sign Up', signUp_g_dic)
    b_signUp.widg.config(command= lambda: signUpVer(l_op, e_user.widg.get(), e_pass.widg.get(), e_passConf.widg.get()))
    
    #Row 6
    signUp_g_dic['row']+= 1
    signUp_g_dic['column'] = 1
    l_guest = gfunc.GenFunc('label', signUp_l_dic, 'Continue as Guest', signUp_g_dic)
    l_guest.widg.bind("<Button-1>", lambda e: switchGuestBool(signUp_frame))

    signUp_frame.pack()
    return
    


def switchGuestBool(frame):
    global is_guest
    is_guest = True

    homescreen(frame=frame)
    return
#Main screen 
def homescreen(frame):
    hideFrame(frame)

    #Defining param DICTIONARIES for WIDGETS
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
    b_specNum.widg.config(command= lambda: specNum(homescreen_frame))
    homescreen_g_dic['column'] = 1
    b_guessG = gfunc.GenFunc('button', homescreen_b_dic, 'Guessing Game', homescreen_g_dic)
    b_guessG.widg.config(command= lambda: initGG(homescreen_frame))

    #Row 2
    homescreen_g_dic['row'] += 1
    homescreen_g_dic['column'] = 0
    b_calc = gfunc.GenFunc('button', homescreen_b_dic, 'Calculators', homescreen_g_dic)
    b_calc.widg.config(command= lambda: calcMenu(homescreen_frame))
    homescreen_g_dic['column'] += 1
    

    #Row 3
    global is_guest
    if not(is_guest):
        configRoot(300, 150, 'Homescreen')
        homescreen_g_dic['column'] = 1
        b_editProf = gfunc.GenFunc('button', homescreen_b_dic, 'Edit Profile', homescreen_g_dic)
        b_editProf.widg.config(command= lambda: editProfile(homescreen_frame))
        homescreen_g_dic['row'] += 1
        homescreen_g_dic['column'] = 0
        homescreen_b_dic['w'] = 37
        homescreen_g_dic['cspan'] = 2
        b_signOut = gfunc.GenFunc('button', homescreen_b_dic, 'Sign Out', homescreen_g_dic)
        b_signOut.widg.config(command= lambda: initSignInUp(homescreen_frame))
    else:
        configRoot(300, 100, 'Homescreen')
        b_signOut = gfunc.GenFunc('button', homescreen_b_dic, 'Sign Out', homescreen_g_dic)
        b_signOut.widg.config(command= lambda: initSignInUp(homescreen_frame))
    homescreen_frame.pack()
    return

#Guessing game menu
def initGG(frame):
    hideFrame(frame)

    global no_tries
    no_tries = 0

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
    b_start = gfunc.GenFunc('button', initGG_b_dic, 'Start', initGG_g_dic)
    b_start.widg.config(command= lambda: guessG(initGG_frame, genNum(combo.get())))
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
    b_back.widg.config(command= lambda: homescreen(initGG_frame))

    diff_expl(l_range, combo.get())

    initGG_frame.pack()
    return
#Explaining ranges of difficulty
def diff_expl(label_obj, choice):
    choice = choice.split(' ')[1].lower()
    if choice == 'easy':
        label_obj.widg.config(text='0 -10')
    elif choice == 'medium':
        label_obj.widg.config(text='0 - 100')
    elif choice == 'hard':
        label_obj.widg.config(text='0 - 1000')
    elif choice == 'insane':
        label_obj.widg.config(text='0 - 10000')
    elif choice == 'god':
        label_obj.widg.config(text='0 - 100000')
    elif choice == 'foodmen':
        label_obj.widg.config(text='-1000000000 - 1000000000')
    return

#Guessing game 
def guessG(frame, number):
    hideFrame(frame)

    guessG_l_dic = {
        'master':guessG_frame,
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
        'w':15,
        'wraplength':None
    }
    guessG_b_dic = {
        'master':guessG_frame,
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
    guessG_e_dic = {
        'master':guessG_frame,
        'bd':None,
        'height':None,
        'w':15,
        'bg':None,
        'fg':None,
        'font':None,
        'insertofftime':None,
        'insertontime':None,
        'highlbg':None,
        'highlcolor':None,
        'cursor':None,
        'padx':None,
        'pady':None,
        'highthick':None,
        'charwidth':None,
        'relief':None,
        'yscrollcommand':None,
        'xscrollcommand':None,
    }
    guessG_g_dic = {
        'column':0,
        'row':0,
        'cspan':1,
        'rspan':1,
        'padx':10,
        'pady':10,
        'ipadx':0,
        'ipady':0
    }
    
    #Row 1
    l_promptGuess = gfunc.GenFunc('label', guessG_l_dic, 'Guess a number:', guessG_g_dic)
    guessG_g_dic['column'] = 1
    e_guess = gfunc.GenFunc('entry', guessG_e_dic, StringVar(), guessG_g_dic)
    
    #Row 2
    guessG_g_dic['column'] = 0
    guessG_g_dic['row'] = 1
    guessG_g_dic['cspan'] = 2
    guessG_l_dic['w'] = 20
    l_op = gfunc.GenFunc('label', guessG_l_dic, '', guessG_g_dic)

    #Row 3
    guessG_g_dic['row'] = 2
    guessG_g_dic['cspan'] = 1
    b_back = gfunc.GenFunc('button', guessG_b_dic, 'Back', guessG_g_dic)
    b_back.widg.config(command= lambda: initGG(guessG_frame))
    guessG_g_dic['column'] = 1
    b_guess = gfunc.GenFunc('button', guessG_b_dic, 'Guess', guessG_g_dic)
    b_guess.widg.config(command= lambda: validateNum(str(e_guess.widg.get()), number, l_op, b_guess))
    
    guessG_frame.pack()
    return
    #Generating a random mnumber with min range and max range
def genNum(choice):
    choice = choice.split(' ')[1].lower()
    number = 0
    if choice == 'easy':
        number = random.randint(0,10)
        r = '0 - 10'
    elif choice == 'medium':
        number = random.randint(0,100)
        r = '0 - 100'
    elif choice == 'hard':
        number = random.randint(0,1000)
        r = '0 - 1000'
    elif choice == 'insane':
        number = random.randint(0,10000)
        r = '0 - 100000'
    elif choice == 'god':
        number = random.randint(0,100000)
        r = '0 - 1000000'
    elif choice == 'foodmen':
        number = random.randint(-1000000000, 1000000000)
        root.title(f'Guessing Game: -1000000000 - 1000000000')
        print(f'{number=}')
        return number
    root.title(f'Guessing Game: {r}')
    return number
#checking if  guess is correct for guessing game
def validateNum(num, val_num, label_obj, button_obj):
    global no_tries
    try:
        num = int(num.strip())
        if num == val_num:
            no_tries+=1
            mess = f'Correct! Number of tries: {no_tries}'
            button_obj.widg.config(state='disabled')
        elif num < val_num:
            no_tries+=1
            mess = 'Try guessing higher!'
        elif num > val_num:
            no_tries+=1
            mess = 'Try guessing lower!'
        label_obj.widg.config(text=mess)
    except:
        label_obj.widg.config(text='Invalid guess!')

def editProfile(frame):
    hideFrame(frame)

    eP_b_dic = {
        'master':editProfile_frame,
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
    eP_g_dic = {
        'column':0,
        'row':0,
        'cspan':1,
        'rspan':1,
        'padx':10,
        'pady':10,
        'ipadx':0,
        'ipady':0
    }

    #Row 1
    #b_changeUser = gfunc.GenFunc('button', eP_b_dic, 'Change Username', eP_g_dic)
    #b_changeUser.widg.config(command= lambda: changeUser(editProfile_frame))
    
    #Row 2
    #eP_g_dic['row'] += 1
    b_changePass = gfunc.GenFunc('button', eP_b_dic, 'Change Password', eP_g_dic)
    b_changePass.widg.config(command= lambda: changePass(editProfile_frame))

    #Row 3
    eP_g_dic['row'] += 1
    b_delAcct = gfunc.GenFunc('button', eP_b_dic, 'Delete Account', eP_g_dic)
    b_delAcct.widg.config(command= lambda: delProf(editProfile_frame))

    #Row 4
    eP_g_dic['row'] += 1
    b_back = gfunc.GenFunc('button', eP_b_dic, 'Cancel', eP_g_dic)
    b_back.widg.config(command= lambda: homescreen(editProfile_frame))

    editProfile_frame.pack()
    return

def changeUser(frame):
    hideFrame(frame)

    changeU_l_dic = {
        'master':changeUser_frame,
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
        'w':15,
        'wraplength':None
    }
    changeU_b_dic = {
        'master':changeUser_frame,
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
    changeU_e_dic = {
        'master':changeUser_frame,
        'bd':None,
        'height':None,
        'w':15,
        'bg':None,
        'fg':None,
        'font':None,
        'insertofftime':None,
        'insertontime':None,
        'highlbg':None,
        'highlcolor':None,
        'cursor':None,
        'padx':None,
        'pady':None,
        'highthick':None,
        'charwidth':None,
        'relief':None,
        'yscrollcommand':None,
        'xscrollcommand':None,
    }
    changeU_g_dic = {
        'column':0,
        'row':0,
        'cspan':1,
        'rspan':1,
        'padx':10,
        'pady':10,
        'ipadx':0,
        'ipady':0
    }

    #Row 1
    l_user = gfunc.GenFunc('label',changeU_l_dic, 'Old Username:', changeU_g_dic)
    changeU_g_dic['column'] += 1
    e_user = gfunc.GenFunc('entry', changeU_e_dic, StringVar(), changeU_g_dic)

    #Row 2
    changeU_g_dic['column'] = 0
    changeU_g_dic['row'] += 1
    l_newUser = gfunc.GenFunc('label', changeU_l_dic, 'New Username:', changeU_g_dic)
    changeU_g_dic['column'] += 1
    e_newUser = gfunc.GenFunc('entry', changeU_e_dic, StringVar(), changeU_g_dic)

    #Row 3
    changeU_g_dic['column'] = 0
    changeU_g_dic['row'] += 1
    l_pass = gfunc.GenFunc('label', changeU_l_dic, 'Password:', changeU_g_dic)
    changeU_g_dic['column'] += 1
    e_pass = gfunc.GenFunc('entry', changeU_e_dic, StringVar(), changeU_g_dic)
    e_pass.widg.config(show=pass_dot)

    #Row 4
    changeU_g_dic['column'] = 0
    changeU_g_dic['row'] += 1
    changeU_g_dic['cspan'] = 2
    l_op = gfunc.GenFunc('label', changeU_l_dic, '<OUTPUT>', changeU_g_dic)
    changeU_g_dic['cspan'] = 1

    #Row 5
    changeU_g_dic['column'] = 0
    changeU_g_dic['row'] += 1
    b_back = gfunc.GenFunc('Button', changeU_b_dic, 'Back', changeU_g_dic)
    b_back.widg.config(command= lambda: editProfile(changeUser_frame))
    changeU_g_dic['column'] += 1
    b_go = gfunc.GenFunc('Button', changeU_b_dic, 'Change Username', changeU_g_dic)
    b_go.widg.config(command= lambda: changeUserVer(l_op, e_user.widg.get(), e_newUser.widg.get(), e_pass.widg.get()))

    changeUser_frame.pack()
    return

def changePass(frame):
    hideFrame(frame)
    changeP_l_dic = {
        'master':changePass_frame,
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
        'w':15,
        'wraplength':None
    }
    changeP_b_dic = {
        'master':changePass_frame,
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
    changeP_e_dic = {
        'master':changePass_frame,
        'bd':None,
        'height':None,
        'w':15,
        'bg':None,
        'fg':None,
        'font':None,
        'insertofftime':None,
        'insertontime':None,
        'highlbg':None,
        'highlcolor':None,
        'cursor':None,
        'padx':None,
        'pady':None,
        'highthick':None,
        'charwidth':None,
        'relief':None,
        'yscrollcommand':None,
        'xscrollcommand':None,
    }
    changeP_g_dic = {
        'column':0,
        'row':0,
        'cspan':1,
        'rspan':1,
        'padx':10,
        'pady':10,
        'ipadx':0,
        'ipady':0
    }

    #Row 1
    l_user = gfunc.GenFunc('label',changeP_l_dic, 'Username:', changeP_g_dic)
    changeP_g_dic['column'] += 1
    e_user = gfunc.GenFunc('entry', changeP_e_dic, StringVar(), changeP_g_dic)

    #Row 2
    changeP_g_dic['column'] = 0
    changeP_g_dic['row'] += 1
    l_pass = gfunc.GenFunc('label', changeP_l_dic, 'Password:', changeP_g_dic)
    changeP_g_dic['column'] += 1
    e_pass = gfunc.GenFunc('entry', changeP_e_dic, StringVar(), changeP_g_dic)
    e_pass.widg.config(show=pass_dot)

    #Row 3
    changeP_g_dic['column'] = 0
    changeP_g_dic['row'] += 1
    l_newPass = gfunc.GenFunc('label', changeP_l_dic, 'New Password:', changeP_g_dic)
    changeP_g_dic['column'] += 1
    e_newPass = gfunc.GenFunc('entry', changeP_e_dic, StringVar(), changeP_g_dic)
    e_newPass.widg.config(show=pass_dot)

    #Row 4
    changeP_g_dic['column'] = 0
    changeP_g_dic['row'] += 1
    l_newPassConf = gfunc.GenFunc('label', changeP_l_dic, 'Confirm Password:', changeP_g_dic)
    changeP_g_dic['column'] += 1
    e_newPassConf = gfunc.GenFunc('entry', changeP_e_dic, StringVar(), changeP_g_dic)
    e_newPassConf.widg.config(show=pass_dot)

    #Row 5
    changeP_g_dic['column'] = 0
    changeP_g_dic['row'] += 1
    changeP_g_dic['cspan'] = 2
    changeP_l_dic['w'] = 30
    l_op = gfunc.GenFunc('label', changeP_l_dic, '', changeP_g_dic)
    changeP_g_dic['cspan'] = 1

    #Row 6
    changeP_g_dic['column'] = 0
    changeP_g_dic['row'] += 1
    b_back = gfunc.GenFunc('Button', changeP_b_dic, 'Back', changeP_g_dic)
    b_back.widg.config(command= lambda: editProfile(changePass_frame))
    changeP_g_dic['column'] += 1
    b_go = gfunc.GenFunc('Button', changeP_b_dic, 'Change Password', changeP_g_dic)
    b_go.widg.config(command= lambda: changePassVer(l_op, e_user.widg.get(), e_pass.widg.get(), e_newPass.widg.get(), e_newPassConf.widg.get()))

    changePass_frame.pack()
    return

def delProf(frame):
    hideFrame(frame)

    delProf_l_dic = {
        'master':delProf_frame,
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
        'w':15,
        'wraplength':None
    }
    delProf_b_dic = {
        'master':delProf_frame,
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
        'w':5,
        'wraplength':None
    }
    delProf_e_dic = {
        'master':delProf_frame,
        'bd':None,
        'height':None,
        'w':15,
        'bg':None,
        'fg':None,
        'font':None,
        'insertofftime':None,
        'insertontime':None,
        'highlbg':None,
        'highlcolor':None,
        'cursor':None,
        'padx':None,
        'pady':None,
        'highthick':None,
        'charwidth':None,
        'relief':None,
        'yscrollcommand':None,
        'xscrollcommand':None,
    }
    delProf_g_dic = {
        'column':0,
        'row':0,
        'cspan':1,
        'rspan':1,
        'padx':10,
        'pady':10,
        'ipadx':0,
        'ipady':0
    }
    '''
    #Row 1
    l_user = gfunc.GenFunc('label',delProf_l_dic, 'Username:', delProf_g_dic)
    delProf_g_dic['column'] += 1
    e_user = gfunc.GenFunc('entry', delProf_e_dic, StringVar(), delProf_g_dic)

    #Row 2
    delProf_g_dic['column'] = 0
    delProf_g_dic['row'] += 1
    l_pass = gfunc.GenFunc('label', delProf_l_dic, 'Password:', delProf_g_dic)
    delProf_g_dic['column'] += 1
    e_pass = gfunc.GenFunc('entry', delProf_e_dic, StringVar(), delProf_g_dic)
    e_pass.widg.config(show=pass_dot)

    #Row 3
    delProf_g_dic['column'] = 0
    delProf_g_dic['row'] += 1
    l_passConf = gfunc.GenFunc('label', delProf_l_dic, 'Confirm Password:', delProf_g_dic)
    delProf_g_dic['column'] += 1
    e_passConf = gfunc.GenFunc('entry', delProf_e_dic, StringVar(), delProf_g_dic)
    e_passConf.widg.config(show=pass_dot)

    #Row 4
    delProf_g_dic['column'] = 0
    delProf_g_dic['row'] += 1
    delProf_g_dic['cspan'] = 2
    l_op = gfunc.GenFunc('label', delProf_l_dic, '<OUTPUT>', delProf_g_dic)
    delProf_g_dic['cspan'] = 1
    '''

    #Row 1
    delProf_g_dic['cspan'] = 2
    delProf_l_dic['w'] = 20
    l_prompt = gfunc.GenFunc('label', delProf_l_dic, 'Are you sure about that?', delProf_g_dic)

    #Row 2
    delProf_g_dic['column'] = 0
    delProf_g_dic['row'] += 1
    b_back = gfunc.GenFunc('Button', delProf_b_dic, 'No', delProf_g_dic)
    b_back.widg.config(command= lambda: editProfile(delProf_frame))
    delProf_g_dic['column'] += 1
    b_go = gfunc.GenFunc('Button', delProf_b_dic, 'Yes', delProf_g_dic)
    b_go.widg.config(command= lambda: delPofileVer())

    delProf_frame.pack()
    return
#Calculator menu
def calcMenu(frame):
    hideFrame(frame)
    #Defining param DICTIONARIES for WIDGETS
    cm_b_dic = {
        'master':calcMenu_frame,
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
        'w':25,
        'wraplength':None
    }
    cm_g_dic = {
        'column':0,
        'row':0,
        'cspan':1,
        'rspan':1,
        'padx':10,
        'pady':10,
        'ipadx':0,
        'ipady':0
    }

    #6 Rows (not sure what happened to two more XD)
    b_calc = gfunc.GenFunc('button', cm_b_dic, 'Normal Calculator', cm_g_dic)
    b_calc.widg.config(command= lambda: normCalc(calcMenu_frame))
    cm_g_dic['row'] +=1
    b_baseN = gfunc.GenFunc('button', cm_b_dic, 'Base-N Calculator', cm_g_dic)
    b_baseN.widg.config(command= lambda: baseCalc(calcMenu_frame))
    cm_g_dic['row'] +=1
    b_quad = gfunc.GenFunc('button', cm_b_dic, 'Quadratic Equation Calculator', cm_g_dic)
    b_quad.widg.config(command= lambda: quadCalc(calcMenu_frame))
    cm_g_dic['row'] +=1
    b_back = gfunc.GenFunc('button', cm_b_dic, 'Back', cm_g_dic)
    b_back.widg.config(command= lambda: homescreen(calcMenu_frame))
    cm_g_dic['row'] +=1

    calcMenu_frame.pack()
    return

def normCalc(frame):
    hideFrame(frame)

    normCalc_b_dic = {
        'master':normCalc_frame,
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
        'w':5,
        'wraplength':None
    }
    normCalc_l_dic = {
        'master':normCalc_frame,
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
        'w':15,
        'wraplength':None
    }
    normCalc_g_dic = {
        'column':0,
        'row':0,
        'cspan':1,
        'rspan':1,
        'padx':5,
        'pady':5,
        'ipadx':5,
        'ipady':5
    }

    #Display Label
    normCalc_g_dic['cspan'] = 5
    l_op = gfunc.GenFunc('label', normCalc_l_dic, '', normCalc_g_dic)
    normCalc_g_dic['cspan'] = 1

    #Number buttons
    normCalc_g_dic['row'] += 1
    row_offest = 0
    col_offest = 0
    for i in range(0,9):
        normCalc_g_dic['row'] = i//3+1 + row_offest
        normCalc_g_dic['column'] =  i%3 + col_offest
        calc_button_list.append(gfunc.GenFunc('button', normCalc_b_dic, str(i+1), normCalc_g_dic))
    normCalc_g_dic['row'] += 1
    normCalc_g_dic['column'] = 1
    calc_button_list.append(gfunc.GenFunc('button', normCalc_b_dic, '0', normCalc_g_dic))
    #Assigning commands of the number buttons
    calc_button_list[0].widg.config(command= lambda: addNumOp(1, l_op))
    calc_button_list[1].widg.config(command= lambda: addNumOp(2, l_op))
    calc_button_list[2].widg.config(command= lambda: addNumOp(3, l_op))
    calc_button_list[3].widg.config(command= lambda: addNumOp(4, l_op))
    calc_button_list[4].widg.config(command= lambda: addNumOp(5, l_op))
    calc_button_list[5].widg.config(command= lambda: addNumOp(6, l_op))
    calc_button_list[6].widg.config(command= lambda: addNumOp(7, l_op))
    calc_button_list[7].widg.config(command= lambda: addNumOp(8, l_op))
    calc_button_list[8].widg.config(command= lambda: addNumOp(9, l_op))
    calc_button_list[9].widg.config(command= lambda: addNumOp(0, l_op))
    
    #Decimal button (.)
    normCalc_g_dic['column'] = 0
    b_dot = gfunc.GenFunc('button', normCalc_b_dic, '.', normCalc_g_dic)
    b_dot.widg.config(command= lambda: addNumOp('.', l_op))

    #Equals sign (=)
    normCalc_g_dic['column'] = 2 + col_offest
    b_eval = gfunc.GenFunc('button', normCalc_b_dic, '=', normCalc_g_dic)
    b_eval.widg.config(command= lambda: evalExp(l_op.widg.cget('text'), l_op))

    #Column 4
    normCalc_g_dic['column'] = 3 + col_offest
    normCalc_g_dic['row'] = 1 + row_offest
    b_add = gfunc.GenFunc('button', normCalc_b_dic, '+', normCalc_g_dic)
    b_add.widg.config(command= lambda: addNumOp('+', l_op))

    normCalc_g_dic['row'] += 1
    b_sub = gfunc.GenFunc('button', normCalc_b_dic, '-', normCalc_g_dic)
    b_sub.widg.config(command= lambda: addNumOp('-', l_op))

    normCalc_g_dic['row'] += 1
    b_mult = gfunc.GenFunc('button', normCalc_b_dic, 'x', normCalc_g_dic)
    b_mult.widg.config(command= lambda: addNumOp('*', l_op))

    normCalc_g_dic['row'] += 1
    b_div = gfunc.GenFunc('button', normCalc_b_dic, '/', normCalc_g_dic)
    b_div.widg.config(command= lambda: addNumOp('/', l_op))

    normCalc_g_dic['row'] += 1
    b_mod = gfunc.GenFunc('button', normCalc_b_dic, 'mod', normCalc_g_dic)
    b_mod.widg.config(command= lambda: addNumOp('%', l_op))

    #Last Row
    normCalc_g_dic['row'] = 5
    normCalc_g_dic['column'] = 0
    b_back = gfunc.GenFunc('button', normCalc_b_dic, 'Back', normCalc_g_dic)
    b_back.widg.config(command= lambda: calcMenu(normCalc_frame))

    #Delete button
    normCalc_g_dic['column'] += 1
    b_del = gfunc.GenFunc('button', normCalc_b_dic, 'Del', normCalc_g_dic)
    b_del.widg.config(command= lambda: delete(l_op.widg.cget('text'), l_op, 1))

    #Clear button
    normCalc_g_dic['column'] += 1
    b_clear = gfunc.GenFunc('button', normCalc_b_dic, 'Clear', normCalc_g_dic)
    b_clear.widg.config(command= lambda: delete(l_op.widg.cget('text'), l_op, 2))

    #Column 5
    normCalc_g_dic['column'] = 4
    normCalc_g_dic['row'] = 1
    b_undo = gfunc.GenFunc('button', normCalc_b_dic, 'UNDO', normCalc_g_dic)
    b_undo.widg.config(command= lambda: undo(l_op.widg.cget('text'), l_op))
    #normCalc_g_dic['row'] += 1
    #b_redo = gfunc.GenFunc('button', normCalc_b_dic, 'REDO', normCalc_g_dic)
    #b_redo.widg.config(command= lambda: undoRedo(l_op.widg.cget('text'), l_op, 'REDO'))
    normCalc_g_dic['row'] += 1
    b_exponent = gfunc.GenFunc('button', normCalc_b_dic, '^', normCalc_g_dic)
    b_exponent.widg.config(command= lambda: addNumOp('^', l_op))
    normCalc_g_dic['row'] += 1
    b_ans = gfunc.GenFunc('button', normCalc_b_dic, 'Ans', normCalc_g_dic)
    b_ans.widg.config(command= lambda: getCalcAns(l_op))
    normCalc_g_dic['row'] += 1
    b_openB = gfunc.GenFunc('button', normCalc_b_dic, '(', normCalc_g_dic)
    b_openB.widg.config(command= lambda: addNumOp('(', l_op))
    normCalc_g_dic['row'] += 1
    b_closeB = gfunc.GenFunc('button', normCalc_b_dic, ')', normCalc_g_dic)
    b_closeB.widg.config(command= lambda: addNumOp(')', l_op))

    normCalc_frame.pack()
    return
#Deleting a character from the expression
def delete(exp, label_obj, op):
    exp = str(exp).strip()
    if exp == 'ERROR' or op == 2:
        label_obj.widg.config(text='')
    else:
        label_obj.widg.config(text=exp[:-1])
    return
#Displaying previous/next exppression
def undo(exp, l_obj):
    exp = str(exp)
    if exp == '':
        return
    global calc_hist
    ind = calc_hist.index(exp)
    if ind == 0:
        print(f'Redo not possible because current step at 0th index of {calc_hist}')
        return
    else:
        l_obj.widg.config(text=calc_hist[-2])
    del calc_hist[-1]
    print(calc_hist)
    return
#Getting last known answer
def getCalcAns(l_obj):
    global calc_ans
    if l_obj.widg.cget('text') == 'ERROR':
        l_obj.widg.config(text='')

    txt = str(l_obj.widg.cget('text'))
    if txt == '':
        l_obj.widg.config(text= calc_ans)
    operators = '+-*/%^'
    if str(l_obj.widg.cget('text'))[-1] in operators:
        txt = f'{txt} {calc_ans}'
    else:
        txt = f'{txt}{calc_ans}'
    l_obj.widg.config(text= txt)
    return

#Evaluating expression
def evalExp(exp, label_obj):
    exp = str(exp)
    
    global calc_hist    
    exp = exp.replace(' ^ ', '**')

    try:
        val = eval(exp)
    except:
        val = 'ERROR'
    label_obj.widg.config(text= val)
    exp = str(label_obj.widg.cget('text')).strip()
    if calc_hist[-1] != exp and exp != 'ERROR':
        calc_hist.append(exp)
        global calc_ans
        calc_ans = float(exp)
        print(calc_ans)
    print(calc_hist)
    return
#Function for adding stuff
def addNumOp(val, label_obj):
    if label_obj.widg.cget('text') == 'ERROR':
        label_obj.widg.config(text='')
    print(val)

    txt = str(label_obj.widg.cget('text'))

        
    print(f'{txt=}')
    operators = '+-*/%()^'
    val = str(val)

    if val.isnumeric() or str(val) == '.':
        try:
            if txt.endswith((operators,)):
                print('exp ends with operator')
            else:
                txt = f'{txt}{val}'
            None
        except:
            None
    elif val in operators:
        txt = f'{txt} {val} '

    label_obj.widg.config(text= txt)
    exp = str(label_obj.widg.cget('text'))

    
    global calc_hist    
    if calc_hist[-1] != exp and exp != 'ERROR':
        calc_hist.append(exp)

    return

def baseCalc(frame):
    hideFrame(frame)

    base_list = [
        ('Base 2',2),
        ('Base 4',4),
        ('Base 8',8),
        ('Base 16',16),
    ]
    baseCalc_e_dic = {
        'master':baseCalc_frame,
        'bd':None,
        'height':None,
        'w':int(len(base_list)*12.5),
        'bg':None,
        'fg':None,
        'font':None,
        'insertofftime':None,
        'insertontime':None,
        'highlbg':None,
        'highlcolor':None,
        'cursor':None,
        'padx':None,
        'pady':None,
        'highthick':None,
        'charwidth':None,
        'relief':None,
        'yscrollcommand':None,
        'xscrollcommand':None,
    }
    baseCalc_l_dic = {
        'master':baseCalc_frame,
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
        'w':15,
        'wraplength':None
    }
    baseCalc_b_dic = {
        'master':baseCalc_frame,
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
    baseCalc_g_dic = {
        'column':0,
        'row':0,
        'cspan':1,
        'rspan':1,
        'padx':10,
        'pady':10,
        'ipadx':0,
        'ipady':0
    }
    #Row 1

    l_inpPrompt = gfunc.GenFunc('label', baseCalc_l_dic, 'Enter number:', baseCalc_g_dic)
    baseCalc_g_dic['column']+=1
    baseCalc_g_dic['cspan'] = len(base_list)
    e_inp = gfunc.GenFunc('entry', baseCalc_e_dic, StringVar(), baseCalc_g_dic)
    baseCalc_g_dic['cspan'] = 1
    baseCalc_g_dic['column']+=len(base_list)
    b_go = gfunc.GenFunc('button', baseCalc_b_dic, 'Convert', baseCalc_g_dic)
    b_go.widg.config(command= lambda: convertBase(e_inp.widg.get(), l_op, l_err))

    #Row 2
    baseCalc_g_dic['row']+=1
    baseCalc_g_dic['column'] = 0
    l_fromBase = gfunc.GenFunc('label', baseCalc_l_dic, 'From:', baseCalc_g_dic)
    baseCalc_g_dic['column']+=1
    inp_bases = []
    base_var_inp = IntVar()
    base_var_inp.set(2)
    '''for text, mode in base_list:
        x = ttk.Radiobutton(master=baseCalc_frame, text=text, variable=base_var_inp, value=mode).grid(row=baseCalc_g_dic['row'], column=baseCalc_g_dic['column'])
        baseCalc_g_dic['column']+=1'''
    #Creating each radio button separately as there is no way to set commands properly using loops
    inp_base_2 = Radiobutton(master=baseCalc_frame, text='Base 2', variable=base_var_inp, value=2, command= lambda: setGlobalBase(2, 1)).grid(row=baseCalc_g_dic['row'], column=baseCalc_g_dic['column'])
    baseCalc_g_dic['column']+=1
    inp_base_8 = Radiobutton(master=baseCalc_frame, text='Base 8', variable=base_var_inp, value=8, command= lambda: setGlobalBase(8, 1)).grid(row=baseCalc_g_dic['row'], column=baseCalc_g_dic['column'])
    baseCalc_g_dic['column']+=1
    inp_base_10 = Radiobutton(master=baseCalc_frame, text='Base 10', variable=base_var_inp, value=10, command= lambda: setGlobalBase(10, 1)).grid(row=baseCalc_g_dic['row'], column=baseCalc_g_dic['column'])
    baseCalc_g_dic['column']+=1
    inp_base_16 = Radiobutton(master=baseCalc_frame, text='Base 16', variable=base_var_inp, value=16, command= lambda: setGlobalBase(16, 1)).grid(row=baseCalc_g_dic['row'], column=baseCalc_g_dic['column'])
    baseCalc_g_dic['column']+=1

    #Row 2 & 3
    baseCalc_g_dic['rspan'] = 2
    l_err = gfunc.GenFunc('label', baseCalc_l_dic, '', baseCalc_g_dic)
    l_err.widg.config(wraplength=100)
    baseCalc_g_dic['rspan'] = 1

    #Row 3
    baseCalc_g_dic['row']+=1
    baseCalc_g_dic['column'] =0
    l_toBase = gfunc.GenFunc('label', baseCalc_l_dic, 'To:', baseCalc_g_dic)
    baseCalc_g_dic['column']+=1
    op_bases = []
    base_var_op = IntVar()
    base_var_op.set(2)
    '''for text, mode in base_list:
        op_bases.append(Radiobutton(master=baseCalc_frame, text=text, variable=base_var_op, value=mode, padx=10).grid(row=baseCalc_g_dic['row'], column=baseCalc_g_dic['column']))
        baseCalc_g_dic['column']+=1'''
    #Creating each radio button separately as there is no way to set commands properly using loops
    op_base_2 = Radiobutton(master=baseCalc_frame, text='Base 2', variable=base_var_op, value=2, command= lambda: setGlobalBase(2, 2)).grid(row=baseCalc_g_dic['row'], column=baseCalc_g_dic['column'])
    baseCalc_g_dic['column']+=1
    op_base_8 = Radiobutton(master=baseCalc_frame, text='Base 8', variable=base_var_op, value=8, command= lambda: setGlobalBase(8, 2)).grid(row=baseCalc_g_dic['row'], column=baseCalc_g_dic['column'])
    baseCalc_g_dic['column']+=1
    op_base_10 = Radiobutton(master=baseCalc_frame, text='Base 10', variable=base_var_op, value=10, command= lambda: setGlobalBase(10, 2)).grid(row=baseCalc_g_dic['row'], column=baseCalc_g_dic['column'])
    baseCalc_g_dic['column']+=1
    op_base_16 = Radiobutton(master=baseCalc_frame, text='Base 16', variable=base_var_op, value=16, command= lambda: setGlobalBase(16, 2)).grid(row=baseCalc_g_dic['row'], column=baseCalc_g_dic['column'])
    baseCalc_g_dic['column']+=1

    #Row 4
    baseCalc_g_dic['row']+=1
    baseCalc_g_dic['column'] =0
    b_back = gfunc.GenFunc('button', baseCalc_b_dic, 'Back', baseCalc_g_dic)
    b_back.widg.config(command= lambda: calcMenu(baseCalc_frame))
    baseCalc_g_dic['column']+=1
    baseCalc_g_dic['cspan'] = len(base_list)
    baseCalc_l_dic['w'] = int(len(base_list)*11)
    l_op = gfunc.GenFunc('label', baseCalc_l_dic, '', baseCalc_g_dic)
    baseCalc_g_dic['cspan'] = 1

    baseCalc_frame.pack()
    return
#Setting global bases
def setGlobalBase(num, _12):
    if _12 == 1:
        global b1
        b1 = num
    elif _12 == 2:
        global b2
        b2 = num
    return
#Converting Bases
def convertBase(num, label_obj, labelErr_obj):
    global b1
    global b2
    if validBase(num, b1, label_obj, labelErr_obj):
        if b1 == b2:
            label_obj.widg.config(text=num)
            return
        #Do the convert base thingy
        #https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base
        op = 0
        if b1 == 2:
            if b2 == 8:
                op = str(oct(int(num, 2)))[2:]
            elif b2 == 10:
                op = int(num, 2)
                op = str(op)
            elif b2 == 16:
                op = hex(int(num, 2))
                op = str(op)[2:].upper()
        elif b1 == 8:
            if b2 == 2:
                op = str(bin(int(num, 8)))[2:]
            elif b2 == 10:
                op = str(int(num, 8))
            elif b2 == 16:
                op = str(hex(int(num, 8)))[2:].upper()
        elif b1 == 10:
            if b2 == 2:
                op = str(bin(int(num)))[2:]
            elif b2 == 8:
                op = str(oct(int(num)))[2:]
            elif b2 == 16:
                op = str(hex(int(num)))[2:].upper()
        elif b1 == 16:
            if b2 == 2:
                op = str(bin(int(num, 16)))[2:]
            elif b2 == 8:
                op = str(oct(int(num, 16)))[2:]
            elif b2 == 10:
                op = str(int(num, 16))
        label_obj.widg.config(text=op)
    return
#Checking if number input lies within opted base
def validBase(num, op, labelOp_obj, labelErr_obj):
    labelOp_obj.widg.config(text='')
    chars = '+-0123456789ABCDEF'
    chars = chars[0:op+2]
    if num == '':
        labelErr_obj.widg.config(text= 'Invalid Input!')
        return False
    
    for i in range(len(num)):
        if num[i] == '.':
            labelErr_obj.widg.config(text= 'Integers only!')
            return False
        if (num[i] == '-' and i != 0) or (num[i] == '+' and i != 0):
            labelErr_obj.widg.config(text= 'Invalid Input!')
            return False
        if num[i].upper() not in chars:
            labelErr_obj.widg.config(text= 'Invalid Input!')
            return False
    labelErr_obj.widg.config(text='Base Converted...')
    return True

#Quadratic equation calculator
def quadCalc(frame):
    hideFrame(frame)

    #Definging param DICTIONARIES for WIDGETS
    quadCalc_l_dic = {
        'master':quadCalc_frame,
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
        'w':5,
        'wraplength':None
    }
    quadCalc_b_dic = {
        'master':quadCalc_frame,
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
    quadCalc_e_dic = {
        'master':quadCalc_frame,
        'bd':None,
        'height':None,
        'w':5,
        'bg':None,
        'fg':None,
        'font':None,
        'insertofftime':None,
        'insertontime':None,
        'highlbg':None,
        'highlcolor':None,
        'cursor':None,
        'padx':None,
        'pady':None,
        'highthick':None,
        'charwidth':None,
        'relief':None,
        'yscrollcommand':None,
        'xscrollcommand':None,
        
    }
    quadCalc_g_dic = {
        'column':0,
        'row':0,
        'cspan':1,
        'rspan':1,
        'padx':2,
        'pady':2,
        'ipadx':0,
        'ipady':0
    }

    #Row 1
    #x^2 inp
    e_x2 = gfunc.GenFunc('entry', quadCalc_e_dic, StringVar(), quadCalc_g_dic)
    quadCalc_g_dic['column']+= 1
    l_x2 = gfunc.GenFunc('label', quadCalc_l_dic, 'x²  +', quadCalc_g_dic)
    quadCalc_g_dic['column']+= 1
    #x inp
    e_x = gfunc.GenFunc('entry', quadCalc_e_dic, StringVar(), quadCalc_g_dic)
    quadCalc_g_dic['column']+= 1
    l_x = gfunc.GenFunc('label', quadCalc_l_dic, 'x  +', quadCalc_g_dic)
    quadCalc_g_dic['column']+= 1
    #const inp
    e_const = gfunc.GenFunc('entry', quadCalc_e_dic, StringVar(), quadCalc_g_dic)
    quadCalc_g_dic['column']+= 1
    l_exp = gfunc.GenFunc('label', quadCalc_l_dic, ' = 0', quadCalc_g_dic)
    quadCalc_g_dic['column']+= 1
    
    #Row 2
    quadCalc_g_dic['row']+= 1
    quadCalc_g_dic['column'] = 1
    quadCalc_l_dic['w'] = 30
    quadCalc_l_dic['justify'] = LEFT
    quadCalc_g_dic['cspan'] = 6
    #configure wraplength
    l_op = gfunc.GenFunc('label', quadCalc_l_dic, '', quadCalc_g_dic)

    #Row 3
    quadCalc_g_dic['row']+= 1
    quadCalc_g_dic['column'] = 0
    quadCalc_g_dic['cspan'] = 3
    b_back = gfunc.GenFunc('button', quadCalc_b_dic, 'Back', quadCalc_g_dic)
    b_back.widg.config(command= lambda: destroyQuadLab(l_op))
    quadCalc_g_dic['column']+= 3
    b_go = gfunc.GenFunc('button', quadCalc_b_dic, 'Compute', quadCalc_g_dic)
    b_go.widg.config(command= lambda: computeQuadRoots(l_op, e_x2.widg.get(), e_x.widg.get(), e_const.widg.get()))

    quadCalc_frame.pack()
    return
    
#Destroying label
def destroyQuadLab(l):
    print('Quad Destroy reached')
    l.widg.grid_forget()
    l.widg.destroy()
    print('label destroyed')
    calcMenu(quadCalc_frame)
    return
#Computing roots for given coefficients of x^2, x and 1
def computeQuadRoots(label_obj, a, b, c):
    #Checking if only floating point / integer values are inputted
    try: 
        a = float(a)
        b = float(b)
        c = float(c)
    except:
        label_obj.widg.config(text='Floating values only!')
        return
    
    #Preventing div by 0 err to be thrown
    if a == 0:
        label_obj.widg.config(text='Coefficient of x^2 cannot be 0!')
        return

    #Discriminant
    d = (b**2) - (4*a*c)

    #Roots
    r1 = str((-b-cmath.sqrt(d))/(2*a))[1:-1]
    r2 = str((-b+cmath.sqrt(d))/(2*a))[1:-1]

    #Cleaning up raw string roots
    if r1.endswith('0j'):
        r1 = r1[0:-3]
    if r2.endswith('0j'):
        r2 = r2[0:-3]
    label_obj.widg.config(text=f'Root 1: {r1}\nRoot 2: {r2}')
    return

#Special number programs
def specNum(frame):
    hideFrame(frame)

    #Definging param DICTIONARIES for WIDGETS
    spn_l_dic = {
        'master':specNum_frame,
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
        'w':15,
        'wraplength':None
    }
    spn_b_dic = {
        'master':specNum_frame,
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
    spn_e_dic = {
        'master':specNum_frame,
        'bd':None,
        'height':None,
        'w':20,
        'bg':None,
        'fg':None,
        'font':None,
        'insertofftime':None,
        'insertontime':None,
        'highlbg':None,
        'highlcolor':None,
        'cursor':None,
        'padx':None,
        'pady':None,
        'highthick':None,
        'charwidth':None,
        'relief':None,
        'yscrollcommand':None,
        'xscrollcommand':None,
        
    }
    spn_g_dic = {
        'column':0,
        'row':0,
        'cspan':1,
        'rspan':1,
        'padx':10,
        'pady':10,
        'ipadx':0,
        'ipady':0
    }

    #Row 1
    l_choose = gfunc.GenFunc('label', spn_l_dic, 'Choose a Function:', spn_g_dic)
    specNum_list = ['Armstrong',
                    'Buzz',
                    'Automorphic',
                    'Capricon',
                    'Disarium',
                    'Duck',
                    'Evil',
                    'Odd or Even',
                    'Krishnamurthy',
                    'Magic',
                    'Neon',
                    'Niven',
                    'Palindrome',
                    'Perfect Square',
                    'Strong',
                    'Pronic',
                    'Spy',
                    'Tech',
                    'Prime',
                    'Factorial of a']
    specNum_list = [(str(i)+'. '+specNum_list[i]+ ' number') for i in range(len(specNum_list))]
    combo = ttk.Combobox(specNum_frame, values= specNum_list, state= 'readonly', width=20)
    combo.current(0)
    spn_g_dic['column']+=1
    combo.grid(row=spn_g_dic['row'], column=spn_g_dic['column'])
    combo.bind('<<ComboboxSelected>>', lambda event: spnExplain(combo.get(), l_exp, l_op))
    #Row 2
    spn_g_dic['row']+=1
    spn_g_dic['column'] = 0
    l_inp = gfunc.GenFunc('label', spn_l_dic, 'Enter a Number:', spn_g_dic)
    spn_g_dic['column']+=1
    e_inp = gfunc.GenFunc('entry', spn_e_dic, StringVar(), spn_g_dic)

    #Row 3
    spn_g_dic['row']+=1
    spn_g_dic['column'] = 0
    spn_g_dic['cspan'] = 2
    spn_l_dic['w'] = 40
    l_op = gfunc.GenFunc('label', spn_l_dic, '', spn_g_dic)
    
    #Row 4
    spn_g_dic['row']+=1
    spn_g_dic['rspan'] = 2
    spn_l_dic['w'] = 40
    spn_l_dic['wraplength'] = 300
    l_exp = gfunc.GenFunc('label', spn_l_dic, '', spn_g_dic)
    spnExplain(combo.get(), l_exp, l_op)
    spn_g_dic['rspan'] = 1
    spn_l_dic['w'] = 15
    spn_l_dic['wraplength'] = None

    #Row 5
    spn_g_dic['row']+=2
    spn_g_dic['cspan'] = 1
    spn_g_dic['cspan'] = 1
    b_back = gfunc.GenFunc('button', spn_b_dic, 'Back', spn_g_dic)
    b_back.widg.config(command= lambda: destroySPNLab(l_exp.widg, specNum_frame))
    spn_g_dic['column']+=1
    b_go = gfunc.GenFunc('button', spn_b_dic, 'Go', spn_g_dic)
    b_go.widg.config(command= lambda: evalSpecNum(combo.get(), e_inp.widg.get(), l_op))
    
    specNum_frame.pack()
    return
    
#Function to explain the special numbers 
def spnExplain(choice, label_obj, op_obj):
    #set title accordingly 
    #root.title(('Special Number -', choice.split(' ')[1]))
    op_obj.widg.config(text='')
    if choice.split(' ')[2] == 'Square':
        choice = 'Square'
    else:
        choice = choice.split(' ')[1]
    label_obj.widg.config(text=spn.specnum_explain[choice])
    return
def evalSpecNum(choice, num, label_obj):
    if len(num) == 0 or  not num.isnumeric():
        label_obj.widg.config(text='Invalid Entry!')
        return
    if choice.split(' ')[2] == 'Square':
        choice = 'Square'
    else:
        choice = choice.split(' ')[1]
    num = int(num)

    message = spn.evalSpecNum(choice=choice, num=num)

    label_obj.widg.config(text=message)
    return

#Function for verifying Sign In:
def SignInVer(label_obj, user, password):
    print(f'{user=}')
    print(f'{password=}')

    foundu,foundp = False,False
    print(foundp, foundu)

    mycursorU = mydb.cursor( )
    mycursorU.execute("Select Username from accounts")
    myresultU = mycursorU.fetchall( )

    mycursorP = mydb.cursor( )
    mycursorP.execute("Select Passcode from accounts")
    myresultP = mycursorP.fetchall( )

    for u in myresultU:
        print(u)
        if(user==u[0]):
            global current_user
            current_user = u[0]
            foundu = True
            break

    for p in myresultP:
        print(p)
        if(password==p[0]):
            global current_pass
            current_pass = p[0]
            foundp = True
            break
    

    if(foundu==True) and (foundp==True):  
        global is_guest
        is_guest = False
        print('Sign In success')
        homescreen(frame=signIn_frame)
        

    return

#Function for verifying Sign Up:
def signUpVer(label_obj, user, password, password_conf):
    validity = False
    a = 1

    sqlform = "INSERT INTO accounts values(%s,%s)"
    mycursor = mydb.cursor( )

    if(password==password_conf):
        # Everything below should come after Human verification
        acc = [(user,password)]
        try:
            mycursor.executemany(sqlform, acc)
            mydb.commit( )
            print("Congratulations!!! You've made an account")
            initSignInUp(signUp_frame)
            return
        except:
            print("ERROR: Username Already Exists!")
            label_obj.widg.config(text='ERROR: Username Already Exists!')
            return


#Function for verifying Delete Acc:
def delPofileVer():
    global current_user
    global current_pass
    mycursor = mydb.cursor( )
    sql = f"DELETE FROM accounts WHERE Username='{current_user}'"
    mycursor.execute(sql)
    mydb.commit( )
    print("Your account was deleted")
    initSignInUp(frame=delProf_frame)

    return

#Function for verifying Change Username:
def changeUserVer(label_obj, user, new_user, password):
    global current_user
    global current_pass
    mycursor = mydb.cursor( )

    if ((password == current_pass) and (user==current_user)):
        sql = f"UPDATE accounts SET Username='{new_user}' WHERE Passcode='{password}'"
        mycursor.execute(sql)
        mydb.commit( )
        print("Your username was updated")

    return

def changePassVer(label_obj, user, password, new_password, new_passwordConfirm):
    global current_user
    global current_pass

    if ((user==current_user)and(password==current_pass)):
        if(new_password==new_passwordConfirm):
            mycursor = mydb.cursor( )
            sql = f"UPDATE accounts SET Passcode='{new_password}' WHERE Username='{user}'"
            mycursor.execute(sql)
            mydb.commit( )
            print("Your password was updated")
            current_pass = new_password
            label_obj.widg.config(text="Your password was updated")

    return
#Function for verifying Change Password:
initSignInUp(None)
#Showing WINDOW
root.mainloop()