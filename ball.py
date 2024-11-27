from turtle import Turtle
turtle = Turtle()

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new, y_new)


    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.move_speed*=0.9
        self.x_move *= -1

    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()