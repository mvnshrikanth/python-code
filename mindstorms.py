import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window=turtle.Screen()
    window.bgcolor("red")

    brad=turtle.Turtle()
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed(2)
    draw_square(brad)

    angie=turtle.Turtle()
    angie.color("blue")
    angie.shape("arrow")
    angie.speed(2)
    angie.circle(100)

    window.exitonclick()

draw_art()
