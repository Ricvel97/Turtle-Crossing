from turtle import Turtle
import random

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.color_list = ["yellow", "gray", "white", "green", "blue", "red", "purple", "pink", "orange"]
        self.cars = []
        self.move_distance = 10
        self.create_car()

    def create_car(self):
        random_y = random.randint(-250, 260)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(self.color_list))
        self.goto(300, random_y)

    def move(self):
        self.backward(10)