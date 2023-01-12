from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

WEBSITE = "Website:"
USERNAME = "Email/Username:"
PASSWORD = "Password"
GENERATE = "Genegerate Password"
ADD = "Add"

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)


def generate_btn_cliked():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


def add_btn_cliked():
    website = website_input.get()
    email = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                       f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels

website_label = Label(text=WEBSITE, width=20)
website_label.grid(row=1, column=0)
username_label = Label(text=USERNAME, width=20)
username_label.grid(row=2, column=0)
password_label = Label(text=PASSWORD, width=20)
password_label.grid(row=3, column=0)

# Entries

website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2)
username_input = Entry(width=40)
username_input.grid(row=2, column=1,  columnspan=2)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons

generate_button = Button(text=GENERATE, command=generate_btn_cliked)
generate_button.grid(row=3, column=2)
add_button = Button(text=ADD, width=38, command=add_btn_cliked)
add_button.grid(row=4, column=1,  columnspan=2)

window.mainloop()
