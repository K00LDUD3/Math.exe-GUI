from tkinter import *
from tkinter import ttk

root=Tk()
frame = LabelFrame(root)

def onReturn(event, text):
    #text = 'hi'
    print(f'{text=}')
    print(f'{type(text)=}')

def callback(sv):
    print(sv.get())

def run():
    sv = StringVar()
    #sv.trace('w', lambda name, index, mode, sv=sv: callback(sv))
    e = Entry(frame, textvariable=sv)
    e.bind('<Return>', lambda event: onReturn( event, e.get()))
    e.place(relheight=0.45, relwidth=0.9, relx=0.05, rely=0.55)

    b = Button(text='GO', command=lambda: onReturn(None, e.get()))
    b.place(relheight=0.5, relwidth=0.9, relx=0.05, rely=0.05)


    frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)


run()
root.mainloop()