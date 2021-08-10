from tkinter import *

# Window
window = Tk()
window.title("Example")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label
label = Label(text="New Text")
label.grid(column=0, row=0)
label.config(padx=15, pady=15)

# Button 1
button1 = Button(text="Button 1")
button1.grid(column=2, row=0)

# Button 2
button2 = Button(text="Button 2")
button2.grid(column=1, row=1)

# Entry
entry = Entry(width=30)
entry.grid(column=3, row=2)

window.mainloop()
