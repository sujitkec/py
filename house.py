from turtle import *
from random import randint


def move(x, y):
    penup()
    goto(x, y)
    pendown()


def house(size, doorwidth, doorheight):
    # body
    fillcolor("blue")
    begin_fill()
    for i in range(4):
        right(90)
        forward(size)
    end_fill()
    # top
    fillcolor("red")
    begin_fill()
    for i in range(3):
        left(120)
        forward(size)
    end_fill()
    # goto bottom
    right(90)
    forward(size)
    right(90)
    pos = (size-doorwidth)/2+doorwidth
    forward(pos)
    # door
    fillcolor("black")
    begin_fill()
    for i in range(4):
        right(90)
        if i % 2 == 0:
            forward(doorheight)
        else:
            forward(doorwidth)
    end_fill()
    left(180)


for i in range(3):
    x, y = randint(-400, 400), randint(-400, 400)
    move(x, y)
    house(200, 60, 100)

done()
