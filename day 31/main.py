from tkinter import *
from random import choice
import pandas
BACKGROUND_COLOR = "#B1DDC6"
random_word = {}
words= {}
flipping = None

# ----------------------------------------
#               FLASH CARDS
# ----------------------------------------

try:
    data = pandas.read_csv("day 31/data/words_to_learn.csv")
except FileNotFoundError:
    try:
        original_data = pandas.read_csv("day 31/data/french_words.csv")
    except FileNotFoundError:
        print("File 'french_words.csv' not found.")
        exit()
    else:
        words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")

def next_card():

    global random_word, flipping
    if flipping is not None:
        window.after_cancel(flipping)

    if len(words) == 0:
        canvas.itemconfig(card_title, text="Congrats!", fill="black")
        canvas.itemconfig(card_word, text="You learned all words!", fill="black")
        canvas.itemconfig(canvas_image, image=front_card_image)
        return
    
    random_word = choice(words)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_card_image)
    
    flipping = window.after(3000, func=flip_card)

def flip_card():

    canvas.itemconfig(canvas_image, image=back_card_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_word["English"], fill="white")

# ----------------------------------------
#               SAVING DATA
# ----------------------------------------

def save_data():

    words.remove(random_word)

    new_data = pandas.DataFrame(words)
    new_data.to_csv("day 31/data/words_to_learn.csv", index=False)

    next_card()

# ----------------------------------------
#                 UI SETUP
# ----------------------------------------

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flipping = window.after(3000, func=flip_card)

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_card_image = PhotoImage(file="day 31/images/card_front.png")
back_card_image = PhotoImage(file="day 31/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card_image)

card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

# labels

# buttons
wrong_image = PhotoImage(file="day 31/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="day 31/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=save_data)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()