import turtle 
import pandas

screen = turtle.Screen()
import turtle 
import pandas

screen = turtle.Screen()
screen.setup(725, 491)
image = "day 25 part 2/blank_states_img.gif"
screen.bgpic(image)
screen.tracer(0)

turtle_aux = turtle.Turtle()
turtle_aux.penup()
turtle_aux.hideturtle()

data = pandas.read_csv("day 25 part 2/50_states.csv")
xy_list = list(zip(data["x"], data["y"]))
states_list = data["state"].to_list()

points = 0

game_is_on = True
while game_is_on:
    screen.title(f"U.S. States Game - {50 - points}/50")
    answer_state = screen.textinput("Guess the State", "What's another state's name? Digit 'Exit' to leave.")

    if answer_state is not None:
        answer_state = answer_state.lower()

        if answer_state in map(str.lower, states_list):
            index = states_list.index(answer_state.title())
            turtle_aux.goto(xy_list[index])
            turtle_aux.color("blue")
            turtle_aux.write(f"{answer_state.title()}", font=("Arial", 7, "normal"))
            turtle_aux.color("black")
            states_list.remove(answer_state.title())
            points += 1
            screen.update()

        if answer_state == "exit":
            turtle_aux.goto(0, 0)
            turtle_aux.write(
                f"Your final pontuation is {points}.\nThanks for playing!", 
                align="center", 
                font=("Arial", 16, "bold")
            )
            screen.update()
            game_is_on = False

        if not states_list:
            turtle_aux.goto(0, 0)
            turtle_aux.write(
                "Congratulations! You've got them all right!",
                align="center",
                font=("Arial", 16, "bold")
            )
            screen.update()
        
screen.exitonclick()