from turtle import  Turtle,Screen
import time

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
        self.head.setheading(RIGHT)

    def create_snake(self):
        for i in range(3):
            new_turtle = Turtle(shape='square')
            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.goto(0 - 20 * i, 0)
            self.turtles.append(new_turtle)


    def move(self):
        for turtle in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[turtle - 1].xcor()
            y = self.turtles[turtle - 1].ycor()
            self.turtles[turtle].goto(x, y)
        self.head.forward(20)

    def head_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def head_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def head_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def head_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def eat(self):
        new_turtle = Turtle(shape='square')
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(self.turtles[-1].xcor(), self.turtles[-1].ycor())
        self.turtles.append(new_turtle)

    def hit_wall(self):
        if self.head.xcor()<-300 or self.head.xcor()>300 or self.head.ycor()<-300 or self.head.ycor()>300:
            return True
        return False

    def hit_tail(self):
        for turtle in range(1, len(self.turtles) - 1):
            if self.turtles[turtle].distance(self.head) < 10:
                return True
        return False

    def disapear(self):
        for turtle in self.turtles:
            turtle.goto(1000, 0)
    def reset(self):
        self.disapear()
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]
        self.head.setheading(RIGHT)




