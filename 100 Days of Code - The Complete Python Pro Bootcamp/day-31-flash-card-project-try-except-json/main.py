from tkinter import *
import math
import pandas
import random

from pandas.core.interchange.dataframe_protocol import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
column_names = ['French', 'English']

def known():
    global card_index
    global cards
    del cards[card_index]
    to_learn = [(row["French"], row["English"]) for index,row in data.iterrows() if index in cards]
    # with open("data/words_to_learn.csv","w") as data_file:
    df = pandas.DataFrame(to_learn, columns=column_names)
    df.to_csv("data/words_to_learn.csv")
    new_card()
    print(len(cards))


def new_card():
    global card_index,flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(background, image=card_front_img)
    canvas.itemconfig(language_text, text=f"French",fill="black")
    card_index = random.randint(0,len(cards))
    canvas.itemconfig(french_text, text=f"{fr_dict[card_index][0]}",fill="black")
    flip_timer = window.after(2000, english)
    # canvas.delete(french_text)
    # french_text = canvas.create_text(400, 263, text=f"{fr_dict[card_index][0]}", fill="black", font=("Ariel", 60, "bold"))



def english():
    global card_index
    canvas.itemconfig(french_text, text=f"{fr_dict[card_index][1]}",fill="white")
    canvas.itemconfig(language_text, text=f"English",fill="white")
    canvas.itemconfig(background,image=card_back_img )

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    with open("data/words_to_learn.csv") as data_file:
        data = pandas.read_csv(data_file)
except FileNotFoundError:
    with open("data/french_words.csv") as data_file:
        data = pandas.read_csv(data_file)

fe_dict = data.to_dict()
fr_dict = [(row["French"],row["English"]) for index, row in data.iterrows()]
print(fr_dict)

card_index = 0

cards = [card for card in range(0, len(data))]
print(cards)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
background = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 160, text="French", fill="black", font=("Ariel", 40, "italic"))
french_text = canvas.create_text(400, 263, text=f"{fe_dict["French"][card_index]}", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
flip_timer =window.after(2000,english)
new_card()

right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=known)
known_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=new_card)
unknown_button.grid(column=0, row=1)


window.mainloop()