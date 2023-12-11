from turtle import Turtle, Screen

from paddle import Paddle

screen = Screen()
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

paddle = Paddle()

for i in range(30):
    tom.forward(15)
    tom.penup()
    tom.forward(15)
    tom.pendown()

screen.listen()

screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")

screen.exitonclick()
