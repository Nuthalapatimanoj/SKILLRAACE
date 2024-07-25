import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Indian Flag")
screen.setup(width=800, height=450)
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()
t.speed(3)

# Draw the saffron rectangle
t.penup()
t.goto(-400, 200)
t.pendown()
t.color("orange")
t.begin_fill()
for _ in range(2):
    t.forward(800)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()

# Draw the white rectangle
t.penup()
t.goto(-400, 50)
t.pendown()
t.color("white")
t.begin_fill()
for _ in range(2):
    t.forward(800)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()

# Draw the green rectangle
t.penup()
t.goto(-400, -20)
t.pendown()
t.color("green")
t.begin_fill()
for _ in range(2):
    t.forward(800)
    t.right(90)
    t.forward(100)
    t.right(90)
t.end_fill()

# Draw the Ashoka Chakra
t.penup()
t.goto(0, 0)  # Center of the white rectangle
t.pendown()
t.color("navy")
t.pensize(2)
t.circle(45)  # Outer circle of the chakra

# Draw the 24 spokes
t.penup()
t.goto(0, 45)  # Position at the top of the circle
t.setheading(90)  # Point upwards
t.pendown()
for _ in range(24):
    t.forward(45)
    t.backward(45)
    t.left(15)  # Rotate counter-clockwise

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
