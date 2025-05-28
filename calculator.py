from tkinter import *

win = Tk()
win.title('Stylish Calculator')
win.geometry('515x365')
win.resizable(0, 0)
win.configure(bg='#1e1e1e')  # Dark background

# Global variables
expression = ""
input_text = StringVar()

# Function for button click
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to clear the input field
def bt_clear():
    global expression
    expression = ""
    input_text.set("")

# Function to evaluate the result
def bt_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

# Input field frame
input_frame = Frame(win, width=312, height=50, bg="#1e1e1e")
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('Segoe UI', 20), fg="#00FFAB", bg="#2e2e2e", width=45, bd=0, justify=RIGHT, textvariable=input_text, insertbackground='white')
input_field.grid(row=0, column=0)
input_field.pack(ipady=15, pady=10)

# Button frame
btns_frame = Frame(win, width=310, height=270, bg="#1e1e1e")
btns_frame.pack()

# Button styling function
def create_button(text, row, column, colspan=1, width=10, cmd=None, color="#3c3c3c", fg="#ffffff"):
    btn = Button(btns_frame, text=text, width=width, height=3, fg=fg, bg=color,
                 bd=0, cursor='hand2', activebackground="#5a5a5a", command=cmd)
    btn.grid(row=row, column=column, columnspan=colspan, padx=3, pady=3)

# Buttons
create_button("C", 0, 0, colspan=3, width=38, cmd=bt_clear, color="#d7263d", fg="white")
create_button("/", 0, 3, cmd=lambda: btn_click("/"), color="#0077b6")

create_button("7", 1, 0, cmd=lambda: btn_click(7))
create_button("8", 1, 1, cmd=lambda: btn_click(8))
create_button("9", 1, 2, cmd=lambda: btn_click(9))
create_button("*", 1, 3, cmd=lambda: btn_click("*"), color="#0077b6")

create_button("4", 2, 0, cmd=lambda: btn_click(4))
create_button("5", 2, 1, cmd=lambda: btn_click(5))
create_button("6", 2, 2, cmd=lambda: btn_click(6))
create_button("-", 2, 3, cmd=lambda: btn_click("-"), color="#0077b6")

create_button("1", 3, 0, cmd=lambda: btn_click(1))
create_button("2", 3, 1, cmd=lambda: btn_click(2))
create_button("3", 3, 2, cmd=lambda: btn_click(3))
create_button("+", 3, 3, cmd=lambda: btn_click("+"), color="#0077b6")

create_button("0", 4, 0, colspan=2, width=24, cmd=lambda: btn_click(0))
create_button(".", 4, 2, cmd=lambda: btn_click("."))
create_button("=", 4, 3, cmd=bt_equal, color="#00b4d8")

win.mainloop()
