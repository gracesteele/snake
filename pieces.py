from turtle import Turtle


class Pieces:
    def __init__(self, xcord, ycord, shape, colour):
        self.part = Turtle(shape)
        self.xcord = xcord
        self.ycord = ycord
        self.colour = colour

    def set_pos(self):
        self.part.penup()
        self.part.goto(self.xcord, self.ycord)
        self.part.color(self.colour)
