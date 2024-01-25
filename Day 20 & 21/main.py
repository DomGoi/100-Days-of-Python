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

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_on=False

    for seg in snake.snakes[1:]:
        if snake.head.distance(seg) < 10:
            score.game_over()
            game_on = False

window.exitonclick()