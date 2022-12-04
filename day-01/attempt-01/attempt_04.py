# Open the input file and read the lines
with open("input.txt") as input_file:
    lines = input_file.readlines()

# Initialize variables to keep track of the Elf carrying the most Calories
elf = 0
most_calories_elf = 0
most_calories = 0
elf_calories = [0] * 10  # assume there are at most 10 Elves

# Loop over the lines in the input
for line in lines:
    # If the line is empty, we've reached the end of one Elf's inventory
    # and need to check if the Elf carrying the most Calories has changed
    if line == "\n":
        elf += 1
        continue
    calories = int(line)
    elf_calories[elf] += calories
    if elf_calories[elf] > most_calories:
        most_calories_elf = elf
        most_calories = elf_calories[elf]

# Print out the result
print(f"Elf {most_calories_elf} is carrying the most Calories: {most_calories}")
