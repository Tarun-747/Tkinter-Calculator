from tkinter import *

root = Tk()

root.geometry("415x320")
root.resizable(0, 0)
root.title("CALCULATOR")
root.configure(background="black")

a = StringVar()

# Function to show numbers and operations in the Entry widget
def show(b):
    if b == "=":
        equ()
    elif b == "AC":
        clear()
    else:
        # Clear the Entry widget if it's not an operator after '=' or 'AC'
        if "=" in a.get():
            clear()
        a.set(a.get() + b)

# Function to clear the Entry widget and reset StringVar
def clear():
    a.set("")
    e1.delete(0, END)  # Clear the Entry widget

# Function to evaluate the expression considering BODMAS rules
def equ():
    ex = a.get()
    try:
        # Use eval to evaluate the expression
        result = str(eval(ex))
        a.set(result)
    except Exception as e:
        # Handle errors, e.g., division by zero
        a.set("Error")

# Entry widget to display the expression
e1 = Entry(root, font=("", 30), justify="right", textvariable=a)
e1.place(x=0, y=0, width=415, height=50)

# Buttons creation for the calculator
button_texts = [
    ("(", 4, 55), (")", 106, 55), ("%", 208, 55), ("AC", 310, 55),
    ("7", 4, 107), ("8", 106, 107), ("9", 208, 107), ("/", 310, 107),
    ("4", 4, 159), ("5", 106, 159), ("6", 208, 159), ("*", 310, 159),
    ("1", 4, 211), ("2", 106, 211), ("3", 208, 211), ("-", 310, 211),
    ("0", 4, 263), (".", 106, 263), ("+", 208, 263), ("=", 310, 263)
]

for (text, x, y) in button_texts:
    Button(root, text=text, command=lambda t=text: show(t), bg="pink", activebackground="lightgreen").place(x=x, y=y, width=100, height=50)

# Binding the Return key to the equals function
root.bind('<Return>', lambda event=None: equ())

root.mainloop()
