""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle
from pathlib import Path
def set_turtle_image(turtle, image_name):
    
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)
    turtle.
image_name = "leaguebot_bolt.gif"
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()

turtle.setup(width=10, height=10)
turtle.pencolor('blue')

set_turtle_image(t, "leaguebot_bolt.gif")

for i in range(6):
    turtle.forward(55)
    turtle.left(60)
turtle.exitonclick