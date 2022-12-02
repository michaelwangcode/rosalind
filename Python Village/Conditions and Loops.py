#----- PROBLEM -----#

# Given: Two positive integers a and b (a < b < 10000).
# Return: The sum of all odd integers from a through b, inclusively.



#----- SOLUTION -----#

# Use a for loop to iterate from a to b and add all the odd numbers.



# Input: Two integers
a = 100
b = 200



# This returns the sum of all odd numbers between two integers
def sum_of_odd_numbers(a, b):

  # Keep track of the sum
  sum = 0

  # Iterate from a to b inclusive
  for i in range(a, b):

    # If i is odd,
    if (i % 2 == 1):

      # Add it to the sum
      sum += i

  # Return the sum
  return sum



# Test the sum_of_odd_numbers function
print(sum_of_odd_numbers(a, b))
