from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT = "./images/card_front.png"
CARD_BACK = "./images/card_back.png"
TIME_TO_FLIP = 3
timer = None
rand_word_dict = None
words_lst = None


# -------------------------- FLIP THE CARD ----------------------------- #
def flip_card():
    global rand_word_dict, timer
    canvas.itemconfig(card_img, image=card_back_photo)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{rand_word_dict['English']}", fill="white")

# --------------------------- FLASH CARDS ------------------------------ #
try:
    # get the data into a data frame
    data = pandas.read_csv("./data/words to learn.csv")
    print("Words to learn selected")
except FileNotFoundError as error_msg:
    print(f'Unable to find word list. Error ->{error_msg}')
    data = pandas.read_csv("./data/french_words.csv")
finally:
    # convert data into a dictionary
    words_lst = data.to_dict(orient='records')


def change_word():
    global rand_word_dict, timer, words_lst
    window.after_cancel(timer)
    rand_word_dict = choice(words_lst)
    canvas.itemconfig(card_img, image=card_front_photo)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{rand_word_dict['French']}", fill="black")
    timer = window.after(3000, func=flip_card)


def right_button():
    global words_lst, rand_word_dict
    words_lst.remove(rand_word_dict)
    change_word()

# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)

card_front_photo = PhotoImage(file=CARD_FRONT)
card_back_photo = PhotoImage(file=CARD_BACK)
card_img = canvas.create_image(400, 263, image=card_front_photo)

language_text = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="trouve", fill="black", font=("Arial", 60, "bold"))


canvas.grid(row=0, column=0, columnspan=2)

# buttons
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_bt = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, relief="flat", command=change_word)
wrong_bt.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_bt = Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, relief="flat", command=right_button)
right_bt.grid(row=1, column=1)

timer = window.after(3000, func=flip_card)
change_word()

window.mainloop()

new_data_frame = pandas.DataFrame(words_lst)
new_data_frame.to_csv("data/words to learn.csv", index=False)
