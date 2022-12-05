def solve_puzzle(groups):
  # Initialize a variable to store the sum of the priorities
  sum_of_priorities = 0

  # Iterate over the groups of Elves
  for group in groups:
    # Initialize a set to store the characters that appear in all three rucksacks in the group
    common_chars = set(group[0])

    # Iterate over the rucksacks in the group
    for rucksack in group[1:]:
      # Find the characters that appear in all three rucksacks
      common_chars.intersection_update(rucksack)

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

# Group the lines into groups of three
groups = [lines[i:i+3] for i in range(0, len(lines), 3)]

# Solve the puzzle
result = solve_puzzle(groups)

# Print the result
print(result)
