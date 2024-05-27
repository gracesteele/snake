from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
BOUNDARY = 290

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_on = True
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food
    if snake.head.part.distance(food.food.part) < 13:
        food.refresh()
        snake.add_to_body()
        score.increase_score()

    # Detect collision with wall
    if snake.head.part.xcor() > BOUNDARY or snake.head.part.xcor() < -BOUNDARY or snake.head.part.ycor() > BOUNDARY or snake.head.part.ycor() < -BOUNDARY:
        # game_on = False
        # score.gameover()
        score.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.body[1:]:
        if snake.head.part.distance(segment.part) < 10:
            # game_on = False
            # score.gameover()
            score.reset()
            snake.reset()

screen.exitonclick()
