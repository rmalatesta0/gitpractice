import turtle

turtle.bgcolor("lavender")
a = turtle.Turtle()
b = turtle.Turtle()

a.color("red")
b.color("blue")
a.width(4)
b.width(4)

for x in range(4):
    a.forward(100)
    a.right(90)
print("square")

b.penup()
b.backward(500)
b.pendown()
for x in range(3):
    b.forward(100)
    b.right(120)
print("triangle")

a.left(90)
a.penup()
a.forward(150)
a.pendown()
for x in range(6):
    a.forward(100)
    a.right(60)
print("hexagon")
    
turtle.Screen().exitonclick()