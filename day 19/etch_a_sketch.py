from turtle import Turtle, Screen, resetscreen

sketch = Turtle()
screen = Screen()

def move_forwards():
    sketch.forward(10)

def move_backwards():
    sketch.backward(10)

def counter_clockwise():
    sketch.left(10)

def clockwise():
    sketch.right(10)

def reset_screen():
    resetscreen()

screen.listen()

screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(counter_clockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(reset_screen, "c")

screen.exitonclick()