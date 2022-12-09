# Imports
import sys

def revert_crates(crates):
    """
    Reverting the given lists
    """

    for i in range(len(crates)):
        crates[i] = crates[i][::-1]
    return crates

def init(size, height):
    """
    Initialization on the script
    Opening the inputs
    Retrieving the value of the inputs
    Calling the revert function
    """

    # Creating empty lists
    crates = [[] for i in range(size)]

    with open('2022_challenges/day_5/input.txt','r') as file:
        for _ in range(height):
            line = file.readline()

            # Getting crates structure line per line
            for j in range(0, size, 1):
                if line[(1+j*4)] != " ":
                    crates[j].append(line[(1+j*4)])

    # Revert crate list and return it
    return revert_crates(crates)

def move_step_one(move_, from_, to_, crates):
    """
    Move crate only one by one
    """

    for _ in range((move_)):
        popped = crates[from_ - 1].pop()
        crates[to_ - 1].append(popped)
    return crates

def move_step_two(move_, from_, to_, crates):
    """
    Move several crates at once
    """

    to_be_moved = crates[from_ - 1][-move_:]
    for i in range(len(to_be_moved)):
        crates[to_ - 1].append(to_be_moved[i])
    crates[from_ - 1] = crates[from_ -1][:-move_]
    return crates

def read_move(size, crates, func):
    """
    Reading move list
    Calling move function according to the step
    """

    res = ""

    with open('2022_challenges/day_5/input.txt','r') as file:
        for _ in range(size+1):
            file, next(file)
        for line in file:
            move_ = int(line.strip().split(" ")[1])
            from_ = int(line.strip().split(" ")[3])
            to_ = int(line.strip().split(" ")[5])
            crates = func(move_, from_, to_, crates)

    for i in range(len(crates)):
        res += crates[i][-1]
    return res


######### STEP ONE #########
def step_one(size, height):

    crates = init(size, height)
    res = read_move(size, crates, move_step_one)
    return res

######### STEP TWO #########
def step_two(size, height):
    
    crates = init(size, height)
    res = read_move(size, crates, move_step_two)
    return res

def main():
    # Manually giving size and height of the crates structure
    size = 9
    height = 8

    print("Result of Part One:", step_one(size, height))
    print("Result of Part Two:", step_two(size, height))
    pass

if __name__ == "__main__":
    sys.exit(main())