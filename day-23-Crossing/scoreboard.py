from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        message = f"Score:{self.score}"
        self.write(arg=message, font=FONT)

    def level_up(self):
        self.score += 1
        self.update_score()

    def get_score(self):
        return self.score

    def game_over(self):
        self.goto(0, 0)
        message = f"Game Over \n" \
                  f"Final Score: {self.score}"
        self.write(arg=message, font=FONT, align='center')
