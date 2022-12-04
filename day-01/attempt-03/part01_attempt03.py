# open the input file and read the contents
with open("input.txt") as f:
    lines = f.readlines()

# initialize variables to keep track of the current Elf and the maximum number of Calories seen so far
current_elf = 0
max_calories = 0
total_calories = 0
elf_with_most_calories = 0

# iterate over the list of strings
for line in lines:
    # if the line is a newline character, we've reached the end of the current Elf's inventory
    if line == "\n":
        # update the current Elf and reset the total number of Calories to 0
        current_elf += 1
        total_calories = 0
    else:
        # convert the string to an integer and add it to the total number of Calories for the current Elf
        total_calories += int(line)
        # if the total number of Calories for the current Elf is greater than the maximum number of Calories seen so far,
        # update the maximum number of Calories and the Elf with the most Calories
        if total_calories > max_calories:
            max_calories = total_calories
            elf_with_most_calories = current_elf

# print the results
print(f"Elf {elf_with_most_calories} is carrying the most Calories ({max_calories}).")
