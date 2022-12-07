def read_initial_stacks(lines):
    # Initialize the stacks of crates
    stacks = []

    # Read the lines until the line that contains a space and a number as the first 2 characters
    for line in lines:
        if line[0] == ' ' and line[1].isdigit():
            break

        # Divide the line into parts of 4 characters and 3 for the last one
        parts = [line[i:i+4] for i in range(0, len(line), 4)]

        # Read the second character for each part
        crates = [part[1] for part in parts]

        # Put each of the read characters into the correct list
        for i in range(len(crates)):
            if len(stacks) < i + 1:
                stacks.append([])
            stacks[i].append(crates[i])

    return stacks

def read_instructions(lines):
    # Parse the instructions for rearranging the crates
    instructions = []
    in_instructions = False
    for line in lines:
        if line == '\n':
            in_instructions = True
            continue
        if in_instructions:
            instructions.append(line.strip().split())

    return instructions

def rearrange(stacks, instructions):
    # Remove spaces from the stacks
    stacks = [[crate for crate in stack if crate != ' '] for stack in stacks]

    for instruction in instructions:
        # Parse the instruction
        num_crates = int(instruction[1])
        from_stack = int(instruction[3])
        to_stack = int(instruction[5])

        # Move the specified number of crates from the source stack to the destination stack,
        # preserving their order
        crates = stacks[from_stack - 1][:num_crates]
        stacks[from_stack - 1] = stacks[from_stack - 1][num_crates:]
        stacks[to_stack - 1] = crates + stacks[to_stack - 1]

    return stacks

# Parse the input
with open('input.txt') as f:
    lines = f.readlines()

# Read the initial stacks of crates
stacks = read_initial_stacks(lines)

# Parse the instructions for rearranging the crates
instructions = read_instructions(lines)

# Simulate the rearrangement of the crates
stacks = rearrange(stacks, instructions)

# Print the first item from every list in stacks as one string
print(''.join([stack[0] for stack in stacks]))
