from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.initial_position()
        self.setheading(90)
        print(self.xcor())

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def initial_position(self):
        self.goto(STARTING_POSITION)
