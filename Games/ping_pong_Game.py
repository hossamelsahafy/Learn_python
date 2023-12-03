#!/usr/bin/python3
# import turtle module
import turtle

wind = turtle.Screen()  # initialize screen
wind.title("Ping pong by Hos")  # title of the window
wind.bgcolor("black")  # background color
wind.setup(width=800, height=600)  # screen width  and height
wind.tracer(0)  # stop the update of window

# object 1
object1 = turtle.Turtle()  # initialize turtle object1
object1.speed(0)  # speed of object1
object1.shape("square")  # set the shape of object1
object1.shapesize(stretch_wid=5, stretch_len=1)  # stretch shape size
object1.color("yellow")  # color of object1
object1.penup()  # stop object1 from drawing lines
object1.goto(-350, 0)  # the position of object1


# object 2
object2 = turtle.Turtle()  # initialize turtle object2
object2.speed(0)  # speed of object2
object2.shape("square")  # set the shape of object2
object2.shapesize(stretch_wid=5, stretch_len=1)  # stretch shape size
object2.color("green")  # color of object2
object2.penup()  # stop object2 from drawing lines
object2.goto(350, 0)  # the position of object2

# ball
ball = turtle.Turtle()  # initialize turtle ball
ball.speed(0)  # speed of ball
ball.shape("circle")  # set the shape of ball
ball.color("white")  # color of ball
ball.penup()  # stop ball from drawing lines
ball.goto(0, 0)  # the position of ball
ball.dx = 1  # speed of  the ball
ball.dy = 1  # speed of the ball

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player 1:0 player2: 0", align="center", font=("courier", 24, "normal"))


# functions for object1
def object1_move_up():
    y = object1.ycor()  # get the y for object1
    y += 20  # the y increased by 20
    object1.sety(y)  # set the y of object1 to new y coordinate


def object1_move_down():
    y = object1.ycor()  # get the y for object1
    y -= 20  # the y decreased by 20
    object1.sety(y)  # set the y of object1 to new y coordinate


# functions for object2
def object2_move_up():
    y = object2.ycor()  # get the y for object2
    y += 25  # y increased by 20
    object2.sety(y)  # set the y of object2 to the new coordinate


def object2_move_down():
    y = object2.ycor()  # get the y for object2
    y -= 25  # y increased by 20
    object2.sety(y)  # set the y of object2 to the new coordinate


# keyboard bindings
wind.listen()
wind.onkeypress(object1_move_up, "w")  # make specific key to go up for object1
wind.onkeypress(object1_move_down, "s")  # make specific key to go down for object1

wind.onkeypress(object2_move_up, "Up")  # make specific key to go up for object2
wind.onkeypress(object2_move_down, "Down")  # make specific key to go down for object2
# game loop
while True:
    wind.update()  # update screen

    # move the ball
    ball.setx(ball.xcor() + ball.dx)  # ball start at 0, while loop running  ---> + 1
    ball.sety(ball.ycor() + ball.dy)  # ball start at 0, while loop running  ---> + 1

    # border check top border +300px, ball is 20px, bottom border -300
    if ball.ycor() > 290:  # if ball is at top border
        ball.sety(290)  # set y coordinate +290
        ball.dy *= -1  # reverse direction, 1 --> -1

    if ball.ycor() < -290:  # if ball in bottom border
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:  # if ball in right border
        ball.goto(0, 0)  # return ball to the center
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write(
            "player1: {} player2: {}".format(score1, score2),
            align="center",
            font=("courier", 24, "normal"),
        )

    if ball.xcor() < -390:  # if ball in left border
        ball.goto(0, 0)  # #return ball to the center
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(
            "player1: {} player2: {}".format(score1, score2),
            align="center",
            font=("courier", 24, "normal"),
        )

    # hitting the ball by the two objects

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
        ball.ycor() < object1.ycor() + 40 and ball.ycor() > object1.ycor() - 40
    ):
        ball.setx(-340)
        ball.dx *= -1

    if (ball.xcor() > 340 and ball.xcor() < 350) and (
        ball.ycor() < object2.ycor() + 40 and ball.ycor() > object2.ycor() - 40
    ):
        ball.setx(340)
        ball.dx *= -1
