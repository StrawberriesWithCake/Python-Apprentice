
""" Tash Me with a Twirl
 
Update your Tash Me Click program ( copy your old program here )
so the moustache will twirl when you click on it. 

Hint: See 08a_More Turtle Programs, section 'Click on the Turtle'
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
         
screen.setup(width=1000, height=1000)
screen.bgcolor('white')


set_background_image(screen, 'emoji.png')
#set_turtle_image(klopp, 'moustache2.gif')
def turtle_clicked(t, x, y):

    print('turtle clicked!')
    
    for i in range(0, 360, 20): # Full circle, 20 degrees at a time
        t.tilt(20) # Tilt the turtle 20 degrees

# Connect the turtle to the turtle_clicked function
klopp.onclick(lambda x, y, t = klopp: turtle_clicked(t, x, y))


turtle.done()