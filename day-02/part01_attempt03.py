# Open the input file and read the encrypted strategy guide
with open("input.txt") as f:
    guide = f.readlines()

# Create a dictionary that maps the characters in the strategy guide to the corresponding shape names
shapes = {"A": "Rock", "B": "Paper", "C": "Scissors", "X": "Rock", "Y": "Paper", "Z": "Scissors"}

# Create a function that simulates a single round of the game
def simulate_round(shape1, shape2):
    # Map the input shapes to the corresponding shape names using the dictionary from step 2
    shape1_name = shapes[shape1]
    shape2_name = shapes[shape2]
    
    # Calculate the score for the shape played by the second player (you)
    if shape2_name == "Rock":
        shape2_score = 1
    elif shape2_name == "Paper":
        shape2_score = 2
    else:
        shape2_score = 3
    
    # Calculate the score for the shape played by the first player (the opponent)
    if shape1_name == "Rock":
        shape1_score = 1
    elif shape1_name == "Paper":
        shape1_score = 2
    else:
        shape1_score = 3
    
    # Determine the outcome of the round based on the shapes played by the two players
    if shape1_name == shape2_name:
        # The round is a draw
        outcome_score = 3
    elif (shape2_name == "Rock" and shape1_name == "Scissors") or (shape2_name == "Scissors" and shape1_name == "Paper") or (shape2_name == "Paper" and shape1_name == "Rock"):
        # The second player (you) wins
        outcome_score = 6
    else:
        # The first player (the opponent) wins
        outcome_score = 0
    
    # Return the scores for the shapes played and the outcome of the round
    return shape2_score, outcome_score

# Initialize the total score to 0
total_score = 0

# Iterate over the strategy guide and simulate each round of the game
for line in guide:
    # Split the line into the shapes played by the two players
    shape1, shape2 = line.strip().split()
    
    # Simulate the round and update the total score
    shape2_score, outcome_score = simulate_round(shape1, shape2)
    total_score += shape2_score + outcome_score

# Print the total score
print(total_score)
