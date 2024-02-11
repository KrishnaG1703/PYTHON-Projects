from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
Score = scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.moves()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.addsnake()
        Score.addpoints()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        Score.gameover()

    for segments in snake.total[1:]:
        if snake.head.distance(segments) < 10:
            game_on = False
            Score.gameover()






























screen.exitonclick()
