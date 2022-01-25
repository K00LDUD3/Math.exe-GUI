from tkinter import *
#Importing required libs and mods
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

#Main screen FRAME
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
    homescreen_g_dic['row'] = 1
    homescreen_g_dic['column'] = 0
    b_signOut = gfunc.GenFunc('button', homescreen_b_dic, 'Sign Out', homescreen_g_dic)
    b_signOut.widg.config(command= lambda: initSignInUp(homescreen_frame))
    homescreen_g_dic['column'] = 1
    b_calc = gfunc.GenFunc('button', homescreen_b_dic, 'Calculators', homescreen_g_dic)
    b_calc.widg.config(command= lambda: calcMenu(homescreen_frame))
    #Row 3
    homescreen_g_dic['row'] = 2
    homescreen_g_dic['column'] = 0
    global is_guest
    if not(is_guest):
        b_editProf = gfunc.GenFunc('button', homescreen_b_dic, 'Edit Profile', homescreen_g_dic)

    homescreen_frame.pack()
    return

#Guessing game menu
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
    print(f'{number=}')
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
    cm_g_dic['row'] +=1
    b_baseN = gfunc.GenFunc('button', cm_b_dic, 'Base-N Calculator', cm_g_dic)
    b_baseN.widg.config(command= lambda: baseCalc(calcMenu_frame))
    cm_g_dic['row'] +=1
    b_quad = gfunc.GenFunc('button', cm_b_dic, 'Quadratic Equation Calculator', cm_g_dic)
    cm_g_dic['row'] +=1
    b_vect = gfunc.GenFunc('button', cm_b_dic, 'Vector Calculator', cm_g_dic)
    cm_g_dic['row'] +=1
    b_back = gfunc.GenFunc('button', cm_b_dic, 'Back', cm_g_dic)
    b_back.widg.config(command= lambda: homescreen(calcMenu_frame))
    cm_g_dic['row'] +=1

    calcMenu_frame.pack()
    return

def baseCalc(frame):
    hideFrame(frame)

    baseCalc_e_dic = {
        'master':baseCalc_frame,
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
    e_inp = gfunc.GenFunc('entry', baseCalc_e_dic, StringVar(), baseCalc_g_dic)

    #Row 2
    baseCalc_g_dic['row']+=1
    #baseCalc_g_dic['column'] =1
    x = IntVar()
    r_ip2 = Radiobutton(master=baseCalc_frame, value=2, text='Base 2', variable=x)
    r_ip2.grid(row=baseCalc_g_dic['row'], column=baseCalc_g_dic['column'])
    baseCalc_g_dic['column']+=1
    r_ip3 = Radiobutton(master=baseCalc_frame, value=8, text='Base 8', variable=X)
    r_ip3.grid(row=baseCalc_g_dic['row'], column=baseCalc_g_dic['column'])
    #FIX RADIO BUTTONS
    
    #Row 3
    baseCalc_g_dic['row']+=1
    #baseCalc_g_dic['column'] =1
    


    #Row 4
    baseCalc_g_dic['row']+=1
    baseCalc_g_dic['column'] =0
    b_back = gfunc.GenFunc('button', baseCalc_b_dic, 'Back', baseCalc_g_dic)
    b_back.widg.config(command= lambda: calcMenu(baseCalc_frame))
    baseCalc_g_dic['column']+=1
    l_op = gfunc.GenFunc('label', baseCalc_l_dic, '<OUTPUT>', baseCalc_g_dic)

    baseCalc_frame.pack()
    return

    

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
    b_back.widg.config(command= lambda: homescreen(specNum_frame))
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
    print(f'{choice=}')
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
initSignInUp(None)
#Showing WINDOW
root.mainloop()

