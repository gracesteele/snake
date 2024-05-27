from pieces import Pieces
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SHAPE = "square"
COLOUR = "white"
X_CORDS = [0, -20, -40]
Y_CORD = 0

class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.tail = self.body[-1]

    def create_snake(self):
        for x_pos in X_CORDS:
            self.add_segment(x_pos, Y_CORD)

    def add_segment(self, x, y):
        new_segment = Pieces(x, y, SHAPE, COLOUR)
        new_segment.set_pos()
        self.body.append(new_segment)

    def add_to_body(self):
        tail_x = self.tail.xcord
        tail_y = self.tail.ycord
        self.add_segment(tail_x, tail_y)

    def move_snake(self):
        for i in range(len(self.body)-1, 0, -1):
            new_pos = self.body[i-1].part.pos()
            self.body[i].part.goto(new_pos)
        self.head.part.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.body:
            seg.part.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def up(self):
        if self.head.part.heading() != DOWN:
            self.head.part.setheading(UP)

    def down(self):
        if self.head.part.heading() != UP:
            self.head.part.setheading(DOWN)

    def left(self):
        if self.head.part.heading() != RIGHT:
            self.head.part.setheading(LEFT)

    def right(self):
        if self.head.part.heading() != LEFT:
            self.head.part.setheading(RIGHT)
