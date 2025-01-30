import os
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        diretorio_atual = os.path.dirname(__file__)
        caminho_data = os.path.join(diretorio_atual, "data.txt")

        with open(caminho_data) as data:
            self.high_score = int(data.read())
        self.color("purple")  
        self.penup()              
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", False, align="center", font=("Arial", 18, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            diretorio_atual = os.path.dirname(__file__)
            caminho_data = os.path.join(diretorio_atual, "data.txt")

            with open(caminho_data, "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()