# Read in the datastream buffer from the input file
with open("input.txt", "r") as file:
    buffer = file.read()

# Keep track of the number of characters processed
chars_processed = 0

# Keep track of the last 14 characters that have been processed
last_fourteen = []

# Iterate through the characters in the buffer
for c in buffer:
    # If we have processed at least 14 characters, check if they are all different
    if chars_processed >= 14 and len(set(last_fourteen)) == 14:
        # If they are, print the number of characters processed and exit the program
        print(chars_processed)
        break

    # Increment the number of characters processed
    chars_processed += 1

    # Add the current character to the list of last 14 characters
    last_fourteen.append(c)

    # If the list of last 14 characters is longer than 14, remove the first character
    if len(last_fourteen) > 14:
        last_fourteen = last_fourteen[1:]
