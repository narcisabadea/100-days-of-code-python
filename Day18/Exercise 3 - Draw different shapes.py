from turtle import Turtle
import random

new_turtle = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        new_turtle.forward(100)
        new_turtle.right(angle)


for shape_side_n in range(3, 10):
    new_turtle.color(random.choice(colours))
    draw_shape(shape_side_n)
