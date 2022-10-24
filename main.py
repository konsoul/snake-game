from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import winsound
import pygame

# Make screen and set it up with certain properties
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anaconda")
screen.tracer(0)
screen.listen()

# Create our snake, food and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Create our controls for the snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Initialize sounds
pygame.mixer.init()
sound = pygame.mixer.Sound("audio/main_theme.wav")
sound.play(10)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 20:
        winsound.PlaySound('audio/apple_eat.wav', winsound.SND_ASYNC)
        food.refresh()
        scoreboard.score_keeper()
        snake.extend()
        snake.speed_up()

    # Detect collision with wall.
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()

        winsound.PlaySound('audio/game_over.wav', winsound.SND_ASYNC)

    # Detect collision with tail
    for segments in snake.segments[4:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()
            winsound.PlaySound('audio/game_over.wav', winsound.SND_ASYNC)

    if scoreboard.score > scoreboard.high_score:
        scoreboard.high_score_sound()

screen.exitonclick()
