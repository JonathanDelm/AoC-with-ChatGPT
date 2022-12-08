# Read in the datastream buffer from the input file
with open("input.txt", "r") as file:
    buffer = file.read()

# Keep track of the number of characters processed
chars_processed = 0

# Iterate through the characters in the buffer
for c in buffer:
    # Increment the number of characters processed
    chars_processed += 1

    # Check if the last four characters in the buffer are all different
    if len(set(buffer[-4:])) == 4:
        # If they are, print the number of characters processed and exit the program
        print(chars_processed)
        break
