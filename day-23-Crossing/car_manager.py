from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.set_color()
        self.set_random_position()

    def set_color(self):
        self.color(choice(COLORS))

    def set_random_position(self):
        rand_y = randint(-230, 280)
        self.goto(300, rand_y)

    def move(self, level):
        self.goto(self.xcor() - STARTING_MOVE_DISTANCE - (level * MOVE_INCREMENT),
                  self.ycor())


class CarManager:
    def __init__(self):
        self.cars = []
        self.add_car()

    def add_car(self):
        car = Car()
        self.cars.append(car)

    def initialise_cars(self):
        self.cars = []
