import turtle


def draw_square():
    brad_square = turtle.Turtle()
    brad_square.shape("turtle")
    brad_square.color("green")
    brad_square.speed(3)

    for i in range(1, 5):
        brad_square.forward(100)
        brad_square.right(90)


def draw_circle():
    pit_circle = turtle.Turtle()
    pit_circle.shape("triangle")
    pit_circle.color("white")

    pit_circle.circle(100)


def draw_triangle():
    fred_triangle = turtle.Turtle()
    fred_triangle.shape("circle")
    fred_triangle.color("blue")

    for i in range(0, 3):
        fred_triangle.forward(100)
        fred_triangle.left(120)


def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    window.title("My different shapes!")
    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick()


draw_shapes()
