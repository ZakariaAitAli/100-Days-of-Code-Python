# import colorgram
# colors = colorgram.extract('image.jpg', 100)
# color_bank = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_rgb = (r, g, b)
#     color_bank.append(color_rgb)
# print(color_bank)
import turtle as t
import random

rgb_colors = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130),
              (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104),
              (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170),
              (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44),
              (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169), (179, 188, 212),
              (48, 74, 73), (147, 37, 35), (43, 62, 61)]

t.colormode(255)
tim = t.Turtle()
tim.penup()
tim.speed("fastest")
tim.hideturtle()

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

numbers_dots = 100
for dot_count in range(1, numbers_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
