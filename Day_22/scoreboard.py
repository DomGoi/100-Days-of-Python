from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_r_value = 0
        self.score_l_value = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(str(self.score_l_value), align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(str(self.score_r_value), align="center", font=("Courier", 80, "normal"))

    def score_r(self):
        self.score_r_value +=1
        self.clear()
        self.update_score()

    def score_l(self):
        self.score_l_value += 1
        self.clear()
        self.update_score()