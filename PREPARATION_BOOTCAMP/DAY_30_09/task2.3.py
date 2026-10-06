import turtle

def draw_polygon(sides):
    if sides < 3:
        print("A polygon needs at least 3 sides.")
        return
    t = turtle.Turtle()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(100)
        t.right(angle)

while True:
    try:
        sides = int(input("How many sides? "))
        if sides >= 3:
            break
        print("A polygon needs at least 3 sides.")
    except ValueError:
        print("Type a integer number: ")

draw_polygon(sides)
turtle.done()