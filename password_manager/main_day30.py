from tkinter import *   # only imports all the classes and constants
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from password_generator import password_generator
password = password_generator()
pyperclip.copy(f'{password}')


def generate():
    Password_input.insert(0, f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    global password
    websites = website_input.get().lower()
    email = Email_input.get()
    # password = Password_input.get()
    new_data = {
        websites: {
            "email": email,
            "password": Password_input.get()
        }
    }
    if len(websites) == 0 or len(Password_input.get()) == 0:
        messagebox.showinfo(title="Oops", message="PLease make sure you haven't left any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:

            # Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            Password_input.delete(0, END)


def search_password():
    websites = website_input.get().lower()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)

        messagebox.showinfo(title=websites, message=f"Email:{data[websites]["email"]}"
                                                   f"\nPassword: {data[websites]["password"]}")
    except KeyError as error_message:
        messagebox.showinfo(title="Error", message=f"The password for {error_message} does not exist here.")

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data file found")

    else:
        pass
    finally:
        website_input.delete(0, END)
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

search_button = Button(text="Search", width=15, highlightthickness=0, command=search_password)
search_button.grid(row=1, column=2)

windows.mainloop()
