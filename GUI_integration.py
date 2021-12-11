'''
LINKS
tkinter basic stuff ===== https://www.javatpoint.com/python-tkinter

'''
#IMPORTING required MODULES
from tkinter import *
from tkinter import ttk
import Special_Numbers as spn
import tkinter.font as font
import random
import math

#WIDGET var PARAMS
button_width = 20
button_padx = 10
button_pady = 10
c_button_width = 5
c_button_padx = 10


#creating WINDOW
root = Tk()
root.title('Math.exe')
root.geometry("365x150")

'''
#button Param Variables
button_width_c = 5
button_height_c = 5
button_padx_c = 0
button_pady_c = 0
button_borderwidth_c = 1
button_font_c = font.Font(size=15)
'''
#Guessing game var NUMBER OF TRIES
count_tries = 0

#scientific calculator vars
button_list = []
c_button_font = font.Font(size=15)

#creating neccessary FRAMES
initSignInUp_frame = LabelFrame(root)
signIn_frame = LabelFrame(root)
signUp_frame = LabelFrame(root)
editProfile_frame = LabelFrame(root)
homescreen_frame = LabelFrame(root)
deleteProfile_frame = LabelFrame(root) 
changeUser_frame = LabelFrame(root)
changPass_frame = LabelFrame(root)
specNumPrg_frame = LabelFrame(root)
initGuessgame_frame = LabelFrame(root)
guessgame_frame = LabelFrame(root)
sciCalc_frame = LabelFrame(root)

#creating the dropdown for SPECIAL NUMBER PROGRAMS
combo = ttk.Combobox()

#function for HIDING given FRAME
def hideFrame(frame):
    try:
        frame.pack_forget()
    except:
        None
    return

#generic function to CREATE BUTTON
def createButton(Text, Width, xcor, ycor, px,py, frame):
    button = Button(frame, width=Width, text=Text)
    button.grid(row=xcor, column=ycor)
    button.grid(row=xcor, column=ycor, padx=px, pady=py)
    return button

#generic function to CREATE LABELS
def createLabel(Text, Width, xcor, ycor, px,py, frame):
    label = Label(frame, width=Width, text=Text)
    label.grid(row=xcor, column=ycor)
    label.grid(row=xcor, column=ycor, padx=px, pady=py)
    return label

#generic function to CREATE TEXTBOXES
def createEntry(Width, xcor, ycor, px,py, frame):
    entry = Entry(frame, width=Width)
    entry.grid(row=xcor, column=ycor)
    entry.grid(row=xcor, column=ycor, padx=px, pady=py)
    return entry




#SIGN IN OR SIGN UP
def initSignInUp(frame):
    #hiding active frame
    hideFrame(frame)

    #configring WINDOW
    root.geometry('250x150')
    root.title('Sign In/Up')

    #creating widgets
    b_sign_in =  createButton('Sign In', button_width, 0, 0, button_padx, button_pady, initSignInUp_frame)
    b_sign_up = createButton('Sign Up', button_width, 1, 0, button_padx, button_pady, initSignInUp_frame)
    b_guest = createButton('Continue As Guest', button_width, 2, 0, button_padx, button_pady, initSignInUp_frame)
    
    b_guest.config(command=lambda: homescreen(initSignInUp_frame))
    b_sign_in.config(command=lambda: signIn(initSignInUp_frame))
    b_sign_up.config(command=lambda: signUp(initSignInUp_frame))

    initSignInUp_frame.pack()
    return

def signIn(frame):
    #hiding active frame
    hideFrame(frame)

    #configuring WINDOW
    root.geometry('350x150')
    root.title('Sign In')

    #creating WIDGETS
    l_user = createLabel('Enter Your Username:', button_width, 0, 0, button_padx, button_pady, signIn_frame)
    l_pass = createLabel('Enter Your Password:', button_width, 1, 0, button_padx, button_pady, signIn_frame)
    
    e_user = createEntry(button_width, 0, 1, button_padx, button_pady, signIn_frame)
    e_user.bind('<Return>', lambda event: signInVer(event, e_user.get(), e_pass.get()))
    e_pass = createEntry(button_width, 1, 1, button_padx, button_pady, signIn_frame)
    e_pass.bind('<Return>', lambda event: signInVer(event, e_user.get(), e_pass.get()))

    b_back = createButton('Back', button_width, 2, 0, button_padx, button_pady, signIn_frame)
    b_go = createButton('Sign In', button_width, 2, 1, button_padx, button_pady, signIn_frame)


    b_back.config(command=lambda: initSignInUp(signIn_frame))
    b_go.config(command=lambda: signInVer(None, e_user.get(), e_pass.get()))
    
    signIn_frame.pack()
    return

def signUp(frame):
    #hiding active frame
    hideFrame(frame)

    #configuring WINDOW
    root.geometry('350x200')
    root.title('Sign Up')

    #creating WIDGETS
    '''
    For password and user,
    use a live action listener to check the database
    if a user/password is taken/weak
    '''




    l_user = createLabel('Enter Your Username:', button_width, 0, 0, button_padx, button_pady, signUp_frame)
    l_pass = createLabel('Enter Your Password:', button_width, 1, 0, button_padx, button_pady, signUp_frame)
    l_passConf = createLabel('Confirm Your Password:', button_width, 2, 0, button_padx, button_pady, signUp_frame)

    e_user = createEntry(button_width, 0, 1, button_padx, button_pady, signUp_frame)
    e_user.bind('<Return>', lambda event: signUpVer(event, e_user.get(), e_pass.get(), e_passconf.get()))

    e_pass = createEntry(button_width, 1, 1, button_padx, button_pady, signUp_frame)
    e_pass.bind('<Return>', lambda event: signUpVer(event, e_user.get(), e_pass.get(), e_passconf.get()))

    e_passconf = createEntry(button_width, 2, 1, button_padx, button_pady, signUp_frame)
    e_passconf.bind('<Return>', lambda event: signUpVer(event, e_user.get(), e_pass.get(), e_passconf.get()))

    b_back = createButton('Back', button_width, 3, 0, button_padx, button_pady, signUp_frame)
    b_go = createButton('Sign In', button_width, 3, 1, button_padx, button_pady, signUp_frame)


    b_back.config(command=lambda: initSignInUp(signUp_frame))
    b_go.config(command=lambda: signUpVer(None, e_user.get(), e_pass.get(), e_passconf.get()))
    
    signUp_frame.pack()
    return
    
#HOMESCREEN frame
def homescreen(frame):
    #hiding active frame
    hideFrame(frame)
    root.geometry('365x150')
    root.title('Homescreen')
    
    #neccessary BUTTONS
    b_editProfile = createButton('Edit Profile', button_width, 0,0, button_padx, button_pady, homescreen_frame)
    b_specNumPrg = createButton('Special Number Programs', button_width,0,1, button_padx, button_pady, homescreen_frame)
    b_calc = createButton('Scienctific Calculator', button_width,1,0, button_padx, button_pady, homescreen_frame)
    b_guessGame = createButton('Guessing Game',button_width,1,1, button_padx, button_pady, homescreen_frame)
    b_signOut = createButton('Sign Out',button_width,2,0, button_padx, button_pady, homescreen_frame)

    b_editProfile.config(command=lambda: editProfile(homescreen_frame))
    b_specNumPrg.config(command=lambda: specNumPrg(homescreen_frame))
    b_calc.config(command=lambda: sciCalc(homescreen_frame))
    b_guessGame.config(command=lambda: initGuessingGame(homescreen_frame))
    b_signOut.config(command=lambda: initSignInUp(homescreen_frame))


    homescreen_frame.pack()
    return

def initCalc():
    return

#EDIT PROFILE frame
def editProfile(frame):
    #hiding  active frame
    hideFrame(frame)

    #configuring window
    root.title('Edit Profile')
    size = str(editProfile_frame.winfo_width())+'x'+str(editProfile_frame.winfo_height())
    print(size)
    root.geometry('200x200')

    #neccessary edit profile BUTTONS
    b_changeUser = createButton('Change Username', button_width, 0, 0, button_padx, button_pady, editProfile_frame)
    b_changePass = createButton('Change Password', button_width, 1, 0, button_padx, button_pady, editProfile_frame)    
    b_delProfile = createButton('Delete Account', button_width, 2, 0, button_padx, button_pady, editProfile_frame)    
    b_Homescreen = createButton('Back', button_width, 3, 0, button_padx, button_pady, editProfile_frame)
    
    #setting COMMANDS/ACTION LISTENERS for above buttons
    b_delProfile.config(command=deleteProfile)
    b_changeUser.config(command=changeUser)
    b_changePass.config(command=changePass)
    b_Homescreen.config(command=lambda: homescreen(editProfile_frame))

    #putting edit profile frame on screen
    editProfile_frame.pack(padx=10, pady=10)
    return

def deleteProfile():
    #hiding active frame
    hideFrame(editProfile_frame)
    
    #configuring window
    root.title('Edit Profile - Delete Account')
    root.geometry('400x200')

    #neccessary delete profile WIDGETS
    l_enterUser = createLabel('Enter Username: ', button_width, 0, 0, button_padx, button_pady, deleteProfile_frame)
    l_enterPass = createLabel('Enter your Password: ', button_width, 1, 0, button_padx, button_pady, deleteProfile_frame)
    l_enterPassConf =createLabel('Confirm Password: ', button_width, 2, 0, button_padx, button_pady, deleteProfile_frame)

    e_username = createEntry(20, 0, 1, button_padx, button_pady, deleteProfile_frame)
    e_username.bind('<Return>', lambda event: delAccVer(event, e_username.get(), e_pass.get(), e_passConf.get()))
    e_pass = createEntry(20, 1, 1, button_padx, button_pady, deleteProfile_frame)
    e_pass.bind('<Return>', lambda event: delAccVer(event, e_username.get(), e_pass.get(), e_passConf.get()))
    e_passConf = createEntry(20, 2, 1, button_padx, button_pady, deleteProfile_frame)
    e_passConf.bind('<Return>', lambda event: delAccVer(event, e_username.get(), e_pass.get(), e_passConf.get()))

    b_confirm = createButton('Delete Account', button_width, 3, 1, button_padx, button_pady, deleteProfile_frame)
    b_confirm.config(command= lambda: delAccVer(None, e_username.get(), e_pass.get(), e_passConf.get()))
    b_cancel = createButton('Cancel',5, 3, 0, button_padx, button_pady, deleteProfile_frame)
    b_cancel.config(command=lambda: editProfile(deleteProfile_frame))


    #putting del profile frame on screen
    deleteProfile_frame.pack(padx=10, pady=10)
    return

def changePass():
    #hiding active frame
    hideFrame(editProfile_frame)

    #configuring window
    root.title('Edit Profile - Change Password')
    root.geometry('400x300')

    #neccessary delete profile WIDGETS
    l_enterUser = createLabel('Enter Username: ', button_width, 0, 0, button_padx, button_pady, changPass_frame)
    l_enterPass = createLabel('Enter your Password: ', button_width, 1, 0, button_padx, button_pady, changPass_frame)
    l_enterPassConf =createLabel('Confirm Password: ', button_width, 2, 0, button_padx, button_pady, changPass_frame)
    l_enterPassUser = createLabel('Enter New Password: ', button_width, 3, 0, button_padx, button_pady, changPass_frame)
    l_enterNewPassConf = createLabel('Confirm New Password: ', button_width, 4, 0, button_padx, button_pady, changPass_frame)

    e_username = createEntry(20, 0, 1, button_padx, button_pady, changPass_frame)
    e_username.bind('<Return>', lambda event: changePassVer(event, e_username.get(), e_pass.get(), e_passConf.get(), e_newPass.get(), e_newPassConf.get()))
    e_pass = createEntry(20, 1, 1, button_padx, button_pady, changPass_frame)
    e_pass.bind('<Return>', lambda event: changePassVer(event, e_username.get(), e_pass.get(), e_passConf.get(), e_newPass.get(), e_newPassConf.get()))
    e_passConf = createEntry(20, 2, 1, button_padx, button_pady, changPass_frame)
    e_passConf.bind('<Return>', lambda event: changePassVer(event, e_username.get(), e_pass.get(), e_passConf.get(), e_newPass.get(), e_newPassConf.get()))
    e_newPass = createEntry(20, 3, 1, button_padx, button_pady, changPass_frame)
    e_newPass.bind('<Return>', lambda event: changePassVer(event, e_username.get(), e_pass.get(), e_passConf.get(), e_newPass.get(), e_newPassConf.get()))
    e_newPassConf = createEntry(button_width, 4, 1, button_padx, button_pady, changPass_frame)
    e_newPassConf.bind('<Return>', lambda event: changePassVer(event, e_username.get(), e_pass.get(), e_passConf.get(), e_newPass.get(), e_newPassConf.get()))

    b_confirm = createButton('Change Password', button_width, 5, 1, button_padx, button_pady, changPass_frame)
    b_confirm.config(command=lambda: changePassVer(None, e_username.get(), e_pass.get(), e_passConf.get(), e_newPass.get(), e_newPassConf.get()))
    b_cancel = createButton('Cancel',5, 5, 0, button_padx, button_pady, changPass_frame)
    b_cancel.config(command=lambda: editProfile(changPass_frame))

    #putting del profile frame on screen
    changPass_frame.pack(padx=10, pady=10)
    return


def changeUser():
    #hiding active frame
    hideFrame(editProfile_frame)

    #configuring window
    root.title('Edit Profile - Change Username')
    root.geometry('400x300')

    #neccessary delete profile WIDGETS
    l_enterUser = createLabel('Enter Username: ', button_width, 0, 0, button_padx, button_pady, changeUser_frame)
    l_enterPass = createLabel('Enter your Password: ', button_width, 1, 0, button_padx, button_pady, changeUser_frame)
    l_enterNewUser = createLabel('Enter New Username: ', button_width, 3, 0, button_padx, button_pady, changeUser_frame)

    e_username = createEntry(20, 0, 1, button_padx, button_pady, changeUser_frame)
    e_username.bind('<Return>', lambda event: changeUserVer(event, e_username.get(), e_newUser.get(), e_pass.get()))
    e_pass = createEntry(20, 1, 1, button_padx, button_pady, changeUser_frame)
    e_pass.bind('<Return>', lambda event: changeUserVer(event, e_username.get(), e_newUser.get(), e_pass.get()))
    e_newUser = createEntry(20, 3, 1, button_padx, button_pady, changeUser_frame)
    e_newUser.bind('<Return>', lambda event: changeUserVer(event, e_username.get(), e_newUser.get(), e_pass.get()))

    b_confirm = createButton('Change Username', button_width, 4, 1, button_padx, button_pady, changeUser_frame)
    b_confirm.config(command=lambda: changeUserVer(None, e_username.get(), e_newUser.get(), e_pass.get()))
    b_cancel = createButton('Cancel',5, 4, 0, button_padx, button_pady, changeUser_frame)
    b_cancel.config(command=lambda: editProfile(changeUser_frame))
    
    #putting change user frame on screen
    changeUser_frame.pack(padx=10, pady=10)
    return

"""
Finish binding <Return> to rest of the ENTRIES
Left off hereerererere
"""
def specNumPrg(frame):
    # hiding active frame
    hideFrame(frame)

    #configuring window
    root.geometry('540x180')

    # creating spec num list
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
    
    #necessary WIDGETS
    #Row 1
    combo = ttk.Combobox(specNumPrg_frame,values=specNum_list,state='readonly', width=25)
    combo.current(0)
    combo.bind('<<ComboboxSelected>>', lambda event: spnExplain(combo.get(), l_spnExplain))
    combo.grid(row=0,column=1)
    l_combo = createLabel('Choose function: ', button_width, 0, 0, button_padx, button_pady, specNumPrg_frame)
    #b_explain = createButton('Explanation', button_width, 0, 2, button_padx, button_pady, specNumPrg_frame)
    #b_explain.config(command=lambda: spnExplain(combo.get(),l_spnExplain))


    #Row 2
    e_num = createEntry(button_width+5, 1, 1, button_padx, button_padx, specNumPrg_frame)
    l_num = createLabel('Enter a number:', button_width, 1, 0, button_padx, button_pady, specNumPrg_frame)
    l_spnExplain = Label(specNumPrg_frame, width=button_width, text='', wraplength=150)
    l_spnExplain.grid(row=1, column=2, rowspan=2)


    #Row 3
    l_output = createLabel('Output:', button_width, 2, 0, button_padx, button_pady, specNumPrg_frame)
    l_opMessage = createLabel('', button_width, 2, 1, button_padx, button_pady, specNumPrg_frame)

    #Row 4
    b_back = createButton('Back',button_width, 3, 0, button_padx, button_pady, specNumPrg_frame)
    b_back.config(command= lambda: homescreen(specNumPrg_frame))
    b_go = createButton('Go', button_width, 3, 1, button_padx, button_pady, specNumPrg_frame)
    b_go.config(command=lambda: initSPN(combo.get(), e_num.get(), l_opMessage)) # Prg this later
    
    #showing the widgets on screen
    specNumPrg_frame.pack()
    return

def spnExplain(choice, label):
    label.grid_forget()
    if choice.split(' ')[2] == 'Square':
        choice = 'Square'
    else:
        choice = choice.split(' ')[1]
    print(f'{choice=}')
    label.config(text=spn.specnum_explain[choice])
    label.grid(row=1, column=2, rowspan=2)
    return

def initSPN(choice, number, label): # intialize special number programs
    if len(number) == 0 or  not number.isnumeric():
        label.config(text='Invalid Entry!')
        return
    if choice.split(' ')[2] == 'Square':
        choice = 'Square'
    else:
        choice = choice.split(' ')[1]
    number = int(number)

    message = spn.evalSpecNum(choice=choice, num=number)
    label.config(text=message)

    return

#add a display label and reference it in every cong(command)
def sciCalc(frame):
    #hiding active frame
    hideFrame(frame)

    #configuring window
    root.geometry("600x300")
    root.title('Calculator')

    #creating WIDGETS
    label = Label(sciCalc_frame, text='', width=55, height=2)
    label.grid(row=0, column=0, columnspan=4)
    #assigning values of buttons (1-9, 0)
    for i in range(0,9):
        button_list.append(Button(sciCalc_frame, width=c_button_width, text = (i+1), font=c_button_font))
        button_list[i].grid(row=i//3+1, column=i%3, padx = c_button_padx, pady = button_pady)

    button_list.append(Button(sciCalc_frame, width=c_button_width, text = 0, font=c_button_font))
    button_list[9].grid(row=4, column=1, padx = button_padx, pady = button_pady)


    #creating NUMBER BUTTONS
    button_list[9].config(command = lambda: AddNumOperator('0', label))
    button_list[0].config(command = lambda: AddNumOperator('1', label))
    button_list[1].config(command = lambda: AddNumOperator('2', label))
    button_list[2].config(command = lambda: AddNumOperator('3', label))
    button_list[3].config(command = lambda: AddNumOperator('4', label))
    button_list[4].config(command = lambda: AddNumOperator('5', label))
    button_list[5].config(command = lambda: AddNumOperator('6', label))
    button_list[6].config(command = lambda: AddNumOperator('7', label))
    button_list[7].config(command = lambda: AddNumOperator('8', label))
    button_list[8].config(command = lambda: AddNumOperator('9', label))

    #creating OPERATOR BUTTONS
    op_font = c_button_font
    op_add = Button(sciCalc_frame, width=c_button_width, text='+', command=lambda: AddNumOperator('+', label), font=op_font)
    op_subtract = Button(sciCalc_frame, width=c_button_width, text='-', command=lambda: AddNumOperator('-', label), font=op_font)
    op_multiply = Button(sciCalc_frame, width=c_button_width, text='*', command=lambda: AddNumOperator('*', label), font=op_font)
    op_divide = Button(sciCalc_frame, width=c_button_width, text='/', command=lambda: AddNumOperator('/', label), font=op_font)
    op_modulus = Button(sciCalc_frame, width=c_button_width, text='mod', command=lambda: AddNumOperator('%', label), font=op_font)
    op_power = Button(sciCalc_frame, width=c_button_width, text='^', command=lambda: AddNumOperator('^', label), font=op_font)
    op_add.grid(row=1, column=3, padx = button_padx, pady = button_pady)
    op_subtract.grid(row=2, column=3, padx = c_button_padx, pady = button_pady)
    op_multiply.grid(row=3, column=3, padx = c_button_padx, pady = button_pady)
    op_divide.grid(row=4, column=3, padx = c_button_padx, pady = button_pady)
    op_modulus.grid(row=4, column=0, padx=c_button_padx, pady=button_pady)
    op_power.grid(row=3, column=4, padx=c_button_padx, pady=button_pady)

    #'=' BUTTON
    __equal = Button(sciCalc_frame, width=c_button_width, text='=', command=lambda: EvalExp(label), font=c_button_font)
    __equal.grid(row=4, column=4, padx = c_button_padx, pady = button_pady)

    #backspace BUTTON
    __backspace = Button(sciCalc_frame, width=c_button_width, text='del', command=lambda: Backspace(label), font=c_button_font)
    __backspace.grid(row=2, column=4, padx = c_button_padx, pady = button_pady)
    
    #Clear BUTTON
    AC = Button(sciCalc_frame, width=c_button_width, text = 'clear', command =lambda: clear(label), font=c_button_font)
    AC.grid(row=1, column=4)
    
    #decimal point BUTTON
    point = Button(sciCalc_frame, width=c_button_width, text = '.', command=lambda: AddNumOperator('.', label), font=c_button_font)
    point.grid(row=4, column=2, padx=button_padx, pady=button_pady)

    #back BUTTON
    back = Button(sciCalc_frame, width=c_button_width, text = 'Back', command =lambda: homescreen(sciCalc_frame))
    back.grid(row=5, column=0, padx=c_button_padx, pady=button_pady)

    sciCalc_frame.pack()
    return

#sci calc func EVALUATE THE EXPRESSION
def EvalExp(label):
    exp = label.cget('text')
    try:
        exp = exp.replace('^','**')
        formatVal = float("{:.3f}".format(float(eval(exp))))
        if int(formatVal) == formatVal:
            formatVal = int(formatVal)
        label.config(text=str(formatVal))
    except:
        label.config(text='ERROR')
    
#sci calc func BACKSPACE
def Backspace(label):
    exp = label.cget('text')
    exp = exp.strip()
    exp = exp[0:len(exp)-1]
    label.config(text=exp)

#sci calc func ADDING A NUMBER/OPERATOR TO OUTPUT DISPLAY
def AddNumOperator(OpNum, label):
    exp = label.cget('text')
    print(type(exp), exp)
    if 'ERROR' in(exp):
        exp = ''
    
    print(f'{exp=}')
    try:
        if (OpNum.isnumeric() or OpNum=='.') and (exp[-1].isnumeric() or exp[-1]=='.'):
            exp = exp+''+OpNum
        elif ~(OpNum.isnumeric()):
            exp = exp+' '+OpNum
        print('exp after concatinating: ',exp)
    except:
        exp = exp+''+OpNum
    label.config(text=exp)

#sci calc func CLEAR OUTPUT DISPLAY
def clear(label):
    label.config(text='')


def initGuessingGame(frame):
    #hiding active frame
    hideFrame(frame)
    
    #configuring window
    root.title('Guessing Game - Menu')

    #creating necessary widgets
    #Row 1
    l_rangeMin = createLabel('Enter minimum value:', button_width, 0, 0, button_padx, button_pady, initGuessgame_frame)
    e_rangeMin = createEntry(button_width, 0, 1, button_padx, button_pady, initGuessgame_frame)
    
    #Row 2
    l_rangeMax = createLabel('Enter maximum value:', button_width, 1, 0, button_padx, button_pady, initGuessgame_frame)
    e_rangeMax = createEntry(button_width, 1, 1, button_padx, button_pady, initGuessgame_frame)

    #Row 3
    b_back = createButton('Back', button_width, 2, 0, button_padx, button_pady, initGuessgame_frame)
    b_start = createButton('Start', button_width, 2, 1, button_padx, button_pady, initGuessgame_frame)
    b_back.config(command=lambda: homescreen(initGuessgame_frame))
    b_start.config(command=lambda: guessingGame(initGuessgame_frame, e_rangeMax.get()))

    #showing frame on screen
    initGuessgame_frame.pack()
    return

def guessingGame(frame, maxR):
    global count_tries
    count_tries=0
    '''if not(maxR.isnumeric() and minR.isnumeric()) or (minR >= maxR) or minR == '' or maxR == '':
        print('Invalid Input')
        return'''
    if not(maxR.isnumeric()):
        return print(f'ERROR: <{maxR=}>: not numeric')
    maxR = int(maxR)
    

    #hiding active frame
    hideFrame(frame)
    
    #configuring window
    root.title(f'Guessing Game: 0 to {maxR}')

    #setting rand number between 0 and maxR
    number = randGen(maxR)
    print(f'{number=}')

    #creating necessary widgets
    #Row1
    l_enterNum = createLabel('Enter a number in given range:', button_width+2, 0, 0, button_padx, button_pady, guessgame_frame)
    e_input = createEntry(button_width, 0, 1, button_padx, button_pady, guessgame_frame)

    #Row2
    l_resultMessage = createLabel('Result:', button_width, 1, 0, button_padx, button_pady, guessgame_frame)
    l_output = createLabel('', button_width, 1, 1, button_padx, button_pady, guessgame_frame)

    #Row3
    b_back = createButton('Back', button_width, 2, 0, button_padx, button_pady, guessgame_frame)
    b_guess = createButton('Guess', button_width, 2, 1, button_padx, button_pady, guessgame_frame)
    b_back.config(command=lambda: initGuessingGame(guessgame_frame))
    b_guess.config(command=lambda: validateChoice(int(e_input.get()), number, l_output, b_guess))

    #showing frame on screen
    guessgame_frame.pack()
    return


def validateChoice(num, valid_num, label, b_guess):
    #"TRYINGGGGGGG" to increment number of tries
    global count_tries
    print(f'GLOBAL <{count_tries = }>')
    count_tries+=1
    #evaluating the guess with the randomly generated number
    if num == valid_num:
        message = f'Correct! Number of tries:{count_tries}'
        #disabling button if number guessed is correct
        b_guess['state'] = 'disabled'
    elif num > valid_num:
        message =  'Try Guessing Lower!'
    elif num < valid_num:
        message =  'Try Guessing Higher!'
    label.config(text=message)
    return

def randGen(maxR):
    maxR = int(maxR)
    return random.randrange(maxR)


#editProfile func CHANGE USERNAME
def changeUserVer(event, old_user, new_user, password):
    #validate with Burgers DB and display message accordingly
    print(f'{event=}')

    return
#editProfile func CHANGE PASSWORD
def changePassVer(event, user, old_password, old_passwordConfirm, new_password, new_passwordConfirm):
    #validate with Burgers DB and display message accordingly
    print(f'{event=}')
    print(f'{user=}')
    print(f'{old_password=}')
    print(f'{old_passwordConfirm=}')
    print(f'{new_password=}')
    print(f'{new_passwordConfirm=}')

    return
#editProfile func DELETE PROFILE
def delAccVer(event, user, password, passwordConfirm):
    #validate with Burgers DB and display message accordingly
    print(f'{event=}')
    print(f'{user=}')
    print(f'{password=}')
    print(f'{passwordConfirm=}')

    return

#sign in or sign up func USERNAME AND PASSWORD verify
def signInVer(event, user, password):
    #validate with Burgers DB and continue accordingly
    print(f'{event=}')
    print(f'{user=}')
    print(f'{password=}')

    return
#sign in or sign up func USERNAME, PASSWORD, CONFIRM PASSWORD verify
def signUpVer(event, user, password, password_conf):
    #validate with Burgers DB and continue accordingly
    print(f'{event=}')
    return


initSignInUp(None)
root.mainloop()

