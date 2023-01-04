import turtle as t
import random

new_turtle = t.Turtle()
t.colormode(255)

# names colors
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# random RBG colors by using a tuple
# a tuple can't be changed like within a list (can't support item assignemt, can't remove element from tupple => is immutable so it can't be changed)
# a tuple can be converted to a list in order to change it: list(my_tuple)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


directions = [0, 90, 180, 270]
new_turtle.pensize(10)
new_turtle.speed("fastest")

for _ in range(200):
    # names colors
    # new_turtle.color(random.choice(colours))

    # random RBG colors
    new_turtle.pencolor(random_color())
    new_turtle.forward(30)
    new_turtle.setheading(random.choice(directions))
