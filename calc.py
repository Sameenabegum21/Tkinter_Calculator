import tkinter as tk
'''Imports tkinter module
tk is an alias for easy access'''

#button click handler
def press(v):
    entry.insert(tk.END,v)
    '''called when a number or operator button is clicked
    Inserts the pressed value at the end of the entry Widget'''

def clear():
    entry.delete(0,tk.END)
    '''Clears the calculator screen
    Delets all characters from starting to end(index numbers)'''

def backspace():
    text=entry.get()
    if text:
        entry.delete(len(text)-1)

#Calculation function
def calc():
    try:
        result = eval(entry.get())
        '''entry.get() retrives the express e.g.(2+6)
        eval() evaluates the string as a python expression'''

        entry.delete(0, tk.END) #clears the old expression 
        entry.insert(0, result) #displays exception instead of crashing
    
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "invalid Expression")
        '''Handles invalid expression (e.g. 5++)
        Display "exception" instead of crashing'''

#main window creation
root = tk.Tk() #create the main application window

root.title("Calculation") #stes window title

root.configure(bg="#1e1e1e")#displays resizing of window

root.resizable(False, False) #disable resizing the window

#Entry widget (display screen)
entry = tk.Entry(
    root,
    font= ("Time new roman", 20),
    bg="#2d2d2d",
    fg="white",
    bd=0,
    justify="right"
)
'''text input feild
acts as calculator display
right-aligned for better calculator look'''
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12,ipady=10)

#button lables
button =[
    "7","8","7","/",
    "6","5","4","*",
    "3","2","1","-",
    "0",".","=","+",
]

'''represent calculator buttons
stored in list to reduse repetitive code'''

#dynamic button creation
r=1
c=0
'''rows and columns counter for grid layout'''
for b in button:
    cmd= calc if b=="=" else lambda x=b: press(x)
    '''if button is "=" , call calc()
    else, call press() with the button value
    lambda x=b prevents late binding issues'''


    tk.Button(
        root,text=b,
        command=cmd,#these three lines creates abutton widget
        font=("Calibri",14),
        width=5,
        height=2,
        bg="#ff9500" if b in "+-*/" else "#3a3a3a",
        fg="white",
        bd=0
    ).grid(row=r, column=c, padx=6, pady=6)
    c+=1
    if c==4:
        r+=1
        c=0
        '''moves to next row after 4 bttons'''

tk.Button(
    root,
    text="clear",
    command=clear,#these three lines creates abutton widget
    font=("Calibri",14),
    width=10,
    height=2,
    bg="#ff3b3b",
    fg="white",
    bd=0
).grid(row=r, column=0, columnspan=2, pady=2)
'''clears the calculator display screen
    spans accorss all columns'''

tk.Button(
    root,
    text="backspace",
    command=backspace,
    font=("calibri",14),
    width=8,
    height=2,
    bg="orange",
    fg="white",
    bd=1,


).grid(row=r, column=1, columnspan=9,padx=4, pady=4)
#event loop 
root.mainloop()
'''keeps the window running 
listens for user interactions'''    