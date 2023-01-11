from tkinter import *

MILES = "Miles"
KM = "Km"
IS_EQUAL = "is equal to"
CALCULATE = "Calculate"


window = Tk()
window.title("Mile to km converter")
window.config(padx=10, pady=20)


def button_clicked():
    print("Clicked!")
    km = round(int(my_input.get()) * 1.609344)
    print(km)
    calc_label.config(text=km)


my_input = Entry(width=10)
my_input.grid(column=1, row=0)

miles_label = Label(text=MILES)
miles_label.grid(column=2, row=0)

is_equal_label = Label(text=IS_EQUAL)
is_equal_label.grid(column=0, row=1)

calc_label = Label(text=0)
calc_label.grid(column=1, row=1)

km_label = Label(text=KM)
km_label.grid(column=2, row=1)


button_label = Button(text=CALCULATE, command=button_clicked)
button_label.grid(column=1, row=2)


window.mainloop()
