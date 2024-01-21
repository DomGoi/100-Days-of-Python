from turtle import Turtle,Screen

tom=Turtle()
window=Screen()

def move_forward():
    tom.forward(10)

def move_backwards():
    tom.backward(10)

def turn_right():
    tom.right(10)

def forward_right():
    tom.forward(10)
    tom.right(10)

def backward_right():
    tom.backward(10)
    tom.right(10)

def turn_left():
    tom.left(10)

def forward_left():
    tom.forward(10)
    tom.left(10)

def backward_left():
    tom.backward(10)
    tom.left(10)

def clear_and_center():
    tom.reset()

window.listen()
window.onkeypress(move_forward,"w")
window.onkeypress(move_backwards,"s")
window.onkeypress(turn_right,"d")
window.onkeypress(turn_left,"a")
window.onkeypress(clear_and_center,"c")



window.exitonclick()