from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_wait = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_wait)
    title.config(text="TIMER", fg=GREEN)
    checkmark.config(text="")
    timer.itemconfig(timer_text, text="00:00")
    start.config(state="normal")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in range(1, 8, 2):
        title.config(text="WORKING", fg=GREEN)
        count_down(work_sec)

    elif reps in range(2, 7, 2):
        title.config(text="SHORT BREAK", fg=PINK)
        count_down(short_break_sec)

    elif reps == 8:
        title.config(text="LONG BREAK", fg=RED)
        count_down(long_break_sec)

    else:
        title.config(text="TIMER", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    m, s = divmod(count, 60)
    timer.itemconfig(timer_text, text=f"{m:02d}:{s:02d}")
    if count > 0:
        global timer_wait
        timer_wait = window.after(1000, count_down, count - 1)
        start.config(state="disabled")
    else:
        start_timer()
    checkmark.config(text="✔" * math.floor((reps / 2)))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
timer.create_image(100, 112, image=tomato_img)
timer_text = timer.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
timer.grid(column=1, row=1)

checkmark = Label()
checkmark.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
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
