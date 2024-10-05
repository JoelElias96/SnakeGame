import random as rd
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('Blue')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        x=rd.randint(-250,250)
        y=rd.randint(-250,250)
        self.goto(x,y)

    def eaten(self):
        x = rd.randint(-250, 250)
        y = rd.randint(-250, 250)
        self.goto(x, y)
