from tkinter import *
from tkinter import messagebox as mb
import random

import pyperclip
from pyperclip import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    char_list=[random.choice(LETTERS) for _ in range(nr_letters)]

    sym_list=[random.choice(SYMBOLS) for _ in range(nr_symbols)]

    num_list=[random.choice(NUMBERS) for _ in range(nr_numbers)]


    password_list = char_list+sym_list+num_list

    random.shuffle(password_list)

    password ="".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,f'{password}')
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
#note=open("note03_02_24.txt", mode='x')
def add_button():
    website_input = website_entry.get()
    password_input = password_entry.get()
    email_input = email_entry.get()
    input_string=f'{website_input} | {email_input} | {password_input} \n'
    if website_input == "" or password_input == "" or email_input == "":
        mb.showinfo(title="Input not provided", message="Please enter all information's")
    else:
        is_ok= mb.askokcancel(title="Confirmation", message=f'Are you sure about these information? \n Website:{website_input} \n Email/Username:{email_input} \n Password:{password_input}')
        if is_ok:
            with open("note03_02_24.txt", mode="a") as file_text:
                file_text.write(input_string)
            cleaning_entries()


def cleaning_entries():
    website_entry.delete(0,END)
    email_entry.delete(0,END)
    password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password manager")
window.config(pady=50, padx=50)

#Image
canvas=Canvas(width=200, height=200, highlightthickness=0)
IMAGE=PhotoImage(file="./logo.png")
canvas.create_image(100,100,image=IMAGE)
canvas.grid(column=1,row=0)

#Website
website=Label(text="Website")
website.grid(column=0,row=1)

website_entry=Entry(width=45)

website_entry.focus()
website_entry.grid(column=1,row=1, columnspan=2)

#Email
email=Label(text="Email/Username")
email.grid(column=0,row=2)

email_entry=Entry(width=45)
email_entry.grid(column=1,row=2, columnspan=2)


#Password
password=Label(text="Password")
password.grid(column=0,row=3)

password_entry=Entry(width=25)
password_entry.grid(column=1,row=3)

password_button=Button(text="Generate Password", width=20, command=password_generator)
password_button.grid(column=2, row=3)

#Add button
add_button=Button(width=45, text="Add", command=add_button)
add_button.grid(column=1, row=4, columnspan=2)













window.mainloop()