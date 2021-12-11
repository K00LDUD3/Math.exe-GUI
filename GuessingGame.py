from tkinter import *
from tkinter import ttk

root=Tk()

def onReturn(event, text):
    #text = 'hi'
    print(f'{text=}')
    print(f'{type(text)=}')

def callback(sv):
    print(sv.get())

def run():
    sv = StringVar()
    sv.trace('w', lambda name, index, mode, sv=sv: callback(sv))
    e = Entry(root, textvariable=sv)
    e.bind('<Return>', lambda event: onReturn( event, e.get()))
    e.pack()

    b = Button(text='GO', command=lambda: onReturn(None, e.get()))
    b.pack()


run()
root.mainloop()