# Imports
import sys
import time

#########STEP ONE#########
def step_one() -> int:
    floor = 0
    with open('2015_challenges/day_1/input.txt','r') as file:
        for line in file:
            for char in line:
                if not char :
                    break
                if(char == "("):
                    floor += 1
                elif(char == ")"):
                    floor -= 1
    return floor

#########STEP TWO#########
def step_two() -> int:
    cpt = 0
    floor = 0

    with open('2015_challenges/day_1/input.txt','r') as file:
        for line in file:
            for char in line:
                if(floor < 0):
                    break
                elif(char == "("):
                    floor += 1
                elif(char == ")"):
                    floor -= 1
                cpt += 1
    return cpt

def main() -> None:
    start_time = time.time()
    print("Result of Part One:", step_one())
    print("Result of Part Two:", step_two())
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    sys.exit(main())