import turtle
from turtle import Turtle


class Paddle:

    def __init__(self):
        turt = Turtle()
        turt.shape("square")
        turt.color("white")
        turt.penup()
        turt.resizemode("user")
        turt.shapesize(stretch_wid=5, stretch_len=1)
        turt.setposition(350, 0)
        self.paddle_body = turt

    def up(self):
        new_y = self.paddle_body.ycor() + 20
        self.paddle_body.goto(self.paddle_body.xcor(), new_y)

    def down(self):
        new_y = self.paddle_body.ycor() - 20
        self.paddle_body.goto(self.paddle_body.xcor(), new_y)
