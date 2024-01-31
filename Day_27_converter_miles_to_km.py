from tkinter import *

window= Tk()
window.title("Miles to Km converter")
window.minsize()
window.config(padx=20, pady=20)

#Test variables
miles_label=Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

km_label=Label(text="Kilometers", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

km_num=Label(text="0", font=("Arial", 12))
km_num.grid(column=1, row=1)

equal_label=Label(text="is equal to", font=("Arial", 12))
equal_label.grid(column=0, row=1)

#Entry

miles_input=Entry(width=10, font=("Arial",12))
miles_input.insert(0, "Enter miles")
miles_input.grid(column=1, row=0)

#Button
def button_clicked():
     km_num.config(text=round(int(miles_input.get())*1.60934, 2), font=("Arial", 12))
button=Button(text="Convert", width=10, command=button_clicked)
button.grid(column= 1, row=2)

window.mainloop()