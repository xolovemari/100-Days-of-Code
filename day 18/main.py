import turtle as t
import random

t.colormode(255)

color_list = [
    (245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), 
    (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), 
    (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), 
    (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), 
    (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), 
    (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def setup_turtle():
    dot = t.Turtle()
    dot.hideturtle()
    dot.penup()
    dot.speed(0)
    return dot

def draw_grid(turtle, colors, rows, cols, dot_size, spacing):
    start_x = -(cols * spacing) // 2
    start_y = -(rows * spacing) // 2
    turtle.setpos(start_x, start_y)

    for _ in range(rows):
        for _ in range(cols):
            color = random.choice(colors)
            turtle.dot(dot_size, color)
            turtle.forward(spacing)
        turtle.setpos(start_x, turtle.ycor() + spacing)

def main():
    rows = 10
    cols = 10
    dot_size = 20
    spacing = 50

    dot = setup_turtle()

    draw_grid(dot, color_list, rows, cols, dot_size, spacing)

    screen = t.Screen()
    screen.exitonclick()

if __name__ == "__main__":
    main()

