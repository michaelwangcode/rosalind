#----- PROBLEM -----#

# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.



#----- SOLUTION -----#

# Copy the text to an input.txt file and save all of the lines in an array
# Iterate through the array and save every other line to an output file



# Input: File names for the input file and output file
input_file = "input.txt"
output_file = "output.txt"



# This function saves every other line of a file and saves it to another fule
def save_even_numbered_lines(input_file, output_file):

  #----- Reading File -----#

  # Open the input file, 'r' stands for 'read mode'
  f = open(input_file, "r")

  # Store the lines of the file
  lines = []

  # Iterate through each line in the file and add it to the lines array
  for line in f:
    lines.append(line)


  #----- Writing to File -----#

  # Open the output file, 'w' stands for 'write' which overwrites contents in the current file
  f = open(output_file, "w")

  # Iterate through the lines array
  for i, line in enumerate(lines):

    # Write all of the even numbered lines to the file (1-based numbering)
    if (i % 2 == 1):
      f.write(line)



# Test the save_even_numbered_lines function
save_even_numbered_lines(input_file, output_file)
