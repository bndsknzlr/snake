from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)