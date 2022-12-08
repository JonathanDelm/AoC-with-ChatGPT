# Read in the datastream buffer from the input file
with open("input.txt", "r") as file:
    buffer = file.read()

# Keep track of the number of characters processed
chars_processed = 0

# Keep track of the last four characters that have been processed
last_four = []

# Iterate through the characters in the buffer
for c in buffer:
    # If we have processed at least four characters, check if they are all different
    if chars_processed >= 4 and len(set(last_four)) == 4:
        # If they are, print the number of characters processed and exit the program
        print(chars_processed - 3)
        break

    # Increment the number of characters processed
    chars_processed += 1

    # Add the current character to the list of last four characters
    last_four.append(c)

    # If the list of last four characters is longer than four, remove the first character
    if len(last_four) > 4:
        last_four = last_four[1:]
