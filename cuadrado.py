import turtle
t = turtle.Turtle()
t.speed(1)
t.penup()
t.goto(-50, 0)
t.pendown()

# Draw a triangle with side length 100
for _ in range(3):
    t.forward(100)
    t.right(120)

import turtle
t = turtle.Turtle()
t.speed(1)
t.penup()
t.goto(-200, 10)
t.pendown()

# Draw a square with side length 100
for _ in range(4):
    t.forward(100)
    t.right(90)

import turtle

t = turtle.Turtle()
t.speed(1)
t.penup()
t.goto(0, -100)
t.pendown()

# Draw a circle with radius 100
t.circle(100)
