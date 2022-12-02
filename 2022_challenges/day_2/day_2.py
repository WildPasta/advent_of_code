# Imports
import sys

def do_i_win(first_roll, second_roll):
    """
    A and X -> Rock
    B and Y -> Paper
    C and Z -> Scissors
    """

    # Tie
    if first_roll == "A" and second_roll == "X": 
        return 1+3
    elif first_roll == "B" and second_roll == "Y":
        return 2+3
    elif first_roll == "C" and second_roll == "Z":
        return 3+3

    # Opponent plays Rock
    elif first_roll == "A":
        if second_roll == "Y":
            return 2+6
        else:
            return 3+0
    # Opponent plays Paper
    elif first_roll == "B":
        if second_roll == "Z":
            return 3+6
        else:
            return 1+0
    # Opponent plays Scissors
    elif first_roll == "C":
            if second_roll == "X":
                return 1+6
            else:
                return 2+0

def what_do_i_need_to_play(opponent_roll, outcome_needed):
    """
    A -> Rock
    B -> Paper
    C -> Scissors
    X -> need to loose
    Y -> need to draw
    Z -> need to win
    """

    # Opponent plays Rock
    if opponent_roll  == "A":
        if outcome_needed == "X":
            return 3+0
        elif outcome_needed == "Y":
            return 1+3
        elif outcome_needed == "Z":
            return 2+6
    # Opponent plays Paper
    elif opponent_roll  == "B":
        if outcome_needed == "X":
            return 1+0
        elif outcome_needed == "Y":
            return 2+3
        elif outcome_needed == "Z":
            return 3+6
    # Opponent plays Scissors
    elif opponent_roll  == "C":
        if outcome_needed == "X":
            return 2+0
        elif outcome_needed == "Y":
            return 3+3
        elif outcome_needed == "Z":
            return 1+6

######### STEP ONE #########
def step_one():
    sum = 0
    with open('2022_challenges/day_2/input.txt','r') as file:
        for line in file:
            opponent_roll = line.strip().split(" ")[0]
            my_roll = line.strip().split(" ")[1]
            sum += do_i_win(opponent_roll, my_roll)
    return sum

######### STEP TWO #########
def step_two():
    sum = 0
    with open('2022_challenges/day_2/input.txt','r') as file:
        for line in file:
            opponent_roll = line.strip().split(" ")[0]
            outcome_needed = line.strip().split(" ")[1]
            sum += what_do_i_need_to_play(opponent_roll, outcome_needed)
    return sum

def main():
    print(step_one())
    print(step_two())

if __name__ == "__main__":
    sys.exit(main())