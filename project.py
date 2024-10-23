

import turtle
turtle.bgcolor("cyan")

turtle.pen()
turtle.shape("turtle")
turtle.pen(pencolor="purple", fillcolor="green",pensize=2, speed=3)
turtle.position()

turtle_1 = turtle.Turtle()
turtle_1.color("green")
turtle_1.pos(0.0 , 5.0)

turtle_2 = turtle_1.clone()
turtle_2.color("blue")
turtle_2.pos(0.0 , 0.0)

turtle_3 = turtle_2.clone()
turtle_3.color("red")
turtle_3.pos(0.0 , -5.0)



turtle.getscreen()._root.mainloop() 