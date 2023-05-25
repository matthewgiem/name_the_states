import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pd.read_csv("50_states.csv")

while True:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").lower()
    if answer_state.capitalize() in states["state"].values:
        x = list(states.query(f"state=='{answer_state.capitalize()}'")['x'])[0]
        y = list(states.query(f"state=='{answer_state.capitalize()}'")['y'])[0]
        coordinate = (x, y)
        state = turtle.Turtle()
        state.penup()
        state.hideturtle()
        state.goto(coordinate)
        state.write(answer_state.capitalize(), font=("Verdana", 10, "normal"))


screen.exitonclick()

