import turtle
import winsound

# Window Setup
Wn = turtle.Screen()
Wn.title('Pong')
Wn.bgcolor('black')
Wn.setup(width=800, height=600)
Wn.tracer(0)

# Score
Score_1 = 0
Score_2 = 0

# Paddle 1
Paddle_1 = turtle.Turtle()
Paddle_1.speed(0)
Paddle_1.shape('square')
Paddle_1.shapesize(stretch_wid=5, stretch_len=1)
Paddle_1.color('white')
Paddle_1.penup()
Paddle_1.goto(-350, 0)

# Paddle 2
Paddle_2 = turtle.Turtle()
Paddle_2.speed(0)
Paddle_2.shape('square')
Paddle_2.shapesize(stretch_wid=5, stretch_len=1)
Paddle_2.color('white')
Paddle_2.penup()
Paddle_2.goto(350, 0)

# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape('square')
Ball.color('white')
Ball.penup()
Ball.goto(0, 0)
# Adjust Ball Speed
Ball.dx = 0.2
Ball.dy = 0.2


# Pen
Pen = turtle.Turtle()
Pen.speed(0)
Pen.color('white')
Pen.penup()
Pen.hideturtle()
Pen.goto(0, 260)
Pen.write("0    0", align='center', font=('Courier', 24, 'normal'))

# Function
def Paddle_1_Up():
    y = Paddle_1.ycor()
    y += 20
    Paddle_1.sety(y)


def Paddle_1_Down():
    y = Paddle_1.ycor()
    y -= 20
    Paddle_1.sety(y)


def Paddle_2_Up():
    y = Paddle_2.ycor()
    y += 20
    Paddle_2.sety(y)


def Paddle_2_Down():
    y = Paddle_2.ycor()
    y -= 20
    Paddle_2.sety(y)


# Keyboard Binding
Wn.listen()
Wn.onkeypress(Paddle_1_Up, "w")
Wn.onkeypress(Paddle_1_Down, "s")
Wn.onkeypress(Paddle_2_Up, "Up")
Wn.onkeypress(Paddle_2_Down, "Down")

# Main Game Loop
while True:
    Wn.update()

    # Move Ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    # Border Checking
    if Ball.ycor() > 290:
        Ball.dy *= -1
        winsound.PlaySound('ping_pong_8bit_plop.wav', winsound.SND_ASYNC)
    if Ball.ycor() < -290:
        Ball.dy *= -1
        winsound.PlaySound('ping_pong_8bit_plop.wav', winsound.SND_ASYNC)

    if Ball.xcor() > 390:
        winsound.PlaySound('ping_pong_8bit_peeeeeep.wav', winsound.SND_ASYNC)
        Ball.goto(Paddle_1.xcor() + 10, Paddle_1.ycor())
        Ball.dx = 0.2
        Score_1 += 1
        Pen.clear()
        Pen.write("{}    {}".format(Score_1, Score_2), align='center', font=('Courier', 24, 'normal'))

    if Ball.xcor() < -390:
        winsound.PlaySound('ping_pong_8bit_peeeeeep.wav', winsound.SND_ASYNC)
        Ball.goto(Paddle_2.xcor() - 10, Paddle_2.ycor())
        Ball.dx = 0.2
        Score_2 += 1
        Pen.clear()
        Pen.write("{}    {}".format(Score_1, Score_2), align='center', font=('Courier', 24, 'normal'))

    # Paddle and Ball Collision
    if 350 > Ball.xcor() > 340 and Paddle_2.ycor() + 50 > Ball.ycor() > Paddle_2.ycor() - 50:
        Ball.dx *= -1
        winsound.PlaySound('ping_pong_8bit_beeep.wav', winsound.SND_ASYNC)

    if -350 < Ball.xcor() < -340 and Paddle_1.ycor() + 50 > Ball.ycor() > Paddle_1.ycor() - 50:
        Ball.dx *= -1
        winsound.PlaySound('ping_pong_8bit_beeep.wav', winsound.SND_ASYNC)

    #Paddle and Wall Collision
    if Paddle_1.ycor() + 50 > 300:
        Paddle_1.goto(-350, 250)

    if Paddle_1.ycor() - 50 < -300:
        Paddle_1.goto(-350, -250)

    if Paddle_2.ycor() + 50 > 300:
        Paddle_2.goto(350, 250)

    if Paddle_2.ycor() - 50 < -300:
        Paddle_2.goto(350, -250)
