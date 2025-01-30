from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.count = 0
        self.speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
        
    def new_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(1, 2)
        new_car.color(random.choice(COLORS))
        new_car.setheading(180)
        new_car.penup()

        rand_y = random.randint(-250, 250)
        new_car.goto(300, rand_y)

        self.all_cars.append(new_car)

    def should_create_car(self):
        self.count += 1
        if self.count % 6 == 0:
            self.new_car()

    def move_cars(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.speed
            car.setx(new_x)

    def new_speed(self):
        self.speed += MOVE_INCREMENT

    def remove_off_screen_cars(self):
        self.all_cars = [car for car in self.all_cars if car.xcor() > -320]

    def update_cars(self):
        self.should_create_car()

        self.move_cars()

        self.remove_off_screen_cars()