from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("hotpink")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 280)
        self.write(f"Level: {self.level}", False, "left", FONT)
        
    def points(self):
        self.level += 1
        self.update_scoreboard