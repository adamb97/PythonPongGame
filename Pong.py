# Simple Pong game in Py thon
# By Adam Benalayat

import turtle

win = turtle.Screen()

win.title("Adam's Pong Game")

win.bgcolor("black")
win.setup(width=800, height=600)
# Tracer method stops the window from updating, so we have to manually update it
win.tracer(0)

# Score
score_one = 0
score_two = 0


# Paddle 1
paddle_one = turtle.Turtle()
paddle_one.speed(0)
paddle_one.shape("square")
paddle_one.color("white")
paddle_one.penup()
paddle_one.goto(-350, 0)
paddle_one.shapesize(stretch_wid=5, stretch_len=1)

# Paddle 2
paddle_two = turtle.Turtle()
paddle_two.speed(0)
paddle_two.shape("square")
paddle_two.color("white")
paddle_two.penup()
paddle_two.goto(+350, 0)
paddle_two.shapesize(stretch_wid=5, stretch_len=1)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player One: 0   Player Two: 0", align="center", font=("Courier", 24, "bold"))




# Functions
def paddle_one_up():
    y = paddle_one.ycor()
    y += 20
    paddle_one.sety(y)
def paddle_one_down():
    y = paddle_one.ycor()
    y -= 20
    paddle_one.sety(y)

def paddle_two_up():
    y = paddle_two.ycor()
    y += 20
    paddle_two.sety(y)
def paddle_two_down():
    y = paddle_two.ycor()
    y -= 20
    paddle_two.sety(y)

# Keyboard binding
win.listen()
win.onkeypress(paddle_one_up, "w")
win.onkeypress(paddle_one_down, "s")
win.onkeypress(paddle_two_up, "Up")
win.onkeypress(paddle_two_down, "Down")



# Main game Loop
while True:
    win.update()


    #Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_one += 1
        pen.clear()
        pen.write("Player One: {}   Player Two: {}".format(score_one, score_two), align="center", font=("Courier", 24, "bold"))

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_two += 1
        pen.clear()
        pen.write("Player One: {}   Player Two: {}".format(score_one, score_two), align="center", font=("Courier", 24, "bold"))

    # Collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_one.ycor() + 50 and ball.ycor() > paddle_one.ycor() - 50:
        ball.dx *= -1 
        
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_two.ycor() + 50 and ball.ycor() > paddle_two.ycor() - 50:
        ball.dx *= -1