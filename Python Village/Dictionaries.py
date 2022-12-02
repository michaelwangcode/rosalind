#----- PROBLEM -----#

# Given: A string s of length at most 10000 letters.
# Return: The number of occurrences of each word in s, where words are separated by spaces. 
# Words are case-sensitive, and the lines in the output can be in any order.



#----- SOLUTION -----#

# Split the string into an array using the split() function
# Iterate through the array and add the words to a dictionary
# Print the dictionary



# Input: A string of words
s = "We tried list and we tried dicts also we tried Zen"



# This function prints out the occurences of each word in a string
def print_occurrences(s):

  # Create a dictionary to store words
  dict = {}

  # Split the words and store them in a words array
  words = s.split()

  # Add the word to the dictonary or increment its value
  for word in words:
    if not word in dict:
      dict[word] = 1
    else:
      dict[word] += 1

  # Iterate through the dictionary and print each word and its frequency
  for word in dict:
    print(word, dict[word])



# Test the print_occurrences function
print_occurrences(s)
