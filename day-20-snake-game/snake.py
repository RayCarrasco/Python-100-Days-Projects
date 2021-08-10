from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):

        self.snake = []
        self.create_snake()
        self.snake[0].setheading(0)
        self.head = self.snake[0]
        self.headed = 0

    def create_snake(self):
        for i in range(3):
            self.add_segment(position=(0-20*i, 0))

    def add_segment(self, position):
        block = Turtle(shape='square')
        block.color('green')
        block.penup()
        block.goto(position)
        self.snake.append(block)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):

        for block_num in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[block_num-1].xcor()
            new_y = self.snake[block_num - 1].ycor()
            self.snake[block_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.headed = self.head.heading()

    def up(self):
        if self.headed != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.headed != UP:
            self.snake[0].setheading(DOWN)

    def left(self):
        if self.headed != RIGHT:
            self.snake[0].setheading(LEFT)

    def right(self):
        if self.headed != LEFT:
            self.snake[0].setheading(RIGHT)
