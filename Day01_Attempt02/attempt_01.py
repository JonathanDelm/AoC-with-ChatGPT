# Read the input data from the file
with open('input.txt', 'r') as file:
    data = file.read()

# Split the input data into lines and filter out empty lines
lines = [line for line in data.split('\n') if line]

# Keep track of the current Elf number and the maximum number of calories seen so far
current_elf = 1
max_calories = 0

# Loop over the lines in the input data
for line in lines:
    # If the line is empty, this marks the end of the current Elf's inventory
    # and we move on to the next Elf
    if not line:
        current_elf += 1
        continue

    # Otherwise, we add the number of calories in the current line to the
    # total number of calories for the current Elf
    calories = int(line)
    max_calories = max(max_calories, calories)

# Print the Elf number and the maximum number of calories
print(f'Elf {current_elf} has the most calories with a total of {max_calories}')
