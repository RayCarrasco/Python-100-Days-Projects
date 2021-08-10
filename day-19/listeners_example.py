from turtle import Turtle, Screen

tim = Turtle()
tim.speed(0)
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def rotate_rigth():
    tim.seth(tim.heading() + 10)


def rotate_left():
    tim.seth(tim.heading() - 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=rotate_rigth)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
