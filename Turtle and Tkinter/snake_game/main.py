from turtle import Screen
from snake import Snake, Food, ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.update(scored=True)
        snake.extend()

    # Detect collision with tail
    for square in snake.snake_body[1:]:
        if snake.head.distance(square) < 10:
            score_board.reset()
            snake.reset()

    # Detect collision with wall
    if 280 >= snake.head.xcor() >= -290 and 280 >= snake.head.ycor() >= -280:
        continue
    score_board.reset()
    snake.reset()

screen.exitonclick()
