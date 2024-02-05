from tkinter import *
import pandas
import random as ra
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
tolearn={}
try:
    df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df=pandas.read_csv("./data/french_words.csv")
    word_df=df.to_dict(orient="records")
else:
    word_df = df.to_dict(orient="records")
def next_card():
    global current_card,timer
    window.after_cancel(timer)
    current_card=ra.choice(word_df)
    Word=current_card["French"]
    card_canvas.itemconfig(card_image, image=front_card)
    card_canvas.itemconfig(text_head, text="French", fill="black")
    card_canvas.itemconfig(text_body,text=Word, fill="black")

    timer=window.after(3000, func=countdown)

def countdown():
        card_canvas.itemconfig(card_image, image=back_card)
        Word_eng = current_card["English"]
        card_canvas.itemconfig(text_head, text="English", fill="white")
        card_canvas.itemconfig(text_body, text=Word_eng, fill="white")

def is_known():
    word_df.remove(current_card)
    data=pandas.DataFrame(word_df)
    data.to_csv("./data/word_to_learn.csv", index=False)


    next_card()

window=Tk()
window.title(string="Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

timer=window.after(3000, func=countdown)
#Cards
back_card = PhotoImage(file="./images/card_back.png")
front_card = PhotoImage(file="./images/card_front.png")
card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image=card_canvas.create_image(400, 263, image=front_card, anchor="center")
card_canvas.grid(column=0, row=0, columnspan=2)


text_head=card_canvas.create_text(400,150, font=("Arial", 40, "italic"))
text_body=card_canvas.create_text(400,263, font=("Arial", 60, "bold"))


#Buttons

wrong_img = PhotoImage(file="./images/wrong.png.")
button_x = Button(image=wrong_img, highlightthickness=0, fg=BACKGROUND_COLOR, command=next_card)
button_x.grid(column=0, row=1)

right_img = PhotoImage(file="./images/right.png")
button_v = Button(image=right_img, highlightthickness=0, fg=BACKGROUND_COLOR, command=is_known)
button_v.grid(column=1, row=1)

next_card()


window.mainloop()