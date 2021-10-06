from tkinter import *


def button_clicked():
    print("I Got Clicked")
    text = input.get()
    my_label.config(text=text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# Button
button_1 = Button(text="Don't Click Me", command=button_clicked)
button_1.grid(column=2, row=0)

button_2 = Button(text="Click Me", command=button_clicked)
button_2.grid(column=1, row=1)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)

# Text Entry, Spinbox, Scale, Checkbox, Radio buttons, Listbox
# Refer ro tkinter_entries.py

# pack(), place(), grid()
# grid and pack cannot be used in the same window

window.mainloop()
