from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(500, 400)
screen.listen()
user_bet = screen.textinput("make your bet", "Which turtle will win the race ? Enter a color: ")
print(user_bet)

colors = ["yellow", "purple", "red", "green", "blue", "orange"]
y_positions = [-150, -100, -50, 0, 50, 100]
all_turtles = []

for turtle_index in range(0, 6):
    t = Turtle("turtle")
    all_turtles.append(t)
    t.color(colors[turtle_index])
    t.penup()
    t.goto(-245, y_positions[turtle_index])

if user_bet:
    is_race_on = True

while is_race_on:
    for t in all_turtles:
        if t.xcor() > 200:
            is_race_on = False
            winning_color = t.pencolor()
            if user_bet == winning_color:
                print(f"You Win , {winning_color} turtle is the one !!")
            else:
                print(f"You Lose , {winning_color} turtle is the one who won!!")
        rand_distance = random.randint(0, 30)
        t.forward(rand_distance)

screen.exitonclick()
