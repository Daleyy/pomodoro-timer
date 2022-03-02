from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    pass
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

checkmark = Label()
checkmark.config(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
checkmark.grid(column=1, row=2)

title = Label()
title.config(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
title.grid(column=1, row=0)

start = Button()
start.config(text="START", fg=GREEN, font=(FONT_NAME, 20, "bold"), command=start_timer)
start.grid(column=0, row=2)

reset = Button()
reset.config(text="RESET", fg=GREEN, font=(FONT_NAME, 20, "bold"), command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
