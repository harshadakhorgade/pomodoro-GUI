import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text ="00:00")
    my_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    # Convert minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        my_label.config(text="Long Break", fg=RED)
        window.attributes("-topmost", True)  # Bring window to the front
        count_down(long_break_sec)
    elif reps % 2 == 0:
        my_label.config(text="Short Break", fg=PINK)
        window.attributes("-topmost", True)  # Bring window to the front
        count_down(short_break_sec)
    else:
        my_label.config(text="Work", fg=GREEN)
        window.attributes("-topmost", False)  # Disable always-on-top during work
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min =math.floor(count/60)     #conveted in to min and taking the min part only if (4.35 then take 4.00)
    count_sec =count % 60      #this will take only sec part the reminder


# here we use dynamic typing which change the data type int to string
    if count_sec < 10:
        count_sec =f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer =window.after(1000,count_down,count-1)

    else:
        start_timer()
        marks =""
        work_session =math.floor(reps/2)
        for _ in range(work_session):
            marks +="✔"
            check_mark.config(text =marks )

# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Pomodoro")
window.config(padx= 100,pady=50,bg=YELLOW)



# canvas widgets
canvas =Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100,112,image =tomato_img)
timer_text = canvas.create_text(100,130,text ="00:00",fill ="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column =1,row=1)



my_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,40),bg=YELLOW)
my_label.grid(column=1, row=0)

start_button = Button(text ="Start",command= start_timer,highlightthickness=0 )
start_button.grid(column=0, row=2)

reset_button= Button(text ="Reset" ,command=reset_timer,highlightthickness=0)
reset_button.grid(column=2, row=2)

check_mark =Label(fg=GREEN,bg=YELLOW)
check_mark.grid(column=1, row=3)

#GUI is event driven
window.mainloop()