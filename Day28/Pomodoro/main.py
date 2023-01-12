# Dinamic typing is changing a variable's datatype by changing it's content


from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TIMER = "Timer"
START = "Start"
RESET = "Reset"

repetitions = 0
timer = None


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="✔")


def start_timer():
    global repetitions
    repetitions += 1

    work_sec = WORK_MIN * 60
    short_work_break = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if repetitions % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif repetitions % 2 == 0:
        count_down(short_work_break)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ''
        for _ in range(math.floor(repetitions/2)):
            mark += "✔"
        check_label.config(text=mark)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text=TIMER, background=YELLOW,
                    fg=GREEN, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

start_button = Button(text=START, bg=YELLOW,
                      highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

check_label = Label(text="✔", background=YELLOW,
                    fg=GREEN, highlightthickness=0)
check_label.grid(column=1, row=3)

reset_button = Button(text=RESET, bg=YELLOW,
                      highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
