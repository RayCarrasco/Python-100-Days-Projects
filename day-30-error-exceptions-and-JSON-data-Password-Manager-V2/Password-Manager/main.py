""""
Password manager that saves all your passwords locally in plain text :v
@author: Raymundo C.
@companny: none :(
"""

from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

# ---------------------------- SEARCH ENGINE ------------------------------- #
def search():
    search_word = website_entry.get()
    if len(search_word) > 0:
        try:
            with open("data.json", 'r') as data_file:
                data = json.load(data_file)
                searched_password = data[search_word]
        except FileNotFoundError:
            title = 'File Not Found'
            message = "No Data File Found"
        except KeyError:
            title = "Not in the data"
            message = "No details for the website exist"
        else:
            clean_fields(default=False)
            title = "Success"
            message = "Fields substituted by the stored values"
            username_entry.insert(0, f"{searched_password['email']}")
            password_entry.insert(0, f"{searched_password['password']}")
        finally:
            messagebox.showinfo(title=title, message=message)



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():
    """
    Generates a password on the password field and copy it to clipboard
    :return: Nothing
    """
    generated_password = [choice(LETTERS) for _ in range(randint(8, 10))]
    generated_password.extend(choice(NUMBERS) for _ in range(randint(2, 4)))
    generated_password.extend(choice(SYMBOLS) for _ in range(randint(2, 4)))
    shuffle(generated_password)
    generated_password = ''.join(generated_password)

    password_entry.delete(0, 'end')
    password_entry.insert(END, f"{generated_password}")
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(website, user_name, password):
    """
    Saves the new password data to data.txf verifying for empty fields.
    :param website: Website direction on the website field
    :param user_name: Username entered in the Email/Username field
    :param password: Password generated or entry by the user in the password field
    :return: Nothing
    """
    new_data = {website: {
        "email": user_name,
        "password": password,
    }}
    if len(website) == 0 or len(user_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please, do not leave any fields empty.")
        confirmation = False
    else:
        # How to write
        # with open("data.json", "w") as data_file:
        #     json.dump(new_data, data_file, indent=4)

        # How to read
        # with open("data.json", 'r') as data_file:
        #     data = json.load(data_file)
        #     print(data)

        # How to update data
        # with open("data.json", 'r') as data_file:
        #     data = json.load(data_file)
        #     data |= new_data
        # with open("data.json", 'w') as data_file:
        #     json.dump(data, data_file, indent=4)

        # Try read the file
        try:
            with open("data.json", 'r') as data_file:
                data = json.load(data_file)
        # if file do not exist, then create it
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        # in other case add the data to the JSON file
        else:
            data |= new_data
            with open("data.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            clean_fields()


def clean_fields(default=True):
    """
    Set the entry fields o the default state
    :return: Nothing
    """
    username_entry.delete(0, 'end')
    if default:
        username_entry.insert(END, "example@mail.com")
        website_entry.delete(0, 'end')
    password_entry.delete(0, 'end')


def add():
    """
    Get the fields data and call the save function
    :return: Nothing
    """
    website = website_entry.get()
    user_name = username_entry.get()
    password = password_entry.get()
    save(website, user_name, password)


# ---------------------------- UI SETUP ------------------------------- #
# Window creation with 20 px of padding and title


window = Tk()
window.title("Password Manager")
window.configure(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
# image added in the center of the window
canvas.create_image(100, 100, image=lock_img)

# use of the geometric system to show the changes
canvas.grid(row=0, column=1)

# labels
website_lb = Label(text="Website: ")
website_lb.grid(row=1, column=0)

username_lb = Label(text="Email/Username: ")
username_lb.grid(row=2, column=0)

password_lb = Label(text="Password: ")
password_lb.grid(row=3, column=0)

# entries
# sticky method is used to occupate the full space of the cell in the grid
# it takes compass directions: N, E, S, W, NE, NW, SE, and SW and zero, for example
# NESW will make the widget to take up the full area, in this case EW means to occupate
# the area filling it from east to west
website_entry = Entry()
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

username_entry = Entry()
# END is a TKinter constant that means the end of the string in that object
# if insert at the beginning is needed the index could be 0
# if insert after the n character is needed can be specified by replacing n for an integer
username_entry.insert(END, string="example@mail.com")
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# buttons
generate_password_bt = Button(text="Generate Password", command=password_generator)
generate_password_bt.grid(row=3, column=2)

add_bt = Button(text="Add", command=add)
add_bt.grid(row=4, column=1, columnspan=2, sticky="EW")

search_bt = Button(text="Search", command=search)
search_bt.grid(row=1, column=2, sticky="EW")

# windows main loop to keep the window showing on the screen
window.mainloop()
