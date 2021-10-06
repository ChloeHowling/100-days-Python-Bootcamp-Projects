from turtle import Turtle


FONT = ("Courier", 80, "normal")


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < 230:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

    def l_surface(self):
        return self.xcor() - 21

    def r_surface(self):
        return self.xcor() + 21


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("purple")
        self.penup()
        self.speed = 1
        self.x_move = self.speed
        self.y_move = self.speed

    def move(self, repeat=1):
        for _ in range(repeat):
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def ball_speed(self, speed):
        self.speed = speed
        self.x_move /= abs(self.x_move)
        self.x_move *= self.speed
        self.y_move /= abs(self.y_move)
        self.y_move *= self.speed

    def add_speed(self, add):
        self.ball_speed(abs(self.x_move) + add)

    def reset_ball(self, position=(0, 0), speed=1):
        self.goto(position)
        self.bounce_x()
        self.bounce_y()
        self.ball_speed(speed)



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, -300)
        self.write("|\n" * 80, align="center", font=("Courier", 10, "normal"))
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=FONT)

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()
