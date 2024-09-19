import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title('button')
window.geometry('600x400')

# button
def button_func():
    #print('A basic button')
    print(radio_var.get())

button_string = tk.StringVar(value = 'A button with string var')

button = ttk.Button(window, text = 'A simple button', command = button_func, textvariable = button_string)
button.pack()

# checkbutton
check_var = tk.IntVar(value = 10)
check = ttk.Checkbutton(
    window, 
    text = 'checkbox 1',
    command = lambda: print(check_var.get()),
    variable = check_var,
    onvalue = 10,
    offvalue = 5)
check.pack()

check2 = ttk.Checkbutton(
    window,
    text = 'Check box 2',
    command = lambda: check_var.set(5),
    onvalue = 5,
    offvalue = 10)
check2.pack()

# radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text = 'Radiobutton1', 
    value = 'radio 1', 
    variable = radio_var,
    command = lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(
    window, 
    text = 'Radiobutton2',
    value = 2,
    variable = radio_var)
radio2.pack()


#Excercise
def radio_func():
    print(check_bool.get())
    check_bool.set(False)

radio_string = tk.StringVar()
check_bool = tk.BooleanVar()
radio3 = ttk.Radiobutton(
    window, 
    text = 'Radio A',
    value = 'A',
    command = radio_func,
    variable = radio_string)
radio3.pack()

radio4 = ttk.Radiobutton(
    window, 
    text = 'Radio B',
    value = 'B',
    command = radio_func,
    variable = radio_string)
radio4.pack()

check3 = ttk.Checkbutton(
    window,
    text = 'exercise',
    variable = check_bool,
    command = lambda: print(radio_string.get()))
check3.pack()
# run 
window.mainloop()
