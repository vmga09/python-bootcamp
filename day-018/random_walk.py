from turtle import Turtle, colormode ,Screen
import random

colormode(255)
timmy = Turtle()
timmy.shape("turtle")

colors = ["SteelBlue4","blue2","brown","coral4","firebrick1","gold4","maroon1","navy","OrangeRed","plum3","tomato","red3"]
movers = [timmy.right(90),timmy.left(90)]


def random_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))




while True:
    #random.choice(movers)
    color = random_color()
    timmy.right(90)
    timmy.forward(random.randint(1,100))
    timmy.color(color)







screen = Screen()
screen.exitonclick()