from turtle import Turtle
import random

COLOR_LIST=["navy","midnight blue","lawn green","lime green", "saddle brown","dark red","indigo",
            "orange","olive drab", "gold","green","medium violet red","maroon","dark orange","dodger blue",
            "hot pink", "dark goldenrod","slate blue","dark slate gray","dim gray","red","crimson","yellow green"]
SPEED_LIST=[1,2,3,4,5,6,7,8,9,10,0]

START_DIS=5
MOVE_INCR=10
X_COR_START=300


class Cars():
    def __init__(self):
        self.all_cars=[]
        self.k = 0

    def car_create(self):
        chance=random.randint(1,6)
        if chance == 1:
            new_car=Turtle(shape="square")
            new_car.color(random.choice(COLOR_LIST))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(X_COR_START,random.randint(-250,250))
            new_car.speed(SPEED_LIST[self.k])
            self.all_cars.append(new_car)
        else:
            pass


    def move_car(self):
        for car in self.all_cars:
            car.backward(START_DIS)

    def speed_up(self):
        self.k += 1









