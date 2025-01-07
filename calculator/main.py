from cProfile import label
from tkinter import *

calc = Tk()
calc.geometry("242x280")  # Adjusted window size
calc.title('Calculator')

e = Entry(calc, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_multi():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_percent():
    first_number = e.get()
    global f_num
    global math
    math = "percent"
    f_num = int(first_number)
    e.delete(0, END)

def button_equals():
    second_number = e.get()
    e.delete(0, END)
    try:
        if math == "addition":
            e.insert(0, f_num + int(second_number))
        if math == "subtraction":
            e.insert(0, f_num - int(second_number))
        if math == "division":
            # Handle division by zero
            if int(second_number) == 0:
                e.insert(0, "Error: Div by 0")
            else:
                e.insert(0, f_num / int(second_number))
        if math == "multiplication":
            e.insert(0, f_num * int(second_number))
        if math == "percent":
            e.insert(0, (f_num * int(second_number)) / 100)  # Corrected percentage calculation
    except ValueError:
        e.insert(0, "Invalid Input")

button_0 = Button(calc, text="0", padx=20, pady=10, command=lambda: button_click(0))
button_1 = Button(calc, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = Button(calc, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = Button(calc, text="3", padx=20, pady=10, command=lambda: button_click(3))
button_4 = Button(calc, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = Button(calc, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = Button(calc, text="6", padx=20, pady=10, command=lambda: button_click(6))
button_7 = Button(calc, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = Button(calc, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = Button(calc, text="9", padx=20, pady=10, command=lambda: button_click(9))
button_clear = Button(calc, text="clear", padx=10, pady=10, command=button_clear)
button_equals = Button(calc, text="=", padx=19, pady=10, command=button_equals)
button_add = Button(calc, text="+", padx=18, pady=10, command=button_add)
button_sub = Button(calc, text="-", padx=20, pady=10, command=button_sub)
button_div = Button(calc, text="/", padx=20, pady=10, command=button_div)
button_multi = Button(calc, text="*", padx=20, pady=10, command=button_multi)
button_percent = Button(calc, text="%", padx=18, pady=13, command=button_percent)
label = Label(calc, text="", relief="raised", width=24, height=3)  # Empty label


button_0.grid(row=4, column=1)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_clear.grid(row=4, column=0)
button_equals.grid(row=4, column=2)
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_div.grid(row=3, column=3)
button_multi.grid(row=4, column=3)
button_percent.grid(row=5, column=3)
label.grid(row=5, column=0, columnspan=3)



calc.mainloop()
