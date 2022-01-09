button_widg_dict = {
    'act_bg':None,
    'act_fg':None,
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
    'w':None,
    'wraplength':None
}
'''
all customisation PARAMS for BUTTON():
1	activebackground	The Background color when the cursor is over the button.
2	activeforeground	The Foreground color when the cursor is over the button.
3	bg	Background Color of the button
4	bd	Border size of frame in pixels. Default is 2.
5	command	Command to be executed when button is clicked. Typically set to a function call.
6	fg	foreground color
7	font	Text font for the button
8	height	Height of the button
9	highlightcolor	The text color when the widget is under focus.
10	image	Image to be displayed on the button. By default, image will replace the text.
11	justify	Changes the alignment of the text. Can be set to either LEFT, CENTER or RIGHT.
12	padx	padding to the left and right of the text.
13	pady	padding above and below the text.
14	relief	It specifies the type of the border. Default is Flat, other options include raised, flat, ridge, groove and sunken.
15	state	Default is NORMAL. DISABLED causes the button to gray out and go inactive. ACTIVE is the state of the button when mouse is over it.
16	underline	Default is -1. Set this option to under line the button text.
17	width	Width of the button
18	wraplength	If the value is set to a positive number, the text lines will be wrapped to fit within this length
'''

grid_dict = {
    'column':None,
    'row':None,
    'cspan':None,
    'rspan':None,
    'padx':None,
    'pady':None,
    'ipadx':None,
    'ipady':None
}

'''
all customisation PARAMS for GRID():
column − The column to put widget in; default 0 (leftmost column).

columnspan − How many columns widgetoccupies; default 1.

ipadx, ipady − How many pixels to pad widget, horizontally and vertically, inside widget's borders.

padx, pady − How many pixels to pad widget, horizontally and vertically, outside v's borders.

row − The row to put widget in; default the first row that is still empty.

rowspan − How many rowswidget occupies; default 1.
'''


lab_dict = {
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
    'w':None,
    'wraplength':None
}
'''
all customisation PARAMS for LABEL():
1	
anchor

This options controls where the text is positioned if the widget has more space than the text needs. The default is anchor=CENTER, which centers the text in the available space.

2	
bg

The normal background color displayed behind the label and indicator.

3	
bitmap

Set this option equal to a bitmap or image object and the label will display that graphic.

4	
bd

The size of the border around the indicator. Default is 2 pixels.

5	
cursor

If you set this option to a cursor name (arrow, dot etc.), the mouse cursor will change to that pattern when it is over the checkbutton.

6	
font

If you are displaying text in this label (with the text or textvariable option, the font option specifies in what font that text will be displayed.

7	
fg

If you are displaying text or a bitmap in this label, this option specifies the color of the text. If you are displaying a bitmap, this is the color that will appear at the position of the 1-bits in the bitmap.

8	
height

The vertical dimension of the new frame.

9	
image

To display a static image in the label widget, set this option to an image object.

10	
justify

Specifies how multiple lines of text will be aligned with respect to each other: LEFT for flush left, CENTER for centered (the default), or RIGHT for right-justified.

11	
padx

Extra space added to the left and right of the text within the widget. Default is 1.

12	
pady

Extra space added above and below the text within the widget. Default is 1.

13	
relief

Specifies the appearance of a decorative border around the label. The default is FLAT; for other values.

14	
text

To display one or more lines of text in a label widget, set this option to a string containing the text. Internal newlines ("\n") will force a line break.

15	
textvariable

To slave the text displayed in a label widget to a control variable of class StringVar, set this option to that variable.

16	
underline

You can display an underline (_) below the nth letter of the text, counting from 0, by setting this option to n. The default is underline=-1, which means no underlining.

17	
width

Width of the label in characters (not pixels!). If this option is not set, the label will be sized to fit its contents.

18	
wraplength

You can limit the number of characters in each line by setting this option to the desired number. The default value, 0, means that lines will be broken only at newlines.
'''


entry_dict = {
    'master':None,
    'bd':None,
    'height':None,
    'width':None,
    'bg':None,
    'fg':None,
    'font':None,
    'insetofftime':None,
    'insetontime':None,
    'padx':None,
    'pady':None,
    'highthick':None,
    'charwidth':None,
    'relief':None,
    'yscrollcommand':None,
    'xscrollcommand':None,
}