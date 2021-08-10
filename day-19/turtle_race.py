from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor('black')
user_bet = screen.textinput(title='Turtle  race', prompt='Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']

turtles = {}
for i in range(7):
    name = f"t{i}"
    turtles[name] = Turtle(shape='turtle')
    color = choice(colors)
    colors.remove(color)
    turtles[name].color(color)
    turtles[name].penup()
    turtles[name].goto(x=-240, y=(i * 60) - 180)

is_race_on = False
if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in turtles:
        random_distance = randint(0, 10)
        turtles[turtle].forward(random_distance)
        if turtles[turtle].xcor() >= 230:
            winner = turtles[turtle]
            is_race_on = False
            if turtles[turtle].pencolor() == user_bet:
                print("You win :)")
            else:
                print("You lost :(")

print(f'The winner is {winner.pencolor()}')

screen.exitonclick()
