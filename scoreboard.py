from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.up()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.goto(-210, 250)
        self.write(arg=f"Level: {self.level}", align="center", font=("Courier", 25, "bold"))

    def next_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Courier", 40, "bold"))
