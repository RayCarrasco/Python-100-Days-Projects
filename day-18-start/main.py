import random
from turtle import Turtle, Screen
from random import randint
tim = Turtle()
tim.shape("turtle")
screen = Screen()
screen.colormode(255)
tim.width(3)
tim.speed(0)


def draw_square(side):
    for _ in range(4):
        dashes(side)
        tim.right(90)


def dashes(td):
    for i in range(td):
        if tim.pen()["pendown"]:
            tim.forward(1)
            tim.penup()
        else:
            tim.forward(1)
            tim.pendown()


def random_colour():
    return randint(1, 255), randint(1, 255), randint(1, 255)

def set_random_colour():
    tim.color(random_colour())


def draw_things(max_sides):
    for iteration in range(3, max_sides+1):
        angle = 360 / iteration
        tim.color(randint(1, 255), randint(1, 255), randint(1, 255))

        for side in range(iteration):
            tim.forward(20)
            tim.right(angle)


def random_walk_ray(iterations):
    should_change_colour = True
    set_random_colour()
    pasos = 20
    for _ in range(iterations):

        if not should_change_colour:
            set_random_colour()

        move = randint(1, 4)
        if move == 1:
            tim.forward(pasos)
            should_change_colour = True
        elif move == 2:
            tim.backward(pasos)
            should_change_colour = False
        elif move == 3:
            tim.left(90)
            tim.forward(pasos)
            should_change_colour = False
        elif move == 4:
            tim.right(90)
            tim.forward(pasos)
            should_change_colour = False


def random_walk_heading(iterations):
    heading = [0, 90, 180, 270]
    step = 20
    tim.setheading(random.choice(heading))
    for _ in range(iterations):
        set_random_colour()
        tim.setheading(random.choice(heading))
        tim.forward(step)

def spirograph():
    for i in range(1, 361, 10):
        tim.seth(i)
        set_random_colour()
        tim.circle(100)


spirograph()
screen.exitonclick()
