import time
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = self.get_high()
        self.score = 0
        self.penup()
        self.goto(260, 260)
        self.color('white')
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score:{self.score} High score:{self.high_score}", align="right", move=True, font=("Courie", 25, "normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.update_high()
        self.score = 0
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", move=True, font=("Courie", 25, "normal"))
        time.sleep(3)
        self.clear()
        self.goto(260, 260)
        self.update_score()

    def get_high(self):
        with open('highscore.txt', 'r') as file:
            return int(file.read())

    def update_high(self):
        with open('highscore.txt', 'w') as file:
            file.write(f"{self.score}")
            self.high_score=self.score