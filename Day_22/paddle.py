from turtle import Turtle

UP = 90
DOWN = 270
DIST=10
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(position)


    def up(self):
        new_y=self.ycor()+20
        if new_y < 249:
            self.goto(self.xcor(), new_y)


    def down(self):
        new_y = self.ycor() - 20
        if new_y > -249:
            self.goto(self.xcor(), new_y)







