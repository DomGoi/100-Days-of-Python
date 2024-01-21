import turtle
from turtle import Turtle,Screen
import random
race=False
window=Screen()
window.setup(width=500, height=400)
user_bet=window.textinput(title="Make your bet!", prompt= "Input color of the turtle you think will win.")
color_list=["red","orange","yellow","green","blue","purple"]
name_list=[]




for i, color in enumerate(color_list):
    turtle_i = Turtle(shape="turtle")
    turtle_i.color(color)
    turtle_i.penup()
    turtle_i.goto(x=-230, y=100 - i * 40)  # Adjust the y-coordinate based on turtle index
    name_list.append(turtle_i)

if user_bet:
    race=True

while race:
    for turtle in name_list:
        if turtle.xcor()>230:
            race = False
            if turtle.pencolor() == user_bet:
                print(f"You have won, the {turtle.pencolor()} won.")

            else:
                print(f"You lost. The {turtle.pencolor()} won.")

        random_dis=(random.randint(0,10))
        turtle.forward(random_dis)








window.exitonclick()

