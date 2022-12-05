# Imports
import re
import sys

def revert_crates(crates):
    for i in range(len(crates)):
        crates[i] = crates[i][::-1]
    return crates

def init(size, height):
    crates = [[] for i in range(size)]
    cur_crate = list()

    with open('2022_challenges/day_5/input.txt','r') as file:
        for i in range(height):
            line = file.readline()     

            for j in range(0, size, 1):
                crates[j].append(line[(1+j*4)])
            cur_crate = list()

    crates = revert_crates(crates)
    return crates

def read_move(size, crates):
    regex = "(\d+)"

    with open('2022_challenges/day_5/input.txt','r') as file:
        for i in range(size+2):
            file, next(file)
        for line in file:
            regex_res = re.findall(regex, line.strip())
            move_ = int(regex_res[0])
            from_ = int(regex_res[1])
            to_ = int(regex_res[2])
            print(line.strip())
            crates = move(move_, from_, to_, crates)
    print(crates)

def move(move_, from_, to_, crates):

    for i in range(len(crates)):
        for j in range(len(crates[i])):
            if crates[i-1][-1] == " ":
                crates[i-1].pop()
    # print("Popped out:", crates)

    for i in range((move_)):
        crates[to_ - 1].append(crates[from_ - 1][-1])
        crates[from_ - 1].pop()
        print("List", crates)
    return crates

######### STEP ONE #########
def step_one(size, height):

    crates = init(size, height)
    print(crates)
    read_move(size, crates)
    return 0

######### STEP TWO #########
def step_two():
    with open('2022_challenges/day_5/input.txt','r') as file:
        for line in file:
            pass
    return 0

def main():
    # size = 3
    # height = 3
    size = 9
    height = 8
    
    print("Result of Part One:", step_one(size, height))
    #print("Result of Part Two:", step_two(size))
    pass

if __name__ == "__main__":
    sys.exit(main())