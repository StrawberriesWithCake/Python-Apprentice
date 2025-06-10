"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk
# Create a window object
window = Tk()
# Hide the window, hint: use the withdraw method
window.withdraw()
# Ask the user for the first number   
first = simpledialog.askfloat("The First Number", "Input a number of your choice.")
# Ask the user for the second number
second = simpledialog.askfloat("The Second Number", "Input another number of your choice.")
# Display the sum of the two numbers 
sum = first + second
if sum < 0:
    messagebox.showinfo("You went...backwards?", "Your number:" + str(sum) + "Why did you choose negative numbers? I guess there's nothing wrong in doing so, but, I'm more of a positive person.")
elif sum > 0 and sum < 11:
    messagebox.showinfo("It works.", "Your number:" + str(sum) + "This is a start, but it's too simple. Try thinking of some more creative numbers.")
elif sum > 10 and sum < 1_000:
    messagebox.showinfo("Good job!", "Your number:" + str(sum) + "This is a pretty large number. Now try running this again and think of the BIGGEST. NUMBER. EVER!")
elif sum > 1_000_000:
    messagebox.showinfo("Wow!", "Your number:" + str(sum) + "You're able to think of two numbers that when combined make as large a number as this?! Great!")
# Keep the window open
window.mainloop()