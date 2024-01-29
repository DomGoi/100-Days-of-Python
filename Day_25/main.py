import turtle
import pandas as pd

window=turtle.Screen()
window.title("U.S. Game")
image="blank_states_img.gif"
window.addshape(image)
turtle.shape(image)



states_data=pd.read_csv("50_states.csv")

def display_state_name(state_name, x, y):
    state_name_turtle = turtle.Turtle()
    state_name_turtle.hideturtle()
    state_name_turtle.penup()
    state_name_turtle.goto(x, y)
    state_name_turtle.write(state_name, align="center", font=("Arial", 10, "normal"))

game_on=True
guessed_states=0
right_state=[]


while game_on:
    answer = window.textinput(title=f"Guess the state name. {guessed_states}/50",
                              prompt="What is the name of the next state?").title().strip()

    if answer is None:
        break

    if answer == "Exit":
        states_to_learn = []
        for state in states_data["state"]:
            if state not in right_state:
                states_to_learn.append(state)
        states_to_learn_csv=pd.DataFrame(states_to_learn, columns=["unguessed_names"])
        states_to_learn_csv.to_csv("States_to_learn.csv")
        game_on=False


    if answer in states_data["state"].values:
        state_coordinates = states_data[states_data["state"] == answer][["x", "y"]].values[0]
        x = state_coordinates[0]
        y = state_coordinates[1]
        display_state_name(answer, x, y)
        guessed_states += 1
        right_state.append(answer)

    if guessed_states == 50:
        game_done = turtle.Turtle()
        game_done.hideturtle()
        game_done.penup()
        game_done.goto(0, 0)
        game_done.write(f'You have won! Congratulations!', align="center", font=("Arial", 20, "normal"))
        game_on = False

window.exitonclick()

window.exitonclick()


