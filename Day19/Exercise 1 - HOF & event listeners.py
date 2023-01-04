# Higher order function

# passing a function as an argument to another function OR returning a function from another function
# for ex JavaScript and Python provides us with some inbuilt higher order functions like map(), filter(), reduce().

from turtle import Turtle, Screen

new_turtle = Turtle()
screen = Screen()


def move_forward():
    new_turtle.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()
