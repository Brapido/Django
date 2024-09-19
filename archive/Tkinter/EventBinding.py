import tkinter as tk
from tkinter import ttk
# Format: modifier-type-detail
# Example: Alt-Keypress-a

# setup
window = tk.Tk()
window.title('Event Binding')
window.geometry('600x500')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text = 'A button')
btn.pack()

# events
window.bind('<Alt-KeyPress-a>', lambda event: print('An event'))

# run
window.mainloop()