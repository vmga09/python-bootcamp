# import time
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.color("red","green")
# timmy.shape("turtle")
# timmy.forward(100)
# for _ in range(1,10):
#    timmy.turtlesize(_,_,_)
#    time.sleep(1)
#    timmy.backward(_*10)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

new_table = PrettyTable()

new_table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
new_table.add_column("Type",["Electric","Fire","Water"])
new_table.align = "l"
print(new_table)