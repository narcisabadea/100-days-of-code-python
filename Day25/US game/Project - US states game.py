import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
total_answers = len(data)
guessed_states = []

while len(guessed_states) < total_answers:
    answer_state = screen.textinput(
        f"{len(guessed_states)}/{total_answers} States Correct", "Enter another state in the US").title()

    if answer_state == 'Exit':
        missing_states = [
            state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        coords = data[data.state == answer_state]
        new_turtle.goto(int(coords.x), int(coords.y))
        new_turtle.write(answer_state)
