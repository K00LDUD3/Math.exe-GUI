from tkinter import *
from tkinter import ttk

root=Tk()

def onReturn(event, text):
    #text = 'hi'
    print(f'{text=}')
    print(f'{type(text)=}')

def run():
    e = Entry(root)
    e.bind('<Return>', lambda event: onReturn( event, e.get()))
    e.pack()

    b = Button(text='GO', command=lambda: onReturn(None, e.get()))
    b.pack()

run()
root.mainloop()