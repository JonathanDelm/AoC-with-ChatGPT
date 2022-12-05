def solve_puzzle(rucksacks):
  # Initialize a set to store the characters that appear in both halves of each rucksack
  common_chars = set()

  # Iterate over the list of rucksacks
  for rucksack in rucksacks:
    # Split the rucksack into its two halves
    half1 = rucksack[:len(rucksack) // 2]
    half2 = rucksack[len(rucksack) // 2:]

    # Find the characters that appear in both halves of the rucksack
    common_chars.update(set(half1).intersection(set(half2)))

  # Initialize a variable to store the sum of the priorities
  sum_of_priorities = 0

  # Iterate over the common characters
  for char in common_chars:
    # If the character is lowercase, its priority is its ASCII value minus 96
    if char.islower():
      priority = ord(char) - 96
    # If the character is uppercase, its priority is its ASCII value minus 38
    else:
      priority = ord(char) - 38

    # Add the priority to the sum of priorities
    sum_of_priorities += priority

  # Return the sum of priorities
  return sum_of_priorities


# Open the input file
with open("input.txt", "r") as file:
  # Read the lines from the file
  lines = file.readlines()

# Solve the puzzle
result = solve_puzzle(lines)

# Print the result
print(result)
