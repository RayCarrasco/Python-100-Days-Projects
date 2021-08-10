from tkinter import *


def covert(miles):
    return miles * 1.60934


def update():
    result_km = covert(int(entry.get()))
    lab_result.config(text=f"{result_km:.5f}")


# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=50, width=300)
window.config(padx=50, pady=25)

# Labels
lab_miles = Label(text="Miles")
lab_miles.grid(row=0, column=2)

lab_is_equal = Label(text="is equal to")
lab_is_equal.grid(row=1, column=0)

lab_result = Label(text="0")
lab_result.grid(row=1, column=1)

lab_km = Label(text="Km")
lab_km.grid(row=1, column=2)


# Entry
entry = Entry(width=5)
entry.grid(row=0, column=1)
entry.insert(END, string="0")


# Button 1
calculate_button = Button(text="Calculate", command=update)
calculate_button.grid(row=2, column=1)


window.mainloop()
