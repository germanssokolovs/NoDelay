from tkinter import *



registered_name = None
registered_email = None
registered_password = None

# ---------- Window switching function ----------





def show_register():
    login_frame.pack_forget()
    register_frame.pack(pady=20)

def show_login():
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    register_frame.pack_forget()
    login_frame.pack()

def submit_registration():
    global is_registered, registered_name, registered_email, registered_password
    name = name_entry.get()
    email = reg_email_entry.get()
    password = reg_password_entry.get()
    confirm = confirm_entry.get()

    if not name or not email or not password:
        print("All fields required!")
        is_registered = False
    elif password != confirm:
        print("Passwords do not match.")
        is_registered = False
    else:
        registered_name = name
        registered_email = email
        registered_password = password
        is_registered = True
        print(f"Registered: {registered_name}, {registered_email}")
        show_login()



def try_sign_in():
    email = email_entry.get()
    password = password_entry.get()

    print(f"Введено: email={email}, password={password}")
    print(f"Ожидается: email={registered_email}, password={registered_password}")

    if not is_registered:
        print("Please register first!")
        return

    if email == registered_email and password == registered_password:
        show_daily_goals()
    else:
        print("Invalid email or password!")







# ---------- Main window ----------
w = Tk()
is_registered = False  

w.title("NoDelay")
w.geometry("360x600")
w.resizable(False, False)

# ---------- Entry frame ----------
login_frame = Frame(w, padx=10, pady=10)

Label(login_frame, text="Let’s beat procrastination together!", font=("Helvetica", 10, "italic")).pack(pady=(10, 5))
Label(login_frame, text="Dear User, welcome in..", font=("Helvetica", 10, "italic")).pack()
Label(login_frame, text="NoDelay!", font=("Helvetica", 20, "bold")).pack()
Label(login_frame, text="Get started right now!", font=("Helvetica", 10, "italic")).pack(pady=(0, 20))

form = Frame(login_frame, bd=2, relief="groove", padx=10, pady=10)
form.pack(pady=10)

Label(form, text="Email").pack(anchor="w")
email_entry = Entry(form, width=30)
#email_entry.insert(0, "Value")
email_entry.pack(pady=5)

Label(form, text="Password").pack(anchor="w")
password_entry = Entry(form, show="*", width=30)
#password_entry.insert(0, "Value")
password_entry.pack(pady=5)

Button(form, text="Sign In", bg="black", fg="white", width=30, command=try_sign_in).pack(pady=10)


Button(form, text="Registration", relief="flat", fg="blue", cursor="hand2", command=show_register).pack()


desc_text = (
    "\nNoDelay helps you beat procrastination and stay productive. Create your task list, "
    "start a focus session, and track your progress. With a simple and motivating design, "
    "NoDelay keeps you on track to achieve your goals—one step at a time."
)
Label(login_frame, text=desc_text, wraplength=320, font=("Helvetica", 9), justify="left").pack(pady=(20, 0))

login_frame.pack()

# ---------- Daily Goals Frame ----------


goals_frame = Frame(w)

def show_daily_goals():
    login_frame.pack_forget()
    goals_frame.pack(pady=20)

Label(goals_frame, text="⚠️", font=("Helvetica", 24)).pack()
Label(goals_frame, text="Whats our plan\nfor today?", font=("Helvetica", 16, "bold")).pack(pady=10)

goals_card = Frame(goals_frame, bd=1, relief="solid", padx=10, pady=10)
goals_card.pack(pady=20)

Label(goals_card, text="Daily Goals", font=("Helvetica", 12, "bold")).pack(anchor="w", pady=(0, 10))

# ---------- Registration Frame ----------
register_frame = Frame(w, padx=10, pady=10)

Label(register_frame, text="Create a new account", font=("Helvetica", 16, "bold")).pack(pady=(10, 20))

Label(register_frame, text="Full Name").pack(anchor="w")
name_entry = Entry(register_frame, width=30)
name_entry.pack(pady=5)

Label(register_frame, text="Email").pack(anchor="w")
reg_email_entry = Entry(register_frame, width=30)
reg_email_entry.pack(pady=5)

Label(register_frame, text="Password").pack(anchor="w")
reg_password_entry = Entry(register_frame, show="*", width=30)
reg_password_entry.pack(pady=5)

Label(register_frame, text="Confirm Password").pack(anchor="w")
confirm_entry = Entry(register_frame, show="*", width=30)
confirm_entry.pack(pady=5)

Button(register_frame, text="Register", bg="green", fg="white", width=30, command=lambda: submit_registration()).pack(pady=10)
Button(register_frame, text="← Back to login", relief="flat", fg="blue", cursor="hand2", command=lambda: show_login()).pack()

#----------------------------------------






# Сto-do list
tasks = [
    ("Read 10 pages", "from my current book"),
    ("Study for 30 minutes", "finish biology assignment"),
    ("Clean my desk", "keep my space distraction-free"),
    ("Make lunch", "prepare something healthy"),
    ("Go to gym", ""),
]

checkbox_vars = []

for task, desc in tasks:
    frame = Frame(goals_card)
    frame.pack(anchor="w", fill="x", pady=3)

    var = IntVar()
    checkbox_vars.append(var)

    def on_check(v=var, t=task):
        if v.get() == 1:
            Button(frame, text="Start Focus Session", command=lambda: open_focus_session(t)).pack(side="bottom", pady=5)

    Checkbutton(frame, variable=var, command=on_check).pack(side="right")
    Label(frame, text=f"{task}", font=("Helvetica", 10, "bold")).pack(anchor="w")
    if desc:
        Label(frame, text=desc, font=("Helvetica", 8, "italic"), fg="gray").pack(anchor="w")


Label(goals_frame, text="\nRemember!", font=("Helvetica", 10, "bold", "italic")).pack()
Label(goals_frame, text='"Small steps lead to big results. Stay focused and make progress!"', font=("Helvetica", 9, "italic")).pack()

def open_focus_session(task_name):
    focus_win = Toplevel(w)
    focus_win.title("Focus Session")
    focus_win.geometry("300x350")
    focus_win.resizable(False, False)

    Label(focus_win, text=task_name, font=("Helvetica", 14, "bold"), wraplength=280).pack(pady=10)

    canvas = Canvas(focus_win, width=200, height=200)
    canvas.pack()

    arc = canvas.create_arc(10, 10, 190, 190, start=90, extent=0, style="arc", width=10, outline="green")
    timer_text = canvas.create_text(100, 100, text="25:00", font=("Helvetica", 16, "bold"))

    duration = 25 * 60
    interval = 1000  # 1 second
    progress = [0]   # list for mutability

    def update_focus_timer():
        nonlocal duration
        minutes = duration // 60
        seconds = duration % 60
        canvas.itemconfig(timer_text, text=f"{minutes:02}:{seconds:02}")

        percent = (progress[0] / (25 * 60)) * 360
        canvas.itemconfig(arc, extent=-percent)

        if duration > 0:
            duration -= 1
            progress[0] += 1
            focus_win.after(interval, update_focus_timer)
        else:
            canvas.itemconfig(timer_text, text="Done!")
            canvas.itemconfig(arc, outline="red")

    update_focus_timer()


# ----------start the main event loop of the GUI  ----------
w.mainloop()
