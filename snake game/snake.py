from turtle import Screen, Turtle

MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = ((0, 0), (-20, 0), (-40, 0))

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_segment(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num-1].pos())
        self.head.forward(MOVE_DIST)
    
    def up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(90)
    def down(self):
        if(self.head.heading() != UP):
            self.head.setheading(270)
    def left(self):
        if(self.head.heading() != RIGHT):
            self.head.setheading(180)
    def right(self):
        if(self.head.heading() != LEFT):
            self.head.setheading(0)
