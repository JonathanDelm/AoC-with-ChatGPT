from typing import List, Tuple

def parse_input(input_string: str) -> List[List[Tuple[int, int]]]:
    # Split the input string into lines
    lines = input_string.splitlines()

    # Create a list of pairs of sections
    pairs = []

    # Iterate over the lines
    for line in lines:
        # Split the line into pairs of integers
        pair = [tuple(map(int, pair.split('-'))) for pair in line.split(',')]
        # Add the pair to the list of pairs
        pairs.append(pair)

    # Return the list of pairs
    return pairs

def count_overlapping_pairs(pairs: List[List[Tuple[int, int]]]) -> int:
    # Initialize a counter for the number of overlapping pairs
    count = 0

    # Iterate over the pairs of Elves
    for pair in pairs:
        # Check if the ranges in the pair overlap
        if (pair[0][0] <= pair[1][1] and pair[0][0] >= pair[1][0]) or (pair[1][0] <= pair[0][1] and pair[1][0] >= pair[0][0]):
            # Increment the counter
            count += 1

    # Return the number of overlapping pairs
    return count


# Read the input data
with open('input.txt') as file:
    input_data = file.read()

# Parse the input
pairs = parse_input(input_data)

# Count the number of overlapping pairs
result = count_overlapping_pairs(pairs)

# Print the result
print(result)
