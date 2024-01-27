from turtle import Screen
from turtle_play import Tutel
from scoreboard import Score
from cars import Cars
import time
import random
#Constants
CAR_NUM=random.randint(1,100)
DELAY = 0.5
#Screen
window=Screen()
window.setup(width=600, height=600)
window.tracer(0)


score=Score()
tutel=Tutel()
cars=Cars()



window.listen()

window.onkeypress(tutel.up,"Up")
window.onkeypress(tutel.down, "Down")
window.onkeypress(tutel.right,"Right")
window.onkeypress(tutel.left, "Left")


game_on=True

while game_on:
    window.update()
    time.sleep(0.1)
    cars.car_create()
    cars.move_car()



    #turtle pass
    if tutel.ycor() >280:
        score.level_done()
        tutel.restart_position()
        cars.speed_up()



    for car in cars.all_cars:
        if tutel.distance(car) < 21:
            window.clear()
            score.game_over()
            game_on=False









window.exitonclick()
