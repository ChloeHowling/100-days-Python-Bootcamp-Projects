from tkinter import *

CONV = 1.609


def calc_button_clicked():
    mile = float(mile_input.get())
    km = mile * CONV
    km_value_label.config(text=str(km))


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

mile_input = Entry(width=5)
mile_input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_value_label = Label(text="0")
km_value_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=calc_button_clicked)
calc_button.grid(column=1, row=2)

window.mainloop()
