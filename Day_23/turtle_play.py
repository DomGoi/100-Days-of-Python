from turtle import Turtle

START_POS=(0,-280)
UP = 90
DOWN = 270
LEFT= 180
RIGHT=0
DIS=15

class Tutel(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.shapesize(1)
        self.seth(UP)
        self.goto(START_POS)

    def up(self):
        if self.ycor() < 280:
            self.seth(UP)
            self.forward(DIS)

    def down(self):
        if self.ycor() > -280:
            self.backward(DIS)

    def left(self):
        if self.xcor() > -280:
            self.seth(LEFT)
            self.forward(DIS)

    def right(self):
        if self.xcor() < 280:
            self.seth(RIGHT)
            self.forward(DIS)

    def restart_position(self):
        self.goto(START_POS)
