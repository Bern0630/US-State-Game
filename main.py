import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_name_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 of states Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missed_states = [state for state in state_name_list if state not in guessed_states]
        create_df = pandas.DataFrame(missed_states)
        create_df.to_csv("a.csv")
        break

    if answer_state in state_name_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

