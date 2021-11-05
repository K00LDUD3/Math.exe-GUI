'''
LINKS
tkinter basic stuff ===== https://www.javatpoint.com/python-tkinter

'''
#importing libs, and modules
import Special_Numbers as sp
from tkinter import *
from tkinter import ttk

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
#root.resizable(False, False)

#creating necessary frames
editProfile_frame = LabelFrame(root)
homescreen_frame = LabelFrame(root)
deleteProfile_frame = LabelFrame(root) 
changeUser_frame = LabelFrame(root)
changPass_frame = LabelFrame(root)
specNumPrgMenu_frame = LabelFrame(root)
specNumPrg_frame = LabelFrame(root)

#function for hiding given frame
def hideFrame(frame):
    try:
        frame.pack_forget()
        print('<<<Frame hidden successfully...>>>')
        print(f'{frame=}')
    except:
        print('<<<No active Frame>>>')
    return

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
def comboclick(event):
    print(combo.get())

def specNumPrgPreSpExecEval(choice, num_raw, lab):
    num = 0
    mess = 'hello'
    TF = False
    if num_raw.isnumeric():
        num = int(num_raw)
        TF = (sp.evalSpecNum(choice, num))

        if TF:
            mess = f'{num} is {choice}'
        else:
            mess = f'{num} is not {choice}'
    else:
        mess = 'Invalid Number! Please Try Again...'
    
    lab.config(text=mess)
    print(f'{TF=} --- {choice=} ---', type(num))
    return



#homescreen frame
def homescreen(frame):
    #hiding active (if any) frame
    hideFrame(frame)
    root.geometry('365x150')
    root.title('Homescreen')
    
    #necessary buttons
    b_editProfile = createButton('Edit Profile', button_width, 0,0, button_padx, button_pady, homescreen_frame)
    b_specNumPrg = createButton('Special Number Programs', button_width,0,1, button_padx, button_pady, homescreen_frame)
    b_calc = createButton('Scienctific Calculator', button_width,1,0, button_padx, button_pady, homescreen_frame)
    b_guessGame = createButton('Guessing Game',button_width,1,1, button_padx, button_pady, homescreen_frame)
    b_signOut = createButton('Sign Out',button_width,2,0, button_padx, button_pady, homescreen_frame)

    b_editProfile.config(command=lambda: editProfile(homescreen_frame))
    b_specNumPrg.config(command=lambda: specNumPrgMenu(homescreen_frame))

    homescreen_frame.pack()
    



def editProfile(frame):
    #hiding the active frame
    hideFrame(frame)

    root.title('Edit Profile')
    ## CHANGE SIZE, GET PROPER SIZE
    size = str(editProfile_frame.winfo_width())+'x'+str(editProfile_frame.winfo_height())
    print(size)
    root.geometry('200x200')
    #necessary edit profile buttons
    b_changeUser = createButton('Change Username', button_width, 0, 0, button_padx, button_pady, editProfile_frame)
    b_changePass = createButton('Change Password', button_width, 1, 0, button_padx, button_pady, editProfile_frame)    
    b_delProfile = createButton('Delete Account', button_width, 2, 0, button_padx, button_pady, editProfile_frame)    
    b_Homescreen = createButton('Back to Homescreen', button_width, 3, 0, button_padx, button_pady, editProfile_frame)
    
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

    #necessary delete profile buttons, labels, textboxes
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

    #necessary delete profile buttons, labels, textboxes
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

    #necessary delete profile buttons, labels, textboxes
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
def specNumPrgMenu(frame):
    # hiding the active frame
    hideFrame(frame)

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
                    'Square Root of a',
                    'Strong',
                    'Pronic',
                    'Spy',
                    'Tech',
                    'Prime']

    specNum_list = [(str(i)+'. '+specNum_list[i]+ ' Number') for i in range(len(specNum_list))]

    #necessary combobox, dropdwn, buttons, etc.
    combo = ttk.Combobox(specNumPrgMenu_frame, values=specNum_list, state='readonly', width=26, height=30)
    combo.current(0)
    combo.bind(comboclick)
    combo.grid(row=0, column=0, columnspan=2)
    #create submit BUTTON
    b_go = createButton('Go', 10, 1, 1, button_padx, button_pady, specNumPrgMenu_frame)
    b_back = createButton('Back', 10, 1, 0, button_padx, button_pady, specNumPrgMenu_frame)
    
    b_back.config(command=lambda: homescreen(specNumPrgMenu_frame))
    b_go.config(command=lambda: specNumPrg(specNumPrgMenu_frame, combo.get()))
    combo.grid(row=0, column=0)

    #showing everything on screen
    specNumPrgMenu_frame.pack()
    

def specNumPrg(frame, choiceRaw):
    #hiding active frame
    hideFrame(frame)

    #extracting minimum requirements to open different frames according to the choice entered
    choice = choiceRaw.split(' ')[1]

    #setting window title
    root.title(str(choice+' Number'))
    if choice == 'Odd':
        root.title('Odd or Even Number')

    #necessary buttons, labels, entrys, etc
    l_enterNum = createLabel('Enter a number: ', button_width, 0,0,button_padx, button_pady, specNumPrg_frame)
    l_result = createLabel('', button_width, 1, 0, button_padx, button_pady, specNumPrg_frame)

    b_go = createButton('Go', button_width, 2, 1, button_padx, button_pady, specNumPrg_frame)
    b_back = createButton('Back', 10, 2, 0, button_padx, button_pady, specNumPrg_frame)

    e_num = createEntry(button_width, 0, 1, button_padx, button_pady, specNumPrg_frame)

    #setting commands for buttons
    b_back.config(command=specNumPrgMenu(specNumPrg_frame))
    b_go.config(command=lambda: specNumPrgPreSpExecEval(choice, e_num.get(), l_result)) # special number program pre special number execution evaluate
    

    #showing everything on screen
    specNumPrg_frame.pack()

    return
    


def changeUserVer(old_user, new_user, password):
    #validate with DB and display message accordingly
    return
def changePassVer(user, old_password, new_password, new_passwordConfirm):
    #validate with DB and display message accordingly
    return

def delAccVer(user, password, passwordConfirm):
    #validate with DB and display message accordingly
    return
homescreen(None)
root.mainloop()

