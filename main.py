from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


# TODO : 3. create food
# TODO : 4. detect collision with food
# TODO : 5. create scoreboard
# TODO : 6. detect collision with wall
# TODO : 7. detect collision with tail

screen.exitonclick()
