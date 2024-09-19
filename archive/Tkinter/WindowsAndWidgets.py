import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def button_func():
        print('The button was pressed')

def button_func2():
        print('hello')


#create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

# tk text
text = tk.Text(master = window)
text.pack()

# tkk entry
entry = ttk.Entry(master = window)
entry.pack()

# 2nd label
label_2 = ttk.Label(master = window, text = 'my label')
label_2.pack()

# ttk button
button = ttk.Button(master = window, text = 'A button', command = button_func)
button.pack()

# ttk 2nd button
#button_2 = ttk.Button(master = window, text = 'My button', command = button_func2)
button_2 = ttk.Button(master = window, text = 'My button', command = lambda: print('hello')) #lambda stand alone function on code line.
button_2.pack()

# run
window.mainloop()
#print('Hello')
