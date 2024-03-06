from tkinter import *

def buttonPress(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text) # prints inputs onto the screen


def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total

    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""

    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""


def clear():
    global equation_text
    equation_label.set("") # empties all inputs
    equation_text = ""


window = Tk()
window.title("Calculator Game") # this is the Title
window.geometry("500x500") # This is the size of the window
equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("consolas", 20), bg="white", width=24, height=2) # this is the display
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda:buttonPress(1))
button1.grid(row=0, column=0) # this just gets the button onto the screen 

button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda:buttonPress(2))
button2.grid(row=0, column=1)
button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda:buttonPress(3))
button3.grid(row=0, column=2)
button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda:buttonPress(4))
button4.grid(row=1, column=0)
button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda:buttonPress(5))
button5.grid(row=1, column=1)
button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda:buttonPress(6))
button6.grid(row=1, column=2)
button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda:buttonPress(7))
button7.grid(row=2, column=0)
button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda:buttonPress(8))
button8.grid(row=2, column=1)
button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda:buttonPress(9))
button9.grid(row=2, column=2)
button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda:buttonPress(0))
button0.grid(row=3, column=1) # this just gets the button onto the screen   

# SYMBOLS
plus = Button(frame, text="+", height=4, width=9, font=35, command=lambda:buttonPress("+"))
plus.grid(row=0, column=3) # this just gets the button onto the screen   

minus = Button(frame, text="-", height=4, width=9, font=35, command=lambda:buttonPress("-"))
minus.grid(row=1, column=3) # this just gets the button onto the screen   

multiply = Button(frame, text="x", height=4, width=9, font=35, command=lambda:buttonPress("x"))
multiply.grid(row=2, column=3) # this just gets the button onto the screen   

divide = Button(frame, text="/", height=4, width=9, font=35, command=lambda:buttonPress("/"))
divide.grid(row=3, column=3) # this just gets the button onto the screen   

equal = Button(frame, text="=", height=4, width=9, font=35, command=equals)
equal.grid(row=3, column=2) # this just gets the button onto the screen   

decimal = Button(frame, text=".", height=4, width=9, font=75, command=lambda:buttonPress("."))
decimal.grid(row=3, column=0) # this just gets the button onto the screen  

clears = Button(window, text="C", height=4, width=15, font=75, command=clear)
clears.pack() # this just gets the button onto the screen  

window.mainloop()