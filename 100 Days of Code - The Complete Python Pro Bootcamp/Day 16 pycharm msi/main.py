# import anothermodule
# import anothermodule
import turtle
from prettytable import PrettyTable

# from turtle import Turtle, Screen
#
# gary = Turtle()
# gary.shape("turtle")
# gary.color("coral")
# myscreen = Screen()
# gary.forward(100)
# print(myscreen.canvheight)
# print (gary)
#
# myscreen.exitonclick()

table = PrettyTable()

table.add_column("Name",["pika","charmander","squirtle"])
table.add_column("type",["electric ","fire","water"])
table.align = "l"
print(table)