from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.speed(15)
        self.penup()
        self.move_speed = 0.1
        self.x_move=random.choice([10,-10])
        self.y_move= random.choice([10,-10])

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bouncey(self):
        self.y_move*=(-1)

    def bouncex(self):
        self.x_move*=(-1)
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bouncex()
