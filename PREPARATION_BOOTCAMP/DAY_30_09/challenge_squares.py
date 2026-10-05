import turtle, random

turtle.colormode(255); t = turtle.Turtle(); t.speed(0); turtle.tracer(0)
for size in range(300, 0, -3):
    t.color("black", [random.randint(0, 255) for _ in range(3)])
    t.begin_fill()
    for _ in range(4): t.forward(size); t.left(90)
    t.end_fill(); t.left(10)
turtle.update(); turtle.done()