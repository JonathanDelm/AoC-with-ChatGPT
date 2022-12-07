# Parse the input to get the initial stack configuration and the rearrangement procedure
with open("input.txt") as f:
    lines = f.read().strip().split("\n")
    initial_stacks = [list(line) for line in lines[:3]]
    moves_to_apply = [line.split() for line in lines[3:]]

# Create a function to apply a move to the stack configuration
def move(stacks, move):
    # Parse the move
    source, _, quantity, _, _, _, _, _, _, target = move

    # Get the source stack and the top `quantity` items in it
    source_stack = stacks[int(source) - 1]
    moved_items = [source_stack.pop() for _ in range(int(quantity))]

    # Add the moved items to the top of the target stack
    target_stack = stacks[int(target) - 1]
    target_stack[:0] = moved_items

# Apply all the moves to the initial stack configuration
for move in moves_to_apply:
    move(initial_stacks, move)

# Print the top item in each stack
for stack in initial_stacks:
    print(stack[0])
