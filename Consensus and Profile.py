#----- QUESTION -----#

# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

# Return: A consensus string and profile matrix for the collection. 
# (If several possible consensus strings exist, then you may return any one of them.)



#----- SOLUTION -----#

# Create a profile array for each nucleotide (A,G,C,T) equal to the length of a DNA strand

# Iterate through the collection of DNA strings
# For each string, increment the corresponding nucleotide at that position

# Lastly, iterate through all of the profile arrays and add the most common letter to the consensus string



# Input: Array of DNA strings
dna_strings = [
  "ATCCAGCT",
  "GGGCAACT",
  "ATGGATCT",
  "AAGCAACC",
  "TTGGAACT",
  "ATGCCATT",
  "ATGGCACT"
]



# This function takes an array of DNA strings and returns the consensus string
def calculate_consensus(dna_strings):

  # Store the length of a DNA string
  dna_length = len(dna_strings[0])

  # Create an array of 0's for each profile
  profile_A = [0] * dna_length
  profile_C = [0] * dna_length
  profile_G = [0] * dna_length
  profile_T = [0] * dna_length

  # Create a consensus string where bases will be added to
  consensus_string = ""

  # Iterate through the list of strands
  for strand in dna_strings:
    
    # Iterate through each individual strand
    for index, base in enumerate(strand):

      # Depending on the base, increment the corresponding profile at the current index
      if base == "A":
        profile_A[index] += 1
      elif base == "C":
        profile_C[index] += 1
      elif base == "G":
        profile_G[index] += 1
      elif base == "T":
        profile_T[index] += 1

  # Iterate through the length of a dna string
  for index in range(dna_length):

    # Store the number of the base that appears the most
    max_base =  max(profile_A[index], profile_C[index], profile_G[index], profile_T[index])

    # If the base is the most frequent base at that position, add it to the consensus string
    if profile_A[index] == max_base:
      consensus_string += "A"
    elif profile_C[index] == max_base:
      consensus_string += "C"
    elif profile_G[index] == max_base:
      consensus_string += "G"
    elif profile_T[index] == max_base:
      consensus_string += "T"

  # return the consensus string
  return consensus_string



# Test the calculate_consensus function
print(calculate_consensus(dna_strings))
