
import turtle
turtle.bgcolor("cyan")

turtle.pen()
turtle.shape("turtle")
turtle.pen(pencolor="purple", fillcolor="pink",pensize=10, speed=8)
turtle.begin_fill()
turtle.dot(50)
turtle.forward(100)
turtle.left(20)
turtle.forward(100)
turtle.end_fill()


turtle.getscreen()._root.mainloop() 