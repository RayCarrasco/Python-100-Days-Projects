# from turtle import Turtle, Screen
#
# timmi = Turtle()
# my_screen = Screen()
#
# timmi.shape("turtle")
# timmi.color("DarkRed")
# timmi.forward(100)
#
# print(timmi)
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'


print(table)

