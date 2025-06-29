from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.y_cor = -280
        self.create_player()
        self.move_distance = 10

    def create_player(self):
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(0, self.y_cor)
        self.setheading(90)

    def move(self):
        self.y_cor += self.move_distance
        self.goto(0, self.y_cor)

    def reset(self):
        self.y_cor = -280
        self.goto(0, self.y_cor)
