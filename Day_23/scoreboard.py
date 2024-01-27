from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,265)
        self.score =0
        self.level=1
        self.updated_score()


    def updated_score(self):
        self.goto(280, 265)
        self.write(f'Score: {self.score}', align="right", font=("Courier", 15, "normal"))
        self.goto(-280, 265)
        self.write(f'Level: {self.level}', align="left", font=("Courier", 15, "normal"))

    def level_done(self):
        self.score +=1
        self.level +=1
        self.clear()
        self.updated_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align="center", font=("Courier", 15, "normal"))
        self.goto(0, -20)
        self.write(f'Your score: {self.score}', align="center", font=("Courier", 15, "normal"))
