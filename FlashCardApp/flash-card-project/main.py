# don't forget to delete the 'words_to_learn.csv' file before trying to learn French
from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("french_words.csv")
finally:
    data_list = data.to_dict(orient="records")
    current_word = choice(data_list)


def next_card():
    global current_word, flip_timer
    windows.after_cancel(flip_timer)
    current_word = choice(data_list)
    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(card_word, text=f"{current_word["French"]}", fill="black")
    canvas.itemconfig(card_title, text="French", fill="black")
    flip_timer = windows.after(3000, flip_card)


# don't remove word without seeing the translation
def remove_word():
    if rbutton:
        data_list.remove(current_word)
        df = pd.DataFrame(data_list)
        df.to_csv("words_to_learn.csv", index=False)


def flip_card():
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{current_word["English"]}", fill="white")
    remove_word()


windows = Tk()
windows.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
flip_timer = windows.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

rbutton_image = PhotoImage(file="right.png")
rbutton = Button(image=rbutton_image, highlightthickness=0, command=next_card)
rbutton.grid(row=1, column=1)

lbutton_image = PhotoImage(file="wrong.png")
lbutton = Button(image=lbutton_image, highlightthickness=0, command=next_card)
lbutton.grid(row=1, column=0)

next_card()

windows.mainloop()
