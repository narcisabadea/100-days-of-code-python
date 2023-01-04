from turtle import Turtle, Screen

new_turtle = Turtle()
screen = Screen()


def move_forward():
    new_turtle.forward(10)


def move_back():
    new_turtle.back(10)


def turn_right():
    new_turtle.right(10)


def turn_left():
    new_turtle.left(10)


def clear():
    new_turtle.clear()
    new_turtle.penup()
    new_turtle.home()
    new_turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
