import turtle

def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)

def draw_circle():
    turtle.circle(50)

def draw_triangle():
    for _ in range(3):
        turtle.forward(100)
        turtle.right(120)

def main():
    turtle.speed(1)

    # Draw a square
    turtle.color("blue")
    draw_square()

    # Move to the next position
    turtle.penup()
    turtle.goto(-100, 0)
    turtle.pendown()

    # Draw a circle
    turtle.color("red")
    draw_circle()

    # Move to the next position
    turtle.penup()
    turtle.goto(50, 50)
    turtle.pendown()

    # Draw a triangle
    turtle.color("green")
    draw_triangle()

    # Hide the turtle and display the art
    turtle.hideturtle()
    turtle.done()
