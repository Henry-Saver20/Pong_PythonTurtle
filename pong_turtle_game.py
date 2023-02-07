#python Pong Game
#Followed tutorial via GameJamMan on YT
#By Henry Saver



from tkinter import font
import turtle

## Game Engine ##

trt = turtle.Screen()
trt.title("Basic Pong Game")
trt.bgcolor("black")
trt.setup(height=600, width=800)
trt.tracer(0)

## players ##

# player 1
controller1 = turtle.Turtle()
controller1.speed(0)
controller1.shape("square")
controller1.color("white")
controller1.shapesize(stretch_len=1, stretch_wid=5)
controller1.penup()
controller1.goto(350,0)

# player 2
controller2 = turtle.Turtle()
controller2.speed(0)
controller2.shape("square")
controller2.color("white")
controller2.shapesize(stretch_len=1, stretch_wid=5)
controller2.penup()
controller2.goto(-350,0)


# Objective
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = -2
ball.dy = 2

score1 = 0
score2 = 0
p = turtle.Turtle()
p.speed(0)
p.color("white")
p.penup()
p.hideturtle()
p.goto(0,260)

def player_one_up():
    x_val, y_val = controller1.pos()

    if(y_val < 280):
        controller1.setposition(x_val, y_val + 20)
    return controller1.pos()

def player_two_up():
    x_val, y_val = controller2.pos()

    if(y_val < 280):
        controller2.setposition(x_val, y_val + 20)
    return controller2.pos()

def player_one_down():
    x_val, y_val = controller1.pos()

    if(y_val > -280):
        controller1.setposition(x_val, y_val - 20)
    return controller1.pos()

def player_two_down():
    x_val, y_val = controller2.pos()

    if(y_val > -280):
        controller2.setposition(x_val, y_val - 20)
    return controller2.pos()
score_string = "P1:" + str(score1) + "---" + "P2:" + str(score2)
p.write(score_string, align="center", font = {"Courier", 24, "normal"})
# Game Running Area #

while True:
    trt.onkeypress(player_one_up, "Up")
    trt.onkeypress(player_one_down, "Down")
    trt.onkeypress(player_two_up, "w")
    trt.onkeypress(player_two_down, "s")
    trt.listen()
    x1, y1 = controller1.pos()
    x2, y2 = controller2.pos()
    xb, yb = ball.pos()
    if(xb >= x1 and (y1-30 < yb < y1+30 ) ):
        ball.dx = -ball.dx
    if(xb <= x2 and (y2-30 < yb < y2+30 ) ):
        ball.dx = -ball.dx
    if(ball.pos()[1] > 300 or ball.pos()[1] < -300):
        ball.dy = -ball.dy
    if(ball.pos()[0] > 400):
        score1 += 1
        p.undo()
        score_string = "P1:" + str(score1) + "---" + "P2:" + str(score2)
        p.write(score_string, align="center", font = {"Courier", 24, "normal"})
        ball.setposition(0,0)
        ball.dx = -2
    elif(ball.pos()[0] < -400):
        score2 += 1
        p.undo()
        score_string = "P1:" + str(score1) + "---" + "P2:" + str(score2)
        p.write(score_string, align="center", font = {"Courier", 24, "normal"})
        ball.setposition(0,0)
        ball.dx = 2
    else:
        ball.setposition(ball.pos()[0] + (ball.dx * 1/30), ball.pos()[1] + (ball.dy * 1/30 ) )
    trt.update()
