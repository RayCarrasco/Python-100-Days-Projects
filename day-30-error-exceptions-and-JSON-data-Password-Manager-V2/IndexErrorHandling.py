"""
Instructions
Use what you've learnt about exception handling to prevent the program from crashing.
If the user enters something that is out of range just print a default output of "Fruit pie". e.g.

"""
FRUITS = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)
