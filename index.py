import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.turn_up,"Up")
screen.onkey(snake.turn_down,"Down")
screen.onkey(snake.turn_right,"Right")
screen.onkey(snake.turn_left,"Left")

game_over = False
speed = 0.2  # Initial speed

while not game_over:
    screen.update()
    time.sleep(speed)  # Use the dynamic speed variable
    snake.move_foreword()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend()

        # Increase speed (make the game faster)
        if speed > 0.05:  # Limit the maximum speed to avoid the game becoming too fast
            speed -= 0.01

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        game_over = True
        scoreboard.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_over = True
            scoreboard.game_over()

screen.exitonclick()
