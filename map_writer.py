from turtle import Turtle

class MapWriter(Turtle):
    def __init__(self, info_tuple):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(info_tuple[1], info_tuple[2])
        self.write(info_tuple[0], font=("Arial", 8, "normal"))
