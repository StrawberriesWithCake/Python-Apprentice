"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk
# Create a window object
window = Tk()
# Hide the window, hint: use the withdraw method
window.withdraw()
# Ask the user for the first number   
first = simpledialog.askfloat("first number", "Input the first number of your choice.")
# Ask the user for the second number
second = simpledialog.askfloat("second number", "Input the second number of your choice.")

Addition = first + second
Subtraction = first - second
Multiplication = first * second
Division = first / second
# Ask the user for the math operation
operation = simpledialog.askstring("Operation Time!", "Pick one of the four operations: Addition, Subtraction, Multiplication, or Division? Please capitalize whichever one you choose.")

# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if operation == "Addition":
   messagebox.showinfo("Your Sum", "Your sum is:" + str(Addition))
elif operation == "Subtraction":
   messagebox.showinfo("Your Difference", "Your difference is:" + str(Subtraction))
elif operation == "Multiplication":
   messagebox.showinfo("Your Product", "Your product is:" + str(Multiplication))
elif operation == "Division":
   messagebox.showinfo("Your Quotient", "Your quotient is" + str(Division))
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()
else:
   messagebox.showerror()
# Keep the window open
window.mainloop
