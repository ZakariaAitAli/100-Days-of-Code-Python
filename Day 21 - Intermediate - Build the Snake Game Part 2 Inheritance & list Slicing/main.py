from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #     detect collision with food
    if snake.segment[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    #     detect collision with the wall
    if snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -280 or snake.segment[0].ycor() > 285 or snake.segment[0].ycor() < -285:
        game_is_on = False
        score.game_over()

    #     detect collision with the tail
    for seg in snake.segment[1:]:
        if snake.segment[0].distance(seg) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
