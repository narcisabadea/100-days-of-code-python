from turtle import Screen
from paddle_model import Paddle
from ball_model import Ball
from scoreboard_model import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong game")

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect colision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect colision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
