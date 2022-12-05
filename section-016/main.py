from turtle import Turtle, Screen
from prettytable import PrettyTable
import another_module

#print(another_module.another_variable)
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")

# timmy.forward(100)
# timmy.circle(50)

# my_screen = Screen()
# my_screen.exitonclick()

table = PrettyTable()

table.add_column("City Name",["data 1","data 2","data 3"])
table.add_column("Type",["data 1","data 2","data 3"])

table.align = "l"

print(table)