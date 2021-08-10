from snake import Snake
from turtle import Screen
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('No importa cuando te esfuerces, perecerás')

snake = Snake()
food = Food()
score_board = ScoreBoard()
score_board.refresh_message()

screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.add_point()
        snake.extend()

    # Detect collision with wall
    if abs(snake.head.xcor()) >= 290 or abs(snake.head.ycor()) >= 290:
        print("Wall")
        game_is_on = False
        score_board.game_over()

    # Detect collision with tail
    for block_num in snake.snake[1:]:
        if snake.head.distance(block_num) < 10:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
