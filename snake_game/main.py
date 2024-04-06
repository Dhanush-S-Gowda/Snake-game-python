import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segments = []

snake = Snake()
screen.listen()
food = Food()
scoreboard = Scoreboard()



screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_status = True
while game_status:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_segment()
        
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()
        
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()







screen.exitonclick()