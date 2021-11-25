from tkinter import *
import tkinter.font as font
from types import BuiltinMethodType

root = Tk()
root.title('Calculator')

#Frame
frame = LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10,pady=10)

button_list = []

#button Param Variables
button_width = 5
button_height = 5
button_padx = 0
button_pady = 10
button_borderwidth = 1
button_font = font.Font(size=15)


#func
def EvalExp():
    exp = label.cget('text')
    try:
        exp = exp.replace('^','**')
        formatVal = float("{:.3f}".format(float(eval(exp))))
        if int(formatVal) == formatVal:
            formatVal = int(formatVal)
        label.config(text=str(formatVal))
    except:
        label.config(text='ERROR')



def clear():
    label.config(text='')

def AddNumOperator(OpNum):
    exp = label.cget('text')
    print(type(exp), exp)
    if 'ERROR' in(exp):
        exp = ''
    
    #exp.replace('ERROR','')
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

#Button customizer func
def createNumberButtons():
    #assigning values of buttons (1-9, 0)
    for i in range(0,9):
        button_list.append(Button(root, width=button_width, text = (i+1), font=button_font))
        button_list[i].grid(row=i//3+1, column=i%3, padx = button_padx, pady = button_pady)

    button_list.append(Button(root, width=button_width, text = 0, font=button_font))
    button_list[9].grid(row=4, column=1, padx = button_padx, pady = button_pady)


    button_list[9].config(command = lambda: AddNumOperator('0'))

    button_list[0].config(command = lambda: AddNumOperator('1'))
    button_list[1].config(command = lambda: AddNumOperator('2'))
    button_list[2].config(command = lambda: AddNumOperator('3'))
    button_list[3].config(command = lambda: AddNumOperator('4'))
    button_list[4].config(command = lambda: AddNumOperator('5'))
    button_list[5].config(command = lambda: AddNumOperator('6'))
    button_list[6].config(command = lambda: AddNumOperator('7'))
    button_list[7].config(command = lambda: AddNumOperator('8'))
    button_list[8].config(command = lambda: AddNumOperator('9'))

def Backspace():
    exp = label.cget('text')
    exp = exp.strip()
    exp = exp[0:len(exp)-1]
    label.config(text=exp)

#Clear button
AC = Button(root, width=button_width, text = 'clear', command = clear, font=button_font)
AC.grid(row=1, column=4)

#decimal point button
point = Button(root, width=button_width, text = '.', command=lambda: AddNumOperator('.'), font=button_font)
point.grid(row=4, column=2, padx=button_padx, pady=button_pady)

#operator buttons
op_font = button_font
#op_font.config(weight='bold')
op_add = Button(root, width=button_width, text='+', command=lambda: AddNumOperator('+'), font=op_font)
op_subtract = Button(root, width=button_width, text='-', command=lambda: AddNumOperator('-'), font=op_font)
op_multiply = Button(root, width=button_width, text='*', command=lambda: AddNumOperator('*'), font=op_font)
op_divide = Button(root, width=button_width, text='/', command=lambda: AddNumOperator('/'), font=op_font)
op_modulus = Button(root, width=button_width, text='mod', command=lambda: AddNumOperator('%'), font=op_font)
op_power = Button(root, width=button_width, text='^', command=lambda: AddNumOperator('^'), font=op_font)

op_add.grid(row=1, column=3, padx = button_padx, pady = button_pady)
op_subtract.grid(row=2, column=3, padx = button_padx, pady = button_pady)
op_multiply.grid(row=3, column=3, padx = button_padx, pady = button_pady)
op_divide.grid(row=4, column=3, padx = button_padx, pady = button_pady)
op_modulus.grid(row=4, column=0, padx=button_padx, pady=button_pady)
op_power.grid(row=3, column=4, padx=button_padx, pady=button_pady)

op_button_list = [op_add, op_subtract, op_multiply, op_divide, op_modulus, op_power]

#'=' button
__equal = Button(root, width=button_width, text='=', command=EvalExp, font=button_font)
__equal.grid(row=2, column=4, padx = button_padx, pady = button_pady)

#backspace button
__backspace = Button(root, width=button_width, text='del', command=Backspace, font=button_font)
__backspace.grid(row=4, column=4, padx = button_padx, pady = button_pady)

#Creating Display Label
label = Label(root, text='10', width=55, height=2)
label.grid(row=0, column=0, columnspan=4)
createNumberButtons()
root.resizable(False, False)


root.mainloop()