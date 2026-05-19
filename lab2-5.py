import turtle
import random


def tree(branchLen, t, width):
    if branchLen > 5:
        t.pensize(width)

        if branchLen < 15:
            t.color("green")
        else:
            t.color("brown")

        t.forward(branchLen)

        angle = random.uniform(15, 45)
        t.right(angle)

        new_len = branchLen - random.uniform(10, 20)
        tree(new_len, t, width * 0.7)

        t.left(angle * 2)
        tree(new_len, t, width * 0.7)

        t.right(angle)
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.speed(0)
    tree(75, t, 10)
    myWin.exitonclick()


main()