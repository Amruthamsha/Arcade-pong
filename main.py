from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

scoreboard = Scoreboard()
ball = Ball()
turtle = Turtle()
turtle.hideturtle()
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("BONG")
screen.tracer(0)

l_paddle = Paddle((-390, 0))
r_paddle = Paddle((380, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "u")
screen.onkey(l_paddle.down, "d")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()

    #collision with upper and bottom walls
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()


    #collision with the paddle
    if ball.xcor() > 350 and ball.distance(r_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() < -350 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    #ball misses paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.L_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.R_point()

screen.exitonclick()