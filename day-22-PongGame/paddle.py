from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def move_upward(self):
        y = self.ycor()
        if y < 240:
            self.goto(self.xcor(), y + 20)

    def move_downward(self):
        y = self.ycor()
        if y > -240:
            self.goto(self.xcor(), y - 20)
