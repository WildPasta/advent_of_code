# Imports
import sys

def is_dupe(string):
    """
    Check if there is any character twice in the given string
    Return True if there is a dupe
    Return False if there is none
    """

    for i in range(len(string)):
        if string.count(string[i]) > 1:
            cpt = string.count(string[i])
            return True
    return False

######### STEP ONE #########
def step_one():
    with open('2022_challenges/day_6/input.txt','r') as file:
        for line in file:
            string = line.strip()
            for i in range(0, len(string), 1):
                if not is_dupe(string[i:i+4]):
                    res = i+4
                    break
    return res

######### STEP TWO #########
def step_two():
    with open('2022_challenges/day_6/input.txt','r') as file:
        for line in file:
            string = line.strip()
            for i in range(0, len(string), 1):
                if not is_dupe(string[i:i+14]):
                    res = i+14
                    break
    return res

def main():
    print("Result of Part One:", step_one())
    print("Result of Part Two:", step_two())

if __name__ == "__main__":
    sys.exit(main())