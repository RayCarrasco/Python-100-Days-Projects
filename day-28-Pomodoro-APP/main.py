from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    window.after_cancel(timer)
    label_message.config(text="Timer", fg=GREEN)
    label_ticks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global rep
    rep = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep
    rep += 1
    print(rep)

    if rep % 8 == 0:
        active_time = LONG_BREAK_MIN
        message = "Break"
        colour = RED
    elif rep % 2 == 0:
        active_time = SHORT_BREAK_MIN
        message = "Break"
        colour = PINK
    else:
        active_time = WORK_MIN
        message = "Work"
        colour = GREEN

    label_message.config(text=message, fg=colour)
    count_down(active_time * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
from math import floor

def count_down(count):
    global rep
    count_minutes = floor(count / 60)
    count_seconds = floor(count % 60)

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count_seconds == 0:
        count_seconds = "00"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        message = "✔" * (rep // 2)
        label_ticks.config(text=message)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=40, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# Timer text
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)

# Text
label_message = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
label_message.grid(row=0, column=1)

label_ticks = Label(fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
label_ticks.grid(row=3, column=1)

# Buttons
button_start = Button(text="Start", command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(row=2, column=2)

window.mainloop()
