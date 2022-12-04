with open("input.txt") as f:
    guide = f.readlines()

shapes = {"A": "Rock", "B": "Paper", "C": "Scissors"}

def simulate_round(shape1, shape2_outcome):
    shape1_name = shapes[shape1]
    
    if shape2_outcome == "X":
        if shape1_name == "Rock":
            shape2_name = "Scissors"
        elif shape1_name == "Paper":
            shape2_name = "Rock"
        else:
            shape2_name = "Paper"
    elif shape2_outcome == "Y":
        shape2_name = shape1_name
    else:
        if shape1_name == "Rock":
            shape2_name = "Paper"
        elif shape1_name == "Paper":
            shape2_name = "Scissors"
        else:
            shape2_name = "Rock"
    
    if shape2_name == "Rock":
        shape2_score = 1
    elif shape2_name == "Paper":
        shape2_score = 2
    else:
        shape2_score = 3
    
    if shape2_outcome == "X":
        return shape2_score
    elif shape2_outcome == "Y":
        return shape2_score + 3
    else:
        return shape2_score + 6

total_score = 0

for round in guide:
    shape1, shape2_outcome = round.strip().split()
    total_score += simulate_round(shape1, shape2_outcome)

# Print the total score for the tournament
print(total_score)
