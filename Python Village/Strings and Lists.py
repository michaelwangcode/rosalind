#----- PROBLEM -----#

# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. 
# In other words, we should include elements s[b] and s[d] in our slice.



#----- SOLUTION -----#

# In python, we can use square brackets to return a slice of a string
# If s = "Hello, World!, then s[7:12] returns "World"

# Write a function that takes a string and returns slices from [a:b+1] and [c:d+1]



# Input: A string
s = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."
a = 22 
b = 27
c = 97
d = 102



# This function takes a string and returns the string slices seperated by a space
def slice_string(s, a, b, c, d):
  slice1 = s[a:b+1]
  slice2 = s[c:d+1]
  return slice1 + " " + slice2



# Test the slice_string function
print(slice_string(s, a, b, c, d))
