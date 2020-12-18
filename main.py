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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    window.after_cancel(timer)
    lblTitle.config(text="")
    lblTick.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_sec = 7 #WORK_MIN * 60
    short_break_sec = 2 #SHORT_BREAK_MIN * 60
    long_break_sec = 4 #LONG_BREAK_MIN * 60

    reps += 1
    print(f"reps={reps}")

    tick_count = int(reps/2)

    if reps % 2 == 1:
        lblTitle.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        lblTick.config(text="✔" * tick_count)
        lblTitle.config(text="Break", fg=RED)
        count_down(long_break_sec)
    else:
        lblTick.config(text="✔" * tick_count)
        lblTitle.config(text="Break", fg=PINK)
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    elif count == 0:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


lblTitle = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
lblTitle.grid(column=1, row=0)

btnStart = Button(text="Start", command=start_timer)
btnStart.grid(column=0, row=2)
btnReset = Button(text="Reset", command=reset)
btnReset.grid(column=2, row=2)

lblTick = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
lblTick.grid(column=1, row=3)

window.mainloop()
