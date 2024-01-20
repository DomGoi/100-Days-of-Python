import colorgram
from turtle import Turtle, Screen
import random

tom=Turtle()
colors=colorgram.extract('image.jpeg',255)

RGB_tuples=[]

for color in colors:
   RGB_tuples.append((color.rgb.r, color.rgb.g, color.rgb.b))

window=Screen()
window.colormode(255)
window.screensize(300,300)



def line_horizontal():
    for i in range(10):
        random_color = random.choice(RGB_tuples)
        tom.dot(20, random_color)
        tom.forward(50)
def change_line():
    tom.penup()
    tom.setposition(-225, tom.ycor()+50)

tom.speed(10)
tom.penup()
tom.setposition(-225,-220)
i=0
while i < 10:
    line_horizontal()
    change_line()
    i +=1






