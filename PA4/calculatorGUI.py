# create a GUI calculator using tkinter
# Name: Yuhua Huang
# 6 March, 2023 
# creating a calculator using tkinter and draw and implement the calculator out 

from tkinter import *


def calculate(expression):
    try:
        result = eval(expression)
    except:
        result = "Error"
    return result


def calculator(gui):
    # name the gui window
    gui.title("Calculator")
    # make a entry text box
    entrybox = Entry(gui, width=36, borderwidth=5)
    # position the entry text box in the gui window using the grid manager
    entrybox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # create buttons: 1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=
    b0 = addButton(gui, entrybox, '0')
    b1 = addButton(gui, entrybox, '1')
    b2 = addButton(gui, entrybox, '2')
    b3 = addButton(gui, entrybox, '3')
    b4 = addButton(gui, entrybox, '4')
    b5 = addButton(gui, entrybox, '5')
    b6 = addButton(gui, entrybox, '6')
    b7 = addButton(gui, entrybox, '7')
    b8 = addButton(gui, entrybox, '8')
    b9 = addButton(gui, entrybox, '9')
    b_add = addButton(gui, entrybox, '+')
    b_sub = addButton(gui, entrybox, '-')
    b_mult = addButton(gui, entrybox, '*')
    b_div = addButton(gui, entrybox, '/')
    b_clr = addButton(gui, entrybox, 'c')
    b_eq = addButton(gui, entrybox, '=')

    # add buttons to the grid
    buttons = [b7, b8, b9, b_clr,
               b4, b5, b6, b_sub,
               b1, b2, b3, b_add,
               b_mult, b0, b_div, b_eq]
    k = 4
    for i in range(k):
        for j in range(k):
            buttons[i * k + j].grid(row=i+1, column=j, columnspan=1)


def addButton(gui, entrybox, value):
    if value == 'c':
        return Button(gui, text=value, height=4, width=9, command=lambda: entrybox.delete(0, END))
    elif value == '=':
        return Button(gui, text=value, height=4, width=9, command=lambda: entrybox.insert(END, f" = {calculate(entrybox.get())}"))
    else:
        return Button(gui, text=value, height=4, width=9, command=lambda: entrybox.insert(END, value))


def clickButton(entrybox, value):
    # the function clickButton() is not implemented!!!
    print(value)  # for debugging


# main program
# create the main window
gui = Tk()
# create the calculator layout
calculator(gui)
# update the window
gui.mainloop()
