#!/usr/bin/python3

import turtle


t = turtle.Turtle()


t.speed(10)


t.shape('turtle')
t.color('black')


t.penup()
t.goto(-100, -100)
t.pendown()
t.fillcolor('yellow')
t.begin_fill()
for i in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()


t.penup()
t.goto(-80, -80)
t.pendown()
t.fillcolor('white')
t.begin_fill()
for i in range(4):
    t.forward(40)
    t.left(90)
t.end_fill()
t.penup()
t.goto(40, -80)
t.pendown()
t.fillcolor('white')
t.begin_fill()
for i in range(4):
    t.forward(40)
    t.left(90)
t.end_fill()


t.penup()
t.goto(-20, -100)
t.pendown()
t.fillcolor('brown')
t.begin_fill()
for i in range(2):
    t.forward(40)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()


t.penup()
t.goto(-100, 100)
t.pendown()
t.fillcolor('red')
t.begin_fill()
t.forward(200)
t.left(135)
t.forward(141)
t.left(90)
t.forward(141)
t.left(135)
t.end_fill()


t.penup()
t.goto(100, 100)
t.pendown()
t.fillcolor('green')
t.begin_fill()
t.right(45)
t.forward(141)
t.right(135)
t.forward(200)
t.right(45)
t.forward(141)
t.right(135)
t.forward(200)
t.end_fill()

# write letters on the house
t.penup()
t.goto(-50, 0)
t.pendown()
t.color('blue')
t.write('A', font=('Arial', 20, 'bold'))
t.penup()
t.goto(50, 0)
t.pendown()
t.write('B', font=('Arial', 20, 'bold'))
t.penup()
t.goto(0, 150)
t.pendown()
t.write('C', font=('Arial', 20, 'bold'))

# finish the drawing
turtle.done()
