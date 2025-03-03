import turtle
import random

def random_color():
    """Generates a random color."""
    return (random.random(), random.random(), random.random())

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Fractal Tree")

# Set up the turtle
tom = turtle.Turtle()
tom.shape("turtle")
tom.left(90)
tom.speed(0)  # Maximum speed

def draw_tree(length, depth):
    """Draws a fractal tree with dynamic color branches."""
    if depth == 0:
        return

    tom.pensize(depth)
    tom.pencolor(random_color())  # Random color for each branch

    tom.forward(length)

    tom.left(30)
    draw_tree(length * 0.7, depth - 1)  # Left branch

    tom.right(60)
    draw_tree(length * 0.7, depth - 1)  # Right branch

    tom.left(30)

    tom.backward(length)  # Return to the original position

# Draw the fractal tree
initial_length = 100
initial_depth = 12
draw_tree(initial_length, initial_depth)

# Exit on click
screen.exitonclick()
