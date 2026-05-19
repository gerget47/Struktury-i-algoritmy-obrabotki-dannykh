import turtle

def koch_side(length, level):
    if level == 0:
        t.forward(length)
    else:
        koch_side(length / 3, level - 1)
        t.left(60)
        koch_side(length / 3, level - 1)
        t.right(120)
        koch_side(length / 3, level - 1)
        t.left(60)
        koch_side(length / 3, level - 1)

def snowflake(length, level):
    for _ in range(3):
        koch_side(length, level)
        t.right(120)

t = turtle.Turtle()
t.speed(0)
t.up()
t.goto(-150, 100)
t.down()

snowflake(300, 3)

turtle.done()