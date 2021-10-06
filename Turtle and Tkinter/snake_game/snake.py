from turtle import Turtle
import random

DATA_PATH = "data.txt"
FONT = ("Chalkboard", 16, "normal")
ALIGNMENT = "center"
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self, length=3):
        for index in range(length):
            self.add_square((-20 * index, 0))

    def add_square(self, position=(0, 0)):
        square = Turtle(shape="square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.snake_body.append(square)

    def extend(self):
        self.add_square(self.snake_body[-1].position())

    def move(self, distance=20):
        for index in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[index - 1].xcor()
            new_y = self.snake_body[index - 1].ycor()
            self.snake_body[index].goto(new_x, new_y)
        self.head.forward(distance)

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

    def reset(self):
        for square in self.snake_body:
            square.hideturtle()
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]


class Food(Turtle):

    def __init__(self, color="yellow"):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(color)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.goto(0, 275)
        self.score = 0
        with open(DATA_PATH) as file:
            self.high_score = int(file.read())

        self.update()

    def update(self, scored=False):
        if scored is True:
            self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}\tHigh Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA_PATH, mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
