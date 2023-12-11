from turtle import Turtle

class Paddle:

    def __init__(self):
        turt = Turtle()
        turt.shape("square")
        turt.color("white")
        turt.penup()
        turt.resizemode("user")
        turt.turtlesize(5, 2, 0)
        turt.setposition(350, 0)
