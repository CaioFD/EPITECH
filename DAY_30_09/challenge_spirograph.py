import turtle

t = turtle.Turtle(); t.speed(0); t.color("purple"); t.pensize(2)
for angle in range(0, 360, 9 ):
    t.penup(); t.goto(0, 0); t.setheading(angle); t.forward(30); t.pendown()
    t.circle(150, 60); t.left(120); t.circle(150, 60)   
turtle.done()