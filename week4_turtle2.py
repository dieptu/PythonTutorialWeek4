import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Set background color

# Create first turtle
turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("red")
turtle1.pensize(3)
turtle1.speed(5)

# Move first turtle
turtle1.forward(100)
turtle1.left(90)
turtle1.forward(100)

# Create second turtle
turtle2 = turtle.Turtle()
turtle2.shape("turtle")
turtle2.color("green")
turtle2.pensize(2)
turtle2.speed(7)

# Move second turtle to a new position before drawing
turtle2.penup()
turtle2.goto(-50, -50)
turtle2.pendown()

# Move second turtle
turtle2.forward(80)
turtle2.right(120)
turtle2.forward(80)
turtle2.right(120)
turtle2.forward(80)

# Create third turtle
turtle3 = turtle.Turtle()
turtle3.shape("turtle")
turtle3.color("blue")
turtle3.pensize(4)
turtle3.speed(3)

# Move third turtle to a new position before drawing
turtle3.penup()
turtle3.goto(50, -100)
turtle3.pendown()

# Move third turtle
turtle3.circle(50)  # Draw a circle

# Exit on click
screen.exitonclick()
