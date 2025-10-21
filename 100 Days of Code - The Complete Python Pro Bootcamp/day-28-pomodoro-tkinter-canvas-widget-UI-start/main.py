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
checks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    global checks
    global timer
    window.after_cancel(timer)
    top_label.config(text="Timer", font=("Arial", 50, "normal"))
    canvas.itemconfig(timer_text,text=f"00:00")
    reps = 0
    checks = ""

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global timer
    # window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"XX")
    reps+=1
    work = WORK_MIN  *60
    short_break = SHORT_BREAK_MIN *60
    long_break =LONG_BREAK_MIN *60
    if reps % 8 == 0:
        countdown(long_break)
        top_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break)
        top_label.config(text="BREAK", fg=PINK)
    else:
        countdown(work)
        top_label.config(text="WORK", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global checks
    global timer
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec ==0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec= f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count >0:
        # print(count)
        timer = window.after(1000, countdown,count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            checks += "✔"
            bot_label.config(text=checks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
# window.minsize(width=500, height=300)
window.config(padx=100, pady=50, bg=YELLOW)


#tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text = canvas.create_text(100,130, text="00.00", fill ="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

# top label
top_label = Label(text="Timer", font=("Arial", 50, "normal"))
# top_label.config(text="New Text")
top_label.grid(column=1, row=0)
top_label.config(padx=20, pady=20, bg=YELLOW, fg=GREEN)

# bottom label

bot_label = Label(text=checks, font=("Arial", 24, "bold"))
# bot_label.config(text="New Text")
bot_label.grid(column=1, row=3)
bot_label.config(padx=20, pady=20, bg=YELLOW, fg=GREEN)

# start
button = Button(text="Start", command=start_timer)
button.grid(column=0, row=2)
button.config(highlightthickness=0)

# reset
button2 = Button(text="Reset", command=timer_reset)
button2.grid(column=2, row=2)
button2.config(highlightthickness=0)


window.mainloop()