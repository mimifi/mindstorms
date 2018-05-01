import turtle


def define_window():
    # define a window to show the flower
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("My lovely flower")
    return window


def turtle_pen():
    draw_pen = turtle.Turtle()
    draw_pen.shape("turtle")
    draw_pen.color("red")
    draw_pen.fillcolor("pink")
    draw_pen.speed(1000)

    return draw_pen


def draw_diamond(pen_to_draw):
    pen_to_draw.fillcolor("violet")
    pen_to_draw.forward(100)
    pen_to_draw.right(50)
    pen_to_draw.forward(100)
    pen_to_draw.right(130)
    pen_to_draw.forward(100)
    pen_to_draw.right(50)
    pen_to_draw.forward(100)
    pen_to_draw.right(130)


def draw_branch(pen_to_draw):
    pen_to_draw.seth(270)
    pen_to_draw.forward(300)


def draw_flower():
    screen = define_window()

    # initial a pen
    pen_to_draw = turtle_pen()

    # draw 36 times the diamond (360)
    for i in range(1, 47):
        draw_diamond(pen_to_draw)
        pen_to_draw.right(8)

    draw_branch(pen_to_draw)

    screen.exitonclick()


draw_flower()
