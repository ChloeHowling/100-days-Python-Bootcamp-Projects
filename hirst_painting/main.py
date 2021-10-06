import random
from turtle import Turtle, Screen

# import colorgram
# import random

# rgb_colors = []
# colors = colorgram.extract('Damien-Hirst-Cineole.png', 30)
# for color in colors:
#     new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

colors = [(232, 236, 233), (243, 235, 239), (41, 104, 173), (234, 205, 113), (229, 151, 84), (188, 46, 75), (117, 88, 46), (232, 117, 144), (111, 107, 189), (217, 59, 76), (53, 178, 109), (114, 186, 136), (118, 177, 215), (198, 17, 40), (114, 171, 34), (223, 55, 46), (32, 57, 114), (23, 143, 108), (182, 168, 223), (155, 224, 194), (29, 165, 174), (85, 35, 37), (31, 45, 86), (231, 168, 181), (75, 35, 31), (231, 172, 164), (113, 39, 36), (72, 78, 40)]
BG_COLOR = (251, 249, 249)
screen_size = 750
# 10 x 10 dots
# 20 size, 50 padding

screen = Screen()
screen.colormode(255)
# screen.screensize(screen_size, screen_size, "black")

greg = Turtle()
greg.speed(0)
greg.penup()
greg.hideturtle()

greg.setheading(225)
greg.forward(300)


for _ in range(10):
    for _ in range(10):
        greg.dot(20, random.choice(colors))
        greg.setheading(0)
        greg.forward(50)
    greg.setheading(90)
    greg.forward(50)
    greg.setheading(180)
    greg.forward(500)

screen.exitonclick()