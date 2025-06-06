"""Flaming Ninja Star

This program already works; run it to see what it does. 
Then change it to make it draw a different pattern. 
"""

import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF)) 
maroon = "#700d02"
pumpkin = "#c24e10"
highlite = "#f5e74e"
fruita = "#b01c48"
colors = [maroon, pumpkin, highlite, fruita]


def getNextColor(i):
    return colors[i % len(colors)]

turtle.setup(600,600,0,0)               # Set the size of the window
window = turtle.Screen()

baseSize = 200  # the size of the black part of the star
flameSize = 130  # the length of the flaming arms

t = turtle.Turtle() 

t.shape("turtle") 

t.width(2) 

t.speed(0) 

for i in range(25):
    t.pencolor(getNextColor(i))

    t.fillcolor(getNextColor(i)) 
   
    t.begin_fill()

    t.forward(64) 

    t.left(40) 

    t.forward(flameSize) 

    t.right(170) 

    t.forward(flameSize) 

    t.right(62) 

    t.forward(baseSize) 

    t.end_fill()

t.hideturtle() 

turtle.done() 
