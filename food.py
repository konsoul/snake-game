
from turtle import Turtle, Screen
import random

APPLE_COLORS = ["royal blue", "cadet blue", "dark slate gray", "firebrick", "dark salmon", "dark red", "slate blue"]
SCREEN_COLORS = ["gainsboro", "alice blue", "light cyan", "light yellow", "linen", "moccasin", "lavender"]
screen = Screen()


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 250)
        screen.bgcolor(random.choice(SCREEN_COLORS))
        self.color(random.choice(APPLE_COLORS))
        self.goto(x=random_x, y=random_y)
