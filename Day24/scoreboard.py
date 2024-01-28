from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial", 24, "normal")



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt", mode="r") as data:
            self.highscore=int(data.read())
        self.penup()
        self.goto(0, 260)
        self.color("White")
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
         self.score += 1
         self.update()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore=self.score

            with open("data.txt", mode="w") as new_score:
                new_score.write(f'{self.highscore}')

        self.score =0
        self.update()



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

