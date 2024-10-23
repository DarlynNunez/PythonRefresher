#Draw a Hexagon using turtle 

import turtle
turtle.bgcolor("cyan")

turtle.pen()
turtle.shape("turtle")
turtle.pen(pencolor="purple", fillcolor="pink",pensize=2, speed=3)
turtle.begin_fill()

turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.end_fill()

#answer below

hexa = turtle.Turtle()
num_lines = 6
line_length = 100
angle = 360.0 / num_lines

for i in range(num_lines):
    hexa.forward(line_length)
    hexa.right(angle)

turtle.done()



turtle.getscreen()._root.mainloop() 