from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Times New Roman"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = ""
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #


def end_the_timer():
    window.after_cancel(timer)
    label.config(text="Timer")

    global checkmarks
    checkmarks = ""

    canvas.itemconfig(timer_text, text="00:00")

    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_the_timer(count):
    minutes = count // 60
    seconds = count % 60

    # Python allows dynamic in storing variables, i.e. we can store an int value in a previously defined str variable.
    if seconds < 10:
        seconds = f"0{seconds}"
    if seconds == 0:
        seconds = "00"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, start_the_timer, count - 1)  # It'll work even tho it is stored in a variable.
    else:
        global reps
        global checkmarks
        if reps % 2 != 0:
            checkmarks += "✔"
            checkbox_label.config(text=checkmarks)
        count_down()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down():
    global reps
    reps += 1
    if reps % 8 == 0:
        global checkmarks
        checkmarks = ""
        start_the_timer(LONG_BREAK_MIN * 60)
        label.config(text='BREAK', fg=RED)
        window.state('zoomed')
        # window.attributes('-topmost', True)
        reps = 0

    elif reps % 2 == 0:
        start_the_timer(SHORT_BREAK_MIN * 60)
        label.config(text='Break', fg=PINK)
        window.state('zoomed')
        # window.attributes('-topmost', True)

    else:
        start_the_timer(WORK_MIN * 60)
        label.config(text="Work", fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.resizable(width=False, height=False)
window.maxsize(500, 450)

# Adding some padding to the window to properly accommodate the tomato image.
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
label.grid(row=0, column=1)

# Adding a canvas to the window (where we can stack timer on the tomato image)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

start_button = Button(text="Start", width=4, bg="white", command=count_down)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", width=4, bg="white", command=end_the_timer)
reset_button.grid(row=2, column=2)

checkbox_label = Label(font=(FONT_NAME, 15), fg=GREEN, bg=YELLOW)
checkbox_label.grid(row=3, column=1)

window.mainloop()

# GUI is an event driven program. It is always listening for something to happen because of the mainloop.
# Therefore, if a while loop is initialized in a program, it will not even be executed. Luckily, Tkinter has a solution.
