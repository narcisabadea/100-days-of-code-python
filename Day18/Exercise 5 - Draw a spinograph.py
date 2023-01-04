import turtle as t
import random

new_turtle = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        new_turtle.color(random_color())
        new_turtle.circle(100)
        new_turtle.setheading(new_turtle.heading() + size_of_gap)


draw_spirograph(5)
