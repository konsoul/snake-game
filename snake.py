from turtle import Turtle
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_COLORS = ["alice blue", "light slate gray", "royal blue", "cadet blue", "dark slate gray", "firebrick",
                "dark salmon", "dark red", "slate blue"]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("dark slate gray")
        self.move_distance = 5

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color(random.choice(SNAKE_COLORS))
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("dark slate gray")
        self.move_distance = 5

    def extend(self):
        # Add new segment to snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(self.move_distance)

    def speed_up(self):
        self.move_distance += 0.5
        print(self.move_distance)
        if self.move_distance > 25:
            self.move_distance = 25

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
