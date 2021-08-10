from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
from time import sleep


screen = Screen()
screen.tracer(0)
screen.listen()
screen.title('Pong')
screen.setup(width=800, height=600)
screen.bgcolor('black')

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score = ScoreBoard()

screen.onkeypress(r_paddle.move_upward, 'Up')
screen.onkeypress(r_paddle.move_downward, 'Down')

screen.onkeypress(l_paddle.move_upward, 'w')
screen.onkeypress(l_paddle.move_downward, 's')

game_on = True

while game_on:
    # detect ball with wall collision
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # detect ball with paddle collision
    if ball.distance(r_paddle) <= 30 and ball.xcor() > 320\
            or ball.distance(l_paddle) <= 30 and ball.xcor() < -320:
        ball.bounce_x()

    # Annotation
    if ball.xcor() > 360:
        score.l_point()
        score.update_score()
        ball.ball_reset()

    if ball.xcor() < -360:
        score.r_point()
        score.update_score()
        ball.ball_reset()

    if score.score[0] > 4 or score.score[1] > 4:
        break

    ball.move()
    sleep(ball.move_speed)
    print(ball.move_speed)
    screen.update()

screen.clear()
screen.bgcolor('black')
score.game_over()
screen.update()

screen.exitonclick()
