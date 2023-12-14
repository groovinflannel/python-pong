from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(position)
        self.score = 0
        self.write(self.score, align="center", font=('Courier', 20, 'bold'))

    def increment(self):
        self.score += 1
        self.clear()
        self.write(self.score, align="center", font=('Courier', 20, 'bold'))
