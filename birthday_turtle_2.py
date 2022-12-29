
import turtle
import time
def drawtwo():    
    punith = turtle.Screen()
    punith.bgcolor("black")
    luffy_op = turtle.Turtle()
    luffy_op.width(7)
    colors = ["#f5ac2f", "#279cf5", "#d820f5", "#a2f52f", "#f527c1"]


    def draw_luffy(i, x, y):
        luffy_op.pencolor("linen")
        luffy_op.color(colors[i % 7])
        luffy_op.lt(70)
        luffy_op.penup()
        luffy_op.goto(x, y)
        luffy_op.pendown()
        luffy_op.circle(22)
        luffy_op.end_fill()


    def ballon(x, y):
        luffy_op.pensize(4)
        for i in range(5):
            draw_luffy(i, x, y)


    def f1():
        for i in range(7):
            luffy_op.pensize(5)
            luffy_op.pencolor('light blue')
            luffy_op.color(colors[i % 19])
            luffy_op.begin_fill()
            luffy_op.left(330)
            luffy_op.forward(55)
            luffy_op.begin_fill()
            luffy_op.rt(110)
            luffy_op.circle(33)
            luffy_op.end_fill()
            luffy_op.rt(11)
            luffy_op.backward(33)
            luffy_op.end_fill()


    def cake(x, y):
        luffy_op.fd(x)
        luffy_op.rt(90)
        luffy_op.fd(y)
        luffy_op.rt(90)
        luffy_op.fd(x)
        luffy_op.rt(90)
        luffy_op.fd(y)


    def move(x, y):
        luffy_op.up()
        luffy_op.setposition(0, 0)
        luffy_op.setheading(90)
        luffy_op.rt(90)
        luffy_op.fd(x)
        luffy_op.lt(90)
        luffy_op.fd(y)
        luffy_op.pendown()


    def mov(x, y):
        luffy_op.up()
        luffy_op.setposition(0, 0)
        luffy_op.setheading(90)
        luffy_op.lt(90)
        luffy_op.fd(x)
        luffy_op.rt(90)
        luffy_op.fd(y)
        luffy_op.pendown()


    def A(size):
        luffy_op.rt(19)
        luffy_op.forward(size)
        luffy_op.rt(141)
        luffy_op.fd(size)
        luffy_op.backward(size / 2)
        luffy_op.rt(105)
        luffy_op.fd(int(size / 3))


    def B(size):
        luffy_op.forward(size)
        luffy_op.rt(90)
        for i in range(18):
            luffy_op.rt(9)
            luffy_op.fd(size // 20)
        for i in range(18):
            luffy_op.rt(size // 5)
            luffy_op.backward(size // 20)


    def D(size):
        luffy_op.fd(size)
        luffy_op.rt(90)
        luffy_op.fd(size // 10)
        for i in range(13):
            luffy_op.rt(13)
            luffy_op.fd(size // 8)


    def E(size):
        luffy_op.rt(90)
        luffy_op.fd(int(size / 3))
        luffy_op.back(int(size / 3))
        luffy_op.left(90)
        luffy_op.fd(size / 2)
        luffy_op.rt(90)
        luffy_op.fd(int(size / 3))
        luffy_op.back(int(size / 3))
        luffy_op.lt(90)
        luffy_op.fd(size / 2)
        luffy_op.rt(90)
        luffy_op.fd(int(size / 3))


    def H(size):
        luffy_op.fd(size)
        luffy_op.backward(size // 2)
        luffy_op.rt(90)
        luffy_op.fd(size // 2)
        luffy_op.lt(90)
        luffy_op.fd(size // 2)
        luffy_op.backward(size)


    def I(size):
        luffy_op.fd(size)
        luffy_op.rt(90)
        luffy_op.circle(size // 8)

    def L(size):
        luffy_op.rt(90)
        luffy_op.fd(int(size / 2))
        luffy_op.back(int(size / 2))
        luffy_op.lt(90)
        luffy_op.fd(size)

    def N(size):
        luffy_op.fd(size)
        luffy_op.rt(150)
        luffy_op.fd(size + int(size / 6))
        luffy_op.lt(150)
        luffy_op.fd(size)


    def P(size):
        luffy_op.fd(size)
        luffy_op.rt(90)
        luffy_op.fd(size // 8)
        for i in range(8):
            luffy_op.rt(20)
            luffy_op.fd(size // 9)

    def R():
        luffy_op.fd(60)
        luffy_op.rt(90)
        luffy_op.fd(7)
        for i in range(15):
            luffy_op.rt(12)
            luffy_op.fd(3)
        luffy_op.lt(120)
        luffy_op.fd(40)


    def S(size):
        luffy_op.rt(90)
        for i in range(0, 5):
            if i < 3:
                luffy_op.fd(size / 2)
                luffy_op.lt(90)
                if i == 2:
                    luffy_op.rt(90)
            else:
                luffy_op.right(90)
                luffy_op.fd(size / 2)


    def T(size):
        luffy_op.fd(size)
        luffy_op.rt(90)
        luffy_op.fd(size // 2)
        luffy_op.backward(size // 2)


    def Y(size):
        luffy_op.fd(size)
        luffy_op.left(60)
        luffy_op.fd(size // 2)
        luffy_op.backward(size // 2)
        luffy_op.rt(90)
        luffy_op.fd(size // 1.5)

    luffy_op.speed(19)


    mov(120, 30)
    luffy_op.color("#f7b543")
    # tech_habit.color(colors[8 % 5])
    luffy_op.begin_fill()
    cake(40, 180)
    luffy_op.end_fill()
    mov(110, 75)
    luffy_op.color("#d152f7")
    luffy_op.begin_fill()
    cake(40, 160)
    luffy_op.end_fill()
    mov(100, 120)
    luffy_op.color("#f54eb8")
    luffy_op.begin_fill()
    cake(40, 140)
    luffy_op.end_fill()
    mov(30, 170)
    luffy_op.width(11)
    luffy_op.pencolor("red")
    luffy_op.circle(7)
    move(180, 307)
    mov(0, 0)
    ballon(-490, 200)
    ballon(490, 200)
    ballon(183, -150)
    ballon(-133, -150)
    mov(330, 235)
    luffy_op.pencolor("#95ed28")
    style = ('Arial', 50, 'italic')
    luffy_op.write("From Punith...", font=style)

    luffy_op.pencolor("cyan")
    luffy_op.width(13)
    mov(260, -80)
    H(100)
    luffy_op.width(7)
    mov(190, -80)
    A(65)
    mov(135, -80)
    P(60)
    mov(100, -80)
    P(60)
    mov(52, -80)
    Y(60)
    mov(28, -80)
    B(60)
    move(12, -80)
    I(60)
    move(36, -80)
    R()
    move(80, -80)
    T(100)

    move(102, -80)
    H(60)
    move(150, -80)
    luffy_op.pencolor('hotpink')
    D(200)
    move(160, -80)
    A(60)
    move(220, -80)
    Y(60)
    time.sleep(2)
    turtle.clearscreen()
