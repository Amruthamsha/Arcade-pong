from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.L_score = 0
        self.R_score = 0


    def update_score(self):
        self.goto(-100, 200)
        self.write(self.L_score, align="center", font=("courier", 80, "normal"))
        self.goto(100,200)
        self.write(self.R_score, align="center", font=("courier", 80, "normal"))

    def L_point(self):
        self.L_score+=1
        self.clear()
        self.update_score()

    def R_point(self):
        self.R_score+=1
        self.clear()
        self.update_score()