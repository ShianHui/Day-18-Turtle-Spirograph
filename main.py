"""Main Module"""
import turtle
import random

direction = [0, 90, 180, 270, ]
tim = turtle.Turtle()
my_screen = turtle.Screen()
my_screen.colormode(255)


def draw_shape(num_of_sides):
    """Function to Draw Shape"""
    for _ in range(1, num_of_sides + 1):
        tim.forward(100)
        tim.right(360 / num_of_sides)


def randomize_color():
    """Function to randomize Color"""
    r_value = random.randint(1, 255)
    g_value = random.randint(1, 255)
    b_value = random.randint(1, 255)
    tup_value = (r_value, g_value, b_value)
    return tup_value


def random_move(paces):
    """Function to turn and move"""
    tim.setheading(random.choice(direction))
    tim.forward(paces)

def draw_spirograph(num_circles):
    """Function to draw spirograph"""
    spin_amount = int(360/num_circles)
    for radius in range(0, 360, spin_amount):
        tim.pencolor(randomize_color())
        tim.setheading(radius)
        tim.circle(100)


tim.speed("fastest")
draw_spirograph(144)


print("It's over")


my_screen.exitonclick()