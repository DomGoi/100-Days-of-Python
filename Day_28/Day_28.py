import math
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
TICK="✔"
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_button():
    window.after_cancel(timer)
    up_label.config(text="Timer", fg=GREEN, bg=YELLOW)
    tick_label.config(font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(time_text, text=f'00:00')
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps +=1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        up_label.config(text="Long break", fg=PINK)
        tick_label.config(text)
    elif reps % 2 == 1:
        count_down(WORK_MIN*60)
        up_label.config(text="Work Time", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        up_label.config(text="Short break", fg=GREEN)
    elif reps % 8 > 0:
        start_timer()



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(time):
    min = math.floor(time / 60)
    sec = time % 60
    if sec == 0:
        sec = "00"
    elif sec <10:
        sec=f'0{sec}'

    canvas.itemconfig(time_text, text=f'{min}:{sec}')
    if time >0:
        global timer
        timer=(window.after(1000, count_down, time-1))
    else:
        start_timer()
        mark=""
        for i in range(math.floor(reps/2)):
            mark +=TICK
        tick_label.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro Method")
window.config(pady=50,padx=100, bg=YELLOW)
canvas=Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
pomidor=PhotoImage(file="./tomato.png")
canvas.create_image(105,115, image=pomidor)
time_text=canvas.create_text(105,130, text=f"00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1,row=1)

# ---------------------------- LABELS ------------------------------- #

up_label=Label(window, text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
up_label.grid(column=1,row=0)


tick_label=Label(window, font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
tick_label.grid(column=1,row=3)


# ---------------------------- BUTTONS ------------------------------- #

button_reset=Button(width=10, text="Reset", font=(FONT_NAME, 12, "bold"), fg=RED, command=reset_button)
button_reset.grid(column=2, row=2)

button_start=Button(width=10, text="Start", font=(FONT_NAME, 12, "bold"), fg=RED, command=start_timer)
button_start.grid(column=0, row=2)

window.mainloop()