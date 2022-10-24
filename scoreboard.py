from turtle import Turtle
import winsound

ALIGNMENT = "center"
FONT = ("Times New Roman", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_sound = True
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 255)
        self.color("dim gray")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score : {self.high_score}",
                   align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
        self.score_sound = True

    def score_keeper(self):
        self.score += 1
        self.update_scoreboard()

    def high_score_sound(self):
        if self.score > self.high_score and self.score_sound == True:
            winsound.PlaySound('audio/high_score.wav', winsound.SND_ASYNC)
            self.score_sound = False
