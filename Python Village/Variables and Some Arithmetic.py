#----- PROBLEM -----#

# Given: Two positive integers a and b, each less than 1000.
# Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.
# Example: Given 3 and 5, return 34 (3^2 + 5^2 = 34)



#----- SOLUTION -----#

# Create a function that takes two integers and returns their squares added together
# (Note: To run a Python file in VSCode, click the "▷" run button at the top right)



# Input: Two integers
a = 953
b = 923



# This function takes two integers and returns the sum of their squares
def sum_of_squares(a, b):
  return a*a + b*b



# Test the sum_of_squares function
print(sum_of_squares(a, b))
