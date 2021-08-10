from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 180)
        self.score = [0, 0]
        self.update_score()

    def r_point(self):
        self.score[1] += 1

    def l_point(self):
        self.score[0] += 1

    def update_score(self):
        self.clear()
        message = f"{self.score[0]} | {self.score[1]}"
        self.write(message, align="center", font=("Courier", 80, "normal"))

    def game_over(self):
        if self.score[0] > self.score[1]:
            winner = "Left"
        else:
            winner = "Right"
        message = f"Game Over\n{winner} Player Wins"
        self.goto(0, 0)
        self.write(message, align="center", font=("Courier", 40, "normal"))




