# pong.py

from turtle import Screen, Turtle
from pong.paddle import Paddle
from pong.ball import Ball
from pong.scoreboard import Scoreboard
import time
import sys

def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)

    r_paddle = Paddle((350, 0))
    l_paddle = Paddle((-350, 0))
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    game_is_on = True

    try:
        while game_is_on:
            time.sleep(ball.move_speed)
            screen.update()
            ball.move()

            if ball.ycor() > 280 or ball.ycor() < -280:
                ball.bounce_y()

            if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
                ball.bounce_x()

            if ball.xcor() > 380:
                ball.reset_position()
                scoreboard.l_point()

            if ball.xcor() < -380:
                ball.reset_position()
                scoreboard.r_point()

    except Turtle.Terminator:
        game_is_on = False
        print("Game ended gracefully.")

    screen.exitonclick()

if __name__ == "__main__":
    main()