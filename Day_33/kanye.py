from tkinter import *
import requests

def get_quote():
    global quote
    response=requests.get(url="https://api.kanye.rest")
    response.raise_for_status()

    data=response.json()
    quote=data["quote"]
    canvas.itemconfig(quote_text, text=quote)

window=Tk()
window.title(string="Kanye Great Quotes")
window.config(padx=50,pady=50)

image=PhotoImage(file="./background.png")
canvas=Canvas(width=300, height=415,highlightthickness=0)
canvas.create_image(150,208, image=image)
quote_text=canvas.create_text(150,208,text="Press button to get the first quote", width=250, font=("Arial", 30, "bold"), fill='white')
canvas.grid(column=0,row=0)


kanye=PhotoImage(file="./kanye.png")
button=Button(image=kanye, highlightthickness=0, command=get_quote)
button.grid(column=0,row=1)
window.mainloop()