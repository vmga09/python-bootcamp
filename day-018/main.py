from turtle import Turtle, Screen


timmy = Turtle()
timmy.shape("turtle")

colors = ["SteelBlue4","blue2","brown","coral4","firebrick1","gold4","maroon1","navy","OrangeRed","plum3","tomato","red3"]

def draw_shape(lados):
    angle = 360/lados
    for _ in range(lados):
        timmy.forward(100)
        timmy.right(angle)

for shape_side in range(3,11):
    timmy.color(colors[shape_side])
    draw_shape(shape_side)

# for _ in range(0,4):
#     timmy.forward(100)
#     timmy.right(90)



# timmy.color("red")
# for _ in range(0,5):
#     timmy.forward(100)
#     timmy.right(72)

# timmy.color("blue")
# for _ in range(0,6):
#     timmy.forward(100)
#     timmy.right(60)

# timmy.color("green")
# for _ in range(0,8):
#     timmy.forward(100)
#     timmy.right(45)
# for _ in range(10):
#     timmy.pen(fillcolor ='black', pencolor="red", pensize=4, pendown=True)
#     timmy.forward(10)
#     timmy.pen(fillcolor ='black', pencolor="red", pensize=30, pendown=False)
#     timmy.forward(10)




# for _ in range(0,4):
#     timmy.left(90)
#     timmy.forward(100)
    

# for _ in range(0,4):
#     timmy.right(90)
#     timmy.forward(100)
    
screen = Screen()
screen.exitonclick()