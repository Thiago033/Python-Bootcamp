from turtle import Turtle, Screen
import random

colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]

turtle = Turtle()

turtle.shape("turtle")
turtle.hideturtle()
turtle.color("black")
turtle.pensize(3)
turtle.speed(0)


# def make_square():
#     for _ in range(4):
#         turtle.forward(100)
#         turtle.right(90)


def make_circle():
    turtle.circle(90)


def make_dashed_line():
    for _ in range(10):
        turtle.pendown()
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)


def make_different_shapes(num_sides):
    angle = 360 / num_sides
    
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)


def make_random_walk(lengh):
    
    directions = [0, 90 ,180 ,270]
    
    
    for _ in range(lengh):
        #turtle.color(random.choice(colors))
        position = random.choice(directions)
        turtle.setheading(position)
        turtle.forward(50)
        
      
def make_spirograph(radios, gap):
    for _ in range(int(360 / gap)):
        turtle.color(random.choice(colors))
        turtle.circle(radios)
        turtle.setheading(turtle.heading() + gap)
        

#make_square()
#make_circle()
#make_dashed_line()

# for i in range(3, 11):
#     make_different_shapes(i)

#make_random_walk(500)

make_spirograph(150, 1)

my_screen = Screen()
my_screen.exitonclick()