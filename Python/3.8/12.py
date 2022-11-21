import turtle

screen = turtle.Screen()
teknős = turtle.Turtle()
screen.bgcolor("lightgreen")
teknős.color("blue")
teknős.shape("turtle")
teknős.pensize(3)
for x in range(0, 12):
     teknős.penup()
     teknős.forward(100)
     teknős.pendown()
     teknős.forward(10)
     teknős.penup()
     teknős.forward(20)
     teknős.stamp()
     teknős.back(130)
     teknős.left(30)



screen.mainloop()