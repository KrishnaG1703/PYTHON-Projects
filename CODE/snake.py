from turtle import Turtle
positions = [(0, 0), (-20, 0), (-40, 0)]
Move = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:

    def __init__(self):
        self.total = []
        self.creating_snake()
        self.head = self.total[0]
        self.tail = self.total[-1]

    def creating_snake(self):
        for turtles in positions:
            new_seg = Turtle('square')
            new_seg.color('white')
            new_seg.penup()
            new_seg.goto(turtles)
            self.total.append(new_seg)

    def moves(self):
        for seg in range(len(self.total)-1, 0, -1):
            x_cor = self.total[seg - 1].xcor()
            y_cor = self.total[seg-1].ycor()
            self.total[seg].goto(x_cor, y_cor)
        self.total[0].forward(Move)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def addsnake(self):
        new = Turtle('square')
        new.color('white')
        new.penup()
        tx_cor = self.tail.xcor()
        ty_cor = self.tail.ycor()
        new.goto(tx_cor,ty_cor)
        self.total.append(new)