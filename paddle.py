from turtle import Turtle

class Paddle:

    def __init__(self):
        turt = Turtle()
        turt.shape("square")
        turt.color("white")
        turt.penup()
        turt.setposition(350, 0)
