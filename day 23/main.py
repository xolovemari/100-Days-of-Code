import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(turtle.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.update_cars()

    if turtle.next_level():
        scoreboard.points()
        car_manager.new_speed()

    for car in car_manager.all_cars:
        if turtle.distance(car) < 20:
            scoreboard.game_over()
            screen.update()
            game_is_on = False

screen.exitonclick()