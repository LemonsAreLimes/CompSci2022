import turtle

window = turtle.Screen()
x = turtle.Turtle()

def drawSqr(sqr_size=None, drawer=None):
    if sqr_size == None or drawer == None: return False         #make sure all perams are filled w/o err
    
    for i in range(4):
        drawer.fd(sqr_size)
        drawer.lt(90)

    return True

def drawPoly(side_len=None, side_num=None, drawer=None):
    if side_len==None or side_num==None or drawer==None: return

    for i in range(side_num):
        drawer.fd(side_len)
        drawer.lt(360/side_num)



def challenge_5():
    for i in range(5):
        drawSqr(30, x)

        x.penup()
        x.fd(50)
        x.pendown()

def challenge_6():
    size = 20
    for i in range(5):
        size += 10

        drawSqr(size, x)
        x.penup()
        x.bk(5)
        x.lt(90)
        x.bk(5)
        x.rt(90)
        x.pendown()

def challenge_7():
    drawPoly(50, 8, x)

def challenge_8():
    for i in range(25):
        x.lt(45 / 3)
        drawSqr(100, x)

def challenge_9_point_5():
    fwd_len = 120
    spacer = 5          #warning! a high spacer value will cause fwd_len go negative

    for i in range(25):
        fwd_len -= spacer
        x.fd(fwd_len)
        x.lt(90)
        # x.lt(90 + i)  #uncomment this to use the outher spiral

def challenge_10():
    for i in range(15):
        x.fd(120)
        x.bk(120)
        x.lt(360/15)


# challenge_5()
# challenge_6()
# challenge_7()
# challenge_8()
# challenge_9_point_5()
challenge_10()

window.exitonclick()