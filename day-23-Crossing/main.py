from time import sleep
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.onkeypress(player.move, 'Up')

game_is_on = True
counter = 0
while game_is_on:
    counter += 1

    if counter == 6:
        car_manager.add_car()
        counter = 0

    for car in car_manager.cars:
        car.move(scoreboard.get_score())

    # finished
    if player.ycor() >= FINISH_LINE_Y:
        player.initial_position()
        scoreboard.level_up()

    # collision detection
    for car in car_manager.cars:
        distance = player.distance(car)
        if distance <= 25:
            scoreboard.game_over()
            game_is_on = False

    sleep(0.1)
    screen.update()

screen.exitonclick()
