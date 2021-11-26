'''
LINKS
tkinter basic stuff ===== https://www.javatpoint.com/python-tkinter

'''
#importing required modules
from tkinter import *
from tkinter import ttk
import Special_Numbers as spn

#active frame
##act_frame = None

#button var params
button_width = 20
button_padx = 10
button_pady = 10

#creating window
root = Tk()
root.title('Math.exe')
root.geometry("365x150")

#creating neccessary frames
editProfile_frame = LabelFrame(root)
homescreen_frame = LabelFrame(root)
deleteProfile_frame = LabelFrame(root) 
changeUser_frame = LabelFrame(root)
changPass_frame = LabelFrame(root)
specNumPrg_frame = LabelFrame(root)

#function for hiding given frame
def hideFrame(frame):
    try:
        frame.pack_forget()
    except:
        None

#generic function to create button
def createButton(Text, Width, xcor, ycor, px,py, frame):
    button = Button(frame, width=Width, text=Text)
    button.grid(row=xcor, column=ycor)
    button.grid(row=xcor, column=ycor, padx=px, pady=py)
    return button

#generic function to create labels
def createLabel(Text, Width, xcor, ycor, px,py, frame):
    label = Label(frame, width=Width, text=Text)
    label.grid(row=xcor, column=ycor)
    label.grid(row=xcor, column=ycor, padx=px, pady=py)
    return label

#generic function to create labels
def createEntry(Width, xcor, ycor, px,py, frame):
    entry = Entry(frame, width=Width)
    entry.grid(row=xcor, column=ycor)
    entry.grid(row=xcor, column=ycor, padx=px, pady=py)
    return entry

combo = ttk.Combobox()

    

#homescreen frame
def homescreen(frame):
    #hiding active (if any) frame
    hideFrame(frame)
    root.geometry('365x150')
    root.title('Homescreen')
    
    #neccessary buttons
    b_editProfile = createButton('Edit Profile', button_width, 0,0, button_padx, button_pady, homescreen_frame)
    b_specNumPrg = createButton('Special Number Programs', button_width,0,1, button_padx, button_pady, homescreen_frame)
    b_calc = createButton('Scienctific Calculator', button_width,1,0, button_padx, button_pady, homescreen_frame)
    b_guessGame = createButton('Guessing Game',button_width,1,1, button_padx, button_pady, homescreen_frame)
    b_signOut = createButton('Sign Out',button_width,2,0, button_padx, button_pady, homescreen_frame)

    b_editProfile.config(command=lambda: editProfile(homescreen_frame))
    b_specNumPrg.config(command=lambda: specNumPrg(homescreen_frame))
    homescreen_frame.pack()
    



def editProfile(frame):
    #hiding the active frame
    hideFrame(frame)

    root.title('Edit Profile')
    ## CHANGE SIZE, GET PROPER SIZE
    size = str(editProfile_frame.winfo_width())+'x'+str(editProfile_frame.winfo_height())
    print(size)
    root.geometry('200x200')
    #neccessary edit profile buttons
    b_changeUser = createButton('Change Username', button_width, 0, 0, button_padx, button_pady, editProfile_frame)
    b_changePass = createButton('Change Password', button_width, 1, 0, button_padx, button_pady, editProfile_frame)    
    b_delProfile = createButton('Delete Account', button_width, 2, 0, button_padx, button_pady, editProfile_frame)    
    b_Homescreen = createButton('Back', button_width, 3, 0, button_padx, button_pady, editProfile_frame)
    
    #setting commands for above buttons
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
    
    root.title('Edit Profile - Delete Account')

    #setting proper size
    root.geometry('400x200')

    #neccessary delete profile buttons, labels, textboxes
    l_enterUser = createLabel('Enter Username: ', button_width, 0, 0, button_padx, button_pady, deleteProfile_frame)
    l_enterPass = createLabel('Enter your Password: ', button_width, 1, 0, button_padx, button_pady, deleteProfile_frame)
    l_enterPassConf =createLabel('Confirm Password: ', button_width, 2, 0, button_padx, button_pady, deleteProfile_frame)

    e_username = createEntry(20, 0, 1, button_padx, button_pady, deleteProfile_frame)
    e_pass = createEntry(20, 1, 1, button_padx, button_pady, deleteProfile_frame)
    e_passConf = createEntry(20, 2, 1, button_padx, button_pady, deleteProfile_frame)

    b_confirm = createButton('Delete Account', button_width, 3, 1, button_padx, button_pady, deleteProfile_frame)
    b_cancel = createButton('Cancel',5, 3, 0, button_padx, button_pady, deleteProfile_frame)
    b_cancel.config(command=lambda: editProfile(deleteProfile_frame))

    #putting del profile frame on screen
    deleteProfile_frame.pack(padx=10, pady=10)
    return

def changePass():
    #hiding active frame
    hideFrame(editProfile_frame)

    root.title('Edit Profile - Change Password')
    #setting proper size
    root.geometry('400x300')

    #neccessary delete profile buttons, labels, textboxes
    l_enterUser = createLabel('Enter Username: ', button_width, 0, 0, button_padx, button_pady, changPass_frame)
    l_enterPass = createLabel('Enter your Password: ', button_width, 1, 0, button_padx, button_pady, changPass_frame)
    l_enterPassConf =createLabel('Confirm Password: ', button_width, 2, 0, button_padx, button_pady, changPass_frame)
    l_enterPassUser = createLabel('Enter New Password: ', button_width, 3, 0, button_padx, button_pady, changPass_frame)
    l_enterNewPassConf = createLabel('Confirm New Password: ', button_width, 4, 0, button_padx, button_pady, changPass_frame)

    e_username = createEntry(20, 0, 1, button_padx, button_pady, changPass_frame)
    e_pass = createEntry(20, 1, 1, button_padx, button_pady, changPass_frame)
    e_passConf = createEntry(20, 2, 1, button_padx, button_pady, changPass_frame)
    e_newPass = createEntry(20, 3, 1, button_padx, button_pady, changPass_frame)
    e_newPassConf = createEntry(button_width, 4, 1, button_padx, button_pady, changPass_frame)

    b_confirm = createButton('Change Password', button_width, 5, 1, button_padx, button_pady, changPass_frame)
    b_cancel = createButton('Cancel',5, 5, 0, button_padx, button_pady, changPass_frame)
    b_cancel.config(command=lambda: editProfile(changPass_frame))

    #putting del profile frame on screen
    changPass_frame.pack(padx=10, pady=10)
    return


def changeUser():
    #hiding active frame
    hideFrame(editProfile_frame)
    root.title('Edit Profile - Change Username')
    
    #setting proper size
    root.geometry('400x300')

    #neccessary delete profile buttons, labels, textboxes
    l_enterUser = createLabel('Enter Username: ', button_width, 0, 0, button_padx, button_pady, changeUser_frame)
    l_enterPass = createLabel('Enter your Password: ', button_width, 1, 0, button_padx, button_pady, changeUser_frame)
    #l_enterPassConf = createLabel('Confirm Password: ', button_width, 2, 0, button_padx, button_pady, changeUser_frame)
    l_enterNewUser = createLabel('Enter New Username: ', button_width, 3, 0, button_padx, button_pady, changeUser_frame)

    e_username = createEntry(20, 0, 1, button_padx, button_pady, changeUser_frame)
    e_pass = createEntry(20, 1, 1, button_padx, button_pady, changeUser_frame)
    #e_passConf = createEntry(20, 2, 1, button_padx, button_pady, changeUser_frame)
    e_newUser = createEntry(20, 3, 1, button_padx, button_pady, changeUser_frame)

    b_confirm = createButton('Change Username', button_width, 4, 1, button_padx, button_pady, changeUser_frame)
    b_confirm.config(command=lambda: changeUserVer(e_username.get(), e_newUser.get(), e_pass.get()))
    b_cancel = createButton('Cancel',5, 4, 0, button_padx, button_pady, changeUser_frame)
    b_cancel.config(command=lambda: editProfile(changeUser_frame))
    
    #putting change user frame on screen
    changeUser_frame.pack(padx=10, pady=10)
    return

def specNumPrg(frame):
    # hiding the active frame
    hideFrame(frame)

    #setting size of frame
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

    specNum_list = [(str(i)+'. '+specNum_list[i]+ ' Number') for i in range(len(specNum_list))]
    
    #necessary combobox, dropdwn, buttons, etc.
    #Row 1
    e_num = createEntry(button_width, 1, 1, button_padx, button_padx, specNumPrg_frame)
    l_num = createLabel('Enter a number:', button_width, 1, 0, button_padx, button_pady, specNumPrg_frame)
    b_explain = createButton('Explanation', button_width, 0, 2, button_padx, button_pady, specNumPrg_frame)
    b_explain.config(command=lambda: spnExplain(combo.get(),l_spnExplain))


    #Row 2
    combo = ttk.Combobox(specNumPrg_frame,values=specNum_list,state='readonly')
    combo.current(0)
    combo.grid(row=0,column=1)
    l_combo = createLabel('Choose function: ', button_width, 0, 0, button_padx, button_pady, specNumPrg_frame)
    #l_spnExplain = createLabel('TEst',button_width, 1, 2, button_padx, button_pady, specNumPrg_frame) #INCREASE ROW SPAN
    l_spnExplain = Label(specNumPrg_frame, width=button_width, text='Test', wraplength=150)
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
    if choice.split(' ')[2] == 'Square':
        choice = 'Square'
    else:
        choice = choice.split(' ')[1]
    #print(f'{choice=}')
    label.config(text=spn.specnum_explain[choice])
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

def changeUserVer(old_user, new_user, password):
    #validate with Burgers DB and display message accordingly
    return
def changePassVer(user, old_password, new_password, new_passwordConfirm):
    #validate with Burgers DB and display message accordingly
    return

def delAccVer(user, password, passwordConfirm):
    #validate with Burgers DB and display message accordingly
    return
    
homescreen(None)
root.mainloop()

