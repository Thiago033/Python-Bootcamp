from turtle import Turtle, Screen
import random

is_race_on = False

colors = ["black", "red", "green", "blue", "cyan", "yellow"]

screen = Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Witch turtle will win the race? Enter a color:")

y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        
        if turtle.xcor() > 200:
            winner = turtle.pencolor()
            is_race_on = 0
            
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
        
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()