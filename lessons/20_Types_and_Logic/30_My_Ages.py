
"""
Am I Big Yet?

Ask the user's age then use an if-elif-else statement to 
tell the user what age groups the user is in. The groups are:

0-2: Baby
3-5: Toddler
6-12: Child
13-19: Teen
20-64: Adult
65+: Senior

Except, if the user is the same age as you, print "You are pretty awesome!"

Here is how you ask the user's age in integer format.  The first argument is 
the title of the window, the second is the message to the user.

age = simpledialog.askinteger("Your Age", "How old are you?") 

Or, you could ask the user for a float with simpledialog.askfloat() 

age =  simpledialog.askfloat("Your Age", "How old are you?")


Here is how you show the user a message window. The first parameter is the title of the window, 
the second is the message to show the user.

messagebox.showinfo('What you are', "You are a baby.")

"""
# how to define some functions
#Am I missing anything?
#I feel like I'm doing manything wrong
from tkinter import messagebox, simpledialog, Tk # import required modules
age = 0-100
window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups

# Ask the user's age
age =  simpledialog.askfloat("Your Age", "How old are you?")
# Use if statements to determine the age group
# and create a message
if age > 0 and age < 3:
    messagebox.showinfo("Welcome to Earth! But..", "You're too young to even be here. Is there some trusty adult watching over you right now? You probably can't even respond this dialogue, anyway, let alone read it.")
elif age > 2 and age < 6:
    messagebox.showinfo("Congratulations!", "On moving on from total infancy, which means babyhood. Your parents taught you how to read, right? Can you understand this?")
elif age > 5 and age < 13:
    messagebox.showinfo("I swear,", "You better not be an Ipad kid.")
elif age == 13:
    messagebox.showinfo(":D", "Me too!")
elif age > 13 and age < 20:
    messagebox.showinfo("Ew", "Teenagers these days are REALLY moody. Probably always have been.")
elif age > 19 and age < 65:
    messagebox.showinfo("Wow.", "Being an adult is tough. But hey, atleast you can look forward to retirement.")
else:
    messagebox.showinfo("It's impressive you've managed to hang on this long", "You're really really really really really really old.")
# Show the message to the user



window.mainloop()  # Keeps the window open


# TODO: 
# Try to write your program so you only need to use one messagebox.showinfo() function.
