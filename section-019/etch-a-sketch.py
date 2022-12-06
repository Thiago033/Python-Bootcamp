from turtle import Turtle, Screen

turtle = Turtle()
my_screen = Screen()
turtle.shape("arrow")
turtle.setheading(90)

def move_fowards():
    turtle.forward(10)

def move_backwards():
    turtle.backward(10)

def move_counter_clockwise():
    turtle.setheading(turtle.heading() + 10)
    
def move_clockwise():
    turtle.setheading(turtle.heading() - 10)
    
def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()
    
my_screen.listen()
my_screen.onkey(key="w", fun=move_fowards)
my_screen.onkey(key="a", fun=move_counter_clockwise)
my_screen.onkey(key="s", fun=move_backwards)
my_screen.onkey(key="d", fun=move_clockwise)
my_screen.onkey(key="c", fun=clear_screen)

my_screen.exitonclick()