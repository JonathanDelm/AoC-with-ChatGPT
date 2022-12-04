# open the input file and read the contents
with open("input.txt") as f:
    lines = f.readlines()

# initialize variables to keep track of the current Elf and the maximum number of Calories seen so far
current_elf = 0
total_calories = 0
elf_with_most_calories = [0, 0, 0]
calories_for_elf_with_most_calories = [0, 0, 0]

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
        # update the list of Elves with the most Calories by adding the current Elf to the list and removing the Elf
        # with the fewest number of Calories from the list
        if total_calories > min(calories_for_elf_with_most_calories):
            elf_with_most_calories.remove(min(elf_with_most_calories))
            calories_for_elf_with_most_calories.remove(min(calories_for_elf_with_most_calories))
            elf_with_most_calories.append(current_elf)
            calories_for_elf_with_most_calories.append(total_calories)

# print the results
print(f"The top three Elves carrying the most Calories are Elves {elf_with_most_calories} with a total of {sum(calories_for_elf_with_most_calories)} Calories.")
