# Parse the input
with open('input.txt') as f:
    lines = f.readlines()

# Initialize the stacks of crates
stacks = [[c for c in line.strip()] for line in lines[:-1]]

# Parse the instructions for rearranging the crates
instructions = [line.strip().split() for line in lines[-1:]]

# Simulate the rearrangement of the crates
for instruction in instructions:
    # Parse the instruction
    num_crates = int(instruction[0])
    from_stack = int(instruction[3])
    to_stack = int(instruction[5])

    # Move the crates from one stack to another
    moved_crates = stacks[from_stack - 1][-num_crates:]
    stacks[from_stack - 1] = stacks[from_stack - 1][:-num_crates]
    stacks[to_stack - 1] += moved_crates

# Print the top crate of each stack
for stack in stacks:
    print(stack[-1])
