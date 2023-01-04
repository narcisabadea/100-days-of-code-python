import turtle as turtle_module
import random
import colorgram

# getting colors from the image
color_list = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    color_list.append(color.rgb)

print(color_list)


turtle_module.colormode(255)
new_turtle = turtle_module.Turtle()

new_turtle.speed("fastest")
new_turtle.penup()
new_turtle.hideturtle()
new_turtle.setheading(225)
new_turtle.forward(300)
new_turtle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    new_turtle.dot(20, random.choice(color_list))
    new_turtle.forward(50)

    if dot_count % 10 == 0:
        new_turtle.setheading(90)
        new_turtle.forward(50)
        new_turtle.setheading(180)
        new_turtle.forward(500)
        new_turtle.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
