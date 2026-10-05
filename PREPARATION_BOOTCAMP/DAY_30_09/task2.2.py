import turtle

t = turtle.Screen()        
t.bgcolor("black")         # background black
turt = turtle.Turtle()
turt.color("red")
for i in range(3):
    turt.right(90)
    turt.circle(50)
t.exitonclick()