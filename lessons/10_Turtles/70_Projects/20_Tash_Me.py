""" Tash Me

Write a program that:
1) Loads an emoji image as the background
2) Make the turtle shape a moustach
3) Move the moustache to the right spont on the emoji

Hint: See 08a_More Turtle Programs, section 'Change the Background Image' and
'Change the Turtle Shape'
"""
import turtle 
klopp = turtle.Turtle()
klopp.penup()
def set_background_image(window, image_name):
    
    from pathlib import Path
    from PIL import Image
    image_dir = Path(__file__).parent.parent/ "images"
    image_path = str(image_dir / image_name)
    image = Image.open(image_path)
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)


def set_turtle_image(turtle, image_name):
    
    from pathlib import Path
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)


def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))
    klopp.goto(x, y)

screen = turtle.Screen()

     # Set the size of the window
         
screen.setup(width=600, height=600)
screen.bgcolor('white')


set_background_image(screen, 'emoji.png')
set_turtle_image(klopp, 'moustache2.gif')


  
screen.onclick(screen_clicked) # Important! Tell Python which function to use when the screen is clicked

turtle.done() # Important! Use `done` not `exitonclick` to keep the window open