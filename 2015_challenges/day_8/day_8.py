# Imports
import sys
import time

######### STEP ONE #########
def step_one() -> int:
    code_total = 0
    memory_total = 0
    # Read instructions
    with open('2015_challenges/day_8/input.txt') as f:
        for line in f:
            code_total += len(line.strip())
            memory_total += len(eval(line.strip()))
    return code_total - memory_total

######### STEP TWO #########
def step_two() -> int:
    code_length = 0 
    encoded_length = 0
    with open('2015_challenges/day_8/input.txt') as f:
        for line in f:
            line = line.strip()
            code_length += len(line)

            encoded_length += get_encoded_length(line)
    return encoded_length - code_length

def get_encoded_length(line):
    # Start with two for the opening and closing quotes
    encoded_length = 2

    for c in line:
        if c == "\\" or c == "\"":
            encoded_length += 2
        else:
            encoded_length += 1
    return encoded_length

def main() -> None:
    start_time = time.time()
    print("Result of Part One:", step_one())
    print("Result of Part Two:", step_two())
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    sys.exit(main())
