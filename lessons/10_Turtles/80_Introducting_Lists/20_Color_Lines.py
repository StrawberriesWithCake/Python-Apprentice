"""
Color Lines

1) Finish the program to make Tina draw a square with each side being a different color. 

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

forward = 60
colors = [ 'red', 'blue', 'black', 'orange']    # define a list of colors
left = 90

for color in colors:                            # loop through the colors
    tina.color(color)
    tina.forward(forward)
    tina.left(left)


# 2) Make another square, but put the colors in reverse order, using a negative index. 
tina.backward(76)
for i in range[4]:
    tina.color(colors[3, 2, 1, 0])
    tina.forward(forward)
    tina.left(left)

turtle.exitonclick()                     # Close the window when we click on it