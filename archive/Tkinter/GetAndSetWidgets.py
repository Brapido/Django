import tkinter as tk
import ttkbootstrap as ttk

def button_func():
    # get the content of the entry
    entry_text = entry.get()

    # update label
    # label.configure(text = entry.get())
    label['text'] = entry_text
    entry['state'] = 'disabled'
    button['state'] = 'disabled'

def button_func_2():
    label['text'] = 'I am a Label'
    entry['state'] = 'enabled'
    button['state'] = 'enabled'

# window
window = tk.Tk()
window.title('Getting and Setting Widgets')
window.geometry('300x300')

# widgets
label = ttk.Label(master = window, text = 'I am a Label')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'IButton', command = button_func)
button.pack()

button_2 = ttk.Button(master = window, text = 'Refresh', command = button_func_2)
button_2.pack()

# run
window.mainloop()