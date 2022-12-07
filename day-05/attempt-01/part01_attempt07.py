# Parse the input to get the initial stack configuration and the rearrangement procedure
with open("input.txt") as f:
    lines = f.read().split("\n")

    # Determine the number of stacks
    numbers_line = [line for line in lines if line.replace(' ', '').isdigit()][0]
    n_stacks = sum(ch.isdigit() for ch in numbers_line)

    # Determine the maximum height of the stacks
    max_height = lines.index(numbers_line)

    # Parse the initial stack configuration
    initial_stacks = []
    for i in range(n_stacks):
        stack = []
        for j in range(max_height):
            line = lines[j]
            stack.append(line[line.index('[') + 1 + i*2:line.index(']') + i*2])
        initial_stacks.append(stack)


    # Parse the moves
    moves = [line.split() for line in lines[3 + max_height:]]

# Create a function to apply a move to the stack configuration
def apply_move(stacks, move):
    # Parse the move
    _, quantity, _, _, _, _, source, _, _, _, target = move

    # Get the source stack and the top `quantity` items in it
    source_stack = stacks[int(source) - 1]
    moved_items = [source_stack.pop() for _ in range(int(quantity))]

    # Add the moved items to the top of the target stack
    target_stack = stacks[int(target) - 1]
    target_stack[:0] = moved_items

# Apply all the moves to the initial stack configuration
for move in moves:
    apply_move(initial_stacks, move)

# Print the top item in each stack
for stack in initial_stacks:
    print(stack[0])
