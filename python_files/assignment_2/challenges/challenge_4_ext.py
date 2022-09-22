def get_numbers():
    import random

    num_1 = random.randint(0,360)
    num_2 = random.randint(0,360)
    
    return [num_1, num_2]


def draw(set=None):
    import turtle
    import time

    screen = turtle.Screen()
    screen.exitonclick()
    x = turtle.Turtle()

    if set==None: return

    for i in 100:

        time.sleep(1)

        x.left(set[0])
        x.forward(10)
    
        for i in 50:
            time.sleep(1)

            x.right(set[1])
            x.forward(5)

