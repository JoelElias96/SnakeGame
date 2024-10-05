from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreBoard import ScoreBoard

screen=Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake-Game")
screen.tracer(0)
snake=Snake()
food=Food()
score=ScoreBoard()

screen.listen()
screen.onkey(snake.head_up,"Up")
screen.onkey(snake.head_down,"Down")
screen.onkey(snake.head_left,"Left")
screen.onkey(snake.head_right,"Right")

def run():
    game_is_on=True
    while game_is_on:
        screen.update()
        time.sleep(0.05)
        snake.move()
        if food.distance(snake.head) < 15:
            food.eaten()
            snake.eat()
            score.increase_score()
        if snake.hit_wall() or snake.hit_tail():
            score.reset()
            snake.reset()
            game_is_on=False

run()



