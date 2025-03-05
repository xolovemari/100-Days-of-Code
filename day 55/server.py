from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def game_page():
    return "<h1> Guess a number between 0 and 9 </h1>" \
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:number>")
def chosen_number(number):
    correct_number = random.randint(0, 9)

    if number > correct_number:
        return "<h1 color='purple'> Too high, try again! </h1>" \
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    if number < correct_number:
        return "<h1 color='red'> Too low, try again! </h1>" \
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1 color='green'> You found me! </h1>" \
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)