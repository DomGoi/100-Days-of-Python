import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score

SET_POS_L=(-350,0)
SET_POS_R=(350,0)


window=Screen()
window.setup(width=800,height=600)
window.bgcolor("black")
window.title("Pong")
window.tracer(0)


paddle_l=Paddle(SET_POS_L)
paddle_r=Paddle(SET_POS_R)
ball=Ball()
score=Score()

window.listen()
window.onkeypress(paddle_r.up, "Up")
window.onkeypress(paddle_r.down, "Down")
window.onkeypress(paddle_l.up, "w")
window.onkeypress(paddle_l.down, "s")

game_on=True

while game_on:
    window.update()
    time.sleep(ball.move_speed)

    ball.move()
    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.bouncey()

    elif ball.xcor() > 390:
        ball.reset_position()
        score.score_l()

    elif ball.xcor() <-390:
        ball.reset_position()
        score.score_r()

    if (ball.distance(paddle_r) < 50 and ball.xcor() > 320) or (ball.distance(paddle_l) < 50 and ball.xcor() < -320):
        ball.bouncex()





























window.exitonclick()