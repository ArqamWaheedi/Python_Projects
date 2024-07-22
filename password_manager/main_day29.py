from tkinter import *   # only imports all the classes and constants
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from password_generator import password_generator
password = password_generator()
pyperclip.copy(f'{password}')


def generate():
    Password_input.insert(0, f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    global password
    websites = website_input.get()
    email = Email_input.get()
    lock = Password_input.get()
    if len(websites) == 0 or len(lock) == 0:
        messagebox.showinfo(title="Oops", message="PLease make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=websites, message=f"These are the details entered: \nEmail:{email}"
                                                               f"\nPassword: {lock} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as new_file:
                new_file.write(f"{website_input.get()} | {Email_input.get()} | {Password_input.get()}\n")
                messagebox.showinfo(message='Password Saved')
                website_input.delete(0, END)
                Password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


windows = Tk()
windows.title("Password Manager")
windows.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)
website_input = Entry(width=32)
website_input.focus()
website_input.grid(row=1, column=1)

Email = Label(text="Email/Username:")
Email.grid(row=2, column=0)
Email_input = Entry(width=51)
Email_input.insert(END, "arqam.waheeedi@gmail.com")
Email_input.grid(row=2, column=1, columnspan=2)

Password = Label(text="Password:")
Password.grid(row=3, column=0)
Password_input = Entry(width=32)
Password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password",  highlightthickness=0, command=generate)
generate_button.grid(row=3, column=2)

Add_button = Button(text="Add", width=36,  highlightthickness=0, command=save)
Add_button.grid(row=4, column=1, columnspan=2)

saerch_button = Button(text="Search", width=15, highlightthickness=0)
saerch_button.grid(row=1, column=2)

windows.mainloop()
