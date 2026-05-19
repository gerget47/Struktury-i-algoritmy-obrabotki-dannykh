import random
import turtle


def mountain(x1, y1, x2, y2, roughness, t):
    if abs(x2 - x1) < 10:
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)
    else:
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        mid_y += random.uniform(-roughness, roughness)

        mountain(x1, y1, mid_x, mid_y, roughness / 2, t)
        mountain(mid_x, mid_y, x2, y2, roughness / 2, t)


t = turtle.Turtle()
t.speed(0)
t.up()
t.goto(-300, -50)
t.down()

mountain(-300, -50, 300, -50, 100, t)

turtle.done()