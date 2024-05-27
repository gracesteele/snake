from pieces import Pieces
import random


def random_coord():
    return random.randint(-280, 280)


class Food:
    def __init__(self):
        self.food = Pieces(random_coord(), random_coord(), "circle", "purple")
        self.food.part.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food.part.speed("fastest")
        self.food.set_pos()
        self.refresh()

    def refresh(self):
        self.food.part.goto(random_coord(), random_coord())
