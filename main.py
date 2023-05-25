import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pd.read_csv("50_states.csv")
guessed_states = []


while True:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state not in guessed_states:
        if answer_state in states["state"].values:
            guessed_states.append(answer_state.title())
            x = list(states.query(f"state=='{answer_state}'")['x'])[0]
            y = list(states.query(f"state=='{answer_state}'")['y'])[0]
            coordinate = (x, y)
            state = turtle.Turtle()
            state.penup()
            state.hideturtle()
            state.goto(coordinate)
            state.write(answer_state, font=("Verdana", 10, "normal"))


screen.exitonclick()

