#----- PROBLEM -----#

# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
# k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele 
# (and thus displaying the dominant phenotype). Assume that any two organisms can mate.



#----- SOLUTION -----#

# k: number of AA organisms
# m: number of Aa organisms
# n: number of aa organisms

# Imagine there are two of each AA, Aa and aa organism

# Calculate the probability of each combination:
# AAxAA, AAxAa, AAxaa; AaxAA, AaxAa, Aaxaa; aaxAA, aaxAa, aaxaa
# This can be visualized easier using 3 tree diagrams, one for each type of parent (AA, Aa, aa)

# When the first parent is AA, the offspring ratios are as follows:

# AAxAA -> 4AA            1/5 chance of mating
# AAxAa -> 2AA, 2Aa       2/5 chance of mating
# AAxaa -> 4Aa            2/5 chance of mating

# When the first parent is Aa, the offspring ratios are as follows:

# AaxAA -> 2AA, 2Aa       2/5 chance of mating
# AaxAa -> 1AA, 2Aa, 1aa  1/5 chance of mating      1/4 chance of aa
# Aaxaa -> 2Aa, 2aa       2/5 chance of mating      1/2 chance of aa

# When the first parent is aa, the offspring ratios are as follows:

# aaxAA -> 4Aa            2/5 chance of mating
# aaxAa -> 2Aa, 2aa       2/5 chance of mating      1/2 chance of aa
# aaxaa -> 4aa            1/5 chance of mating      1/1 chance of aa

# To calculate the percentage of offspring with at least one A allele,
# it's easier to calculate the number of genes with no A allele (aa genes) and subtract it from 1 (100%).

# We can do this by multiplying the mating chance with the aa chance and add them up, before subtracting from 1
# Probability = 1.0 - AaxAa * 0.25 + Aaxaa * 0.5 + aaxAa * 0.5 + aaxaa

# Lastly, the formula can be generalized by replacing 5 with (total-1) in the denominator
# The numerator is either k, m or n for parents with different genes or k-1, m-1 or n-1 in the numerator
# Now, we can return the percentage of AA or Aa organisms for any values of k, m and n



# Input: Three positive integers k, m and n
k = 2
m = 2
n = 2



# This function returns the probability that two random mating organisms will produce an offspring with a dominant allele (A)
def calculate_probability(k, m, n):

  # The total number of organisms
  total = k + m + n

  # Percentage of each parent
  percentage_of_AA = k / total
  percentage_of_Aa = m / total
  percentage_of_aa = n / total

  # Probabilities for each parent combination           # Offspring Produced

  # First parent is AA: (second parent is AA, Aa or aa)
  AAxAA = percentage_of_AA * ((k - 1) / (total - 1))    # 4AA
  AAxAa = percentage_of_AA * (m / (total - 1))          # 2AA, 2Aa
  AAxaa = percentage_of_AA * (n / (total - 1))          # 4Aa
  
  # First parent is Aa: (second parent is AA, Aa or aa)
  AaxAA = percentage_of_Aa * (k / (total - 1))          # 2AA, 2Aa
  AaxAa = percentage_of_Aa * ((m - 1)/ (total - 1))     # 1AA, 2Aa, 1aa     - Will produce 1/4 aa offspring
  Aaxaa = percentage_of_Aa * (n / (total - 1))          # 2Aa, 2aa          - Will produce 2/4 aa offspring

  # First parent is aa: (second parent is AA, Aa or aa)
  aaxAA = percentage_of_aa * (k / (total - 1))          # 4Aa
  aaxAa = percentage_of_aa * (m / (total - 1))          # 2Aa, 2aa          - Will produce 2/4 aa offspring
  aaxaa = percentage_of_aa * ((n - 1) / (total - 1))    # 4aa               - Will produce 4/4 aa offspring

  # Total percentage of aa offspring
  total_percentage_aa_offspring = AaxAa * 0.25 + Aaxaa * 0.5 + aaxAa * 0.5 + aaxaa

  # Return 100% minus the number of aa offspring to get the number of AA and Aa offspring
  return 1.0 - total_percentage_aa_offspring



# Test the calculate_probability function
print(calculate_probability(k, m, n))

