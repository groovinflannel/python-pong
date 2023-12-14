from turtle import Turtle, Screen

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
tom = Turtle()
tom.speed("fastest")
tom.color("white")
tom.penup()
tom.setposition(x=0, y=300)
tom.pendown()
tom.pencolor("white")
tom.setheading(270)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

for i in range(30):
    tom.forward(15)
    tom.penup()
    tom.forward(15)
    tom.pendown()

screen.listen()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

ball = Ball()


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detects wall collision, changes ball direction
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Paddle collision
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.paddle_bounce()

    # Detect left paddle point (right paddle miss)
    if ball.xcor() > 380:
        ball.reset_position()

    # Detect right paddle point (left paddle miss)
    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()
