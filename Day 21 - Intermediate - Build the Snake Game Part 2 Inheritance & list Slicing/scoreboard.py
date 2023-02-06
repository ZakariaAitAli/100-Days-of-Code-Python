from turtle import Turtle
ALIGNEMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGNEMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align=ALIGNEMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
