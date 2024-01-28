from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Score

import time
window=Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake")
window.tracer(0)

snake=Snake()
food=Food()
score=Score()

window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down,"Down")
window.onkey(snake.right,"Right")
window.onkey(snake.left,"Left")

game_on=True

while game_on:
    window.update()
    time.sleep(0.1)
    snake.snake_move()



    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset_score()
        snake.snake_reset()

    for seg in snake.snakes[1:]:
        if snake.head.distance(seg) < 10:
            score.reset_score()
            snake.snake_reset()

window.exitonclick()