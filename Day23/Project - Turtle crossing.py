from turtle import Screen
from car_model import Car
from turtle_model import Player
from scoreboard_model import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.title("Turtle crossing game")

car = Car()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    # Detect colision with car
    for c in car.all_cars:
        if c.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect succesful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        scoreboard.update_level()

screen.exitonclick()
