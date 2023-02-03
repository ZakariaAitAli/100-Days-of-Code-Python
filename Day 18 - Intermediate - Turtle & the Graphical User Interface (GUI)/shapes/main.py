import turtle
import random

tim = turtle.Turtle()

tim.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw(sides):
    is_on = True
    nbr_sides = 3
    if sides < 3:
        is_on = False
    while is_on:
        for _ in range(nbr_sides):
            angle = 360 / nbr_sides
            tim.forward(100)
            tim.right(angle)
        nbr_sides += 1
        tim.color(random.choice(colours))
        if nbr_sides == sides:
            is_on = False


draw(10)

screen = turtle.Screen()
screen.exitonclick()
