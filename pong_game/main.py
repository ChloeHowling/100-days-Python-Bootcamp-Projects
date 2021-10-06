from turtle import Screen
from pong import Paddle, Ball, ScoreBoard

# Pong Game
# TODO:
#   Create the screen
#   Create and move a paddle (20x100 (350, 0))
#   Create another paddle
#   Create the ball and make it move
#   Detect collision with wall and bounce
#   Detect collision with paddle
#   Detect when paddle misses
#   Keep score


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_player = Paddle((350, 0))
l_player = Paddle((-350, 0))

score_board = ScoreBoard()

screen.listen()
screen.onkeypress(r_player.up, "Up")
screen.onkeypress(r_player.down, "Down")
screen.onkeypress(l_player.up, "w")
screen.onkeypress(l_player.down, "s")

ball = Ball()
ball.ball_speed(2)

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    if ball.xcor() > 0:
        if ball.xcor() > r_player.xcor() + 30:
            score_board.l_point()
            ball.reset_ball()
        elif ball.distance(r_player) < 50:
            if ball.xcor() > r_player.l_surface():
                ball.bounce_x()
                ball.add_speed(0.5)
                if abs(ball.ycor() - r_player.ycor()) > 47:
                    ball.bounce_y()
                ball.move(3)
    else:
        if l_player.xcor() - 30 > ball.xcor():
            score_board.r_point()
            ball.reset_ball()
        elif ball.distance(l_player) < 50:
            if ball.xcor() < l_player.r_surface():
                ball.bounce_x()
                ball.add_speed(0.5)
                if abs(ball.ycor() - l_player.ycor()) > 47:
                    ball.bounce_y()
                ball.move(3)

    if -280 > ball.ycor() or ball.ycor() > 290:
        ball.bounce_y()

    # old ----------------
    #
    # if l_player.xcor() - 30 > ball.xcor():
    #     score_board.r_point()
    #     ball.reset_ball()
    # elif ball.xcor() > r_player.xcor() + 30:
    #     score_board.l_point()
    #     ball.reset_ball()
    #
    # elif ball.distance(r_player) < 50 or ball.distance(l_player) < 50:
    #     if ball.xcor() > r_player.l_surface() or ball.xcor() < l_player.r_surface():
    #         print("bounced surface")
    #         ball.bounce_x()
    #         ball.add_speed(0.5)
    #         r_dis = abs(ball.ycor() - r_player.ycor())
    #         l_dis = abs(ball.ycor() - l_player.ycor())
    #         if r_dis > 49 or l_dis > 49:
    #             print(f"bounced side l: {l_dis} r: {r_dis}")
    #             ball.bounce_y()

screen.exitonclick()
