from typing import List, Tuple

def count_containment_pairs(pairs: List[Tuple[int, int]]) -> int:
    # Initialize a counter for the number of containment pairs
    count = 0

    # Iterate over the pairs of sections
    for pair1 in pairs:
        for pair2 in pairs:
            # Check if pair1 fully contains pair2
            if pair1[0] <= pair2[0] and pair1[1] >= pair2[1]:
                # Increment the counter
                count += 1

    # Return the number of containment pairs
    return count

# Read the input data
with open('input.txt') as file:
    input_data = file.read()

# Parse the input
pairs = [tuple(map(int, pair.split(','))) for pair in input_data.splitlines()]

# Count the number of containment pairs
result = count_containment_pairs(pairs)

# Print the result
print(result)