# Imports
import sys
import re

######### STEP ONE #########
def step_one():
    cpt = 0
    with open('2022_challenges/day_4/input.txt','r') as file:
        for line in file:

            elf_one_starting_zone = int(re.split(",|-", line.strip())[0])
            elf_one_ending_zone = int(re.split(",|-", line.strip())[1])

            elf_two_starting_zone = int(re.split(",|-", line.strip())[2])
            elf_two_ending_zone = int(re.split(",|-", line.strip())[3])

            if elf_one_starting_zone >= elf_two_starting_zone and elf_one_ending_zone <= elf_two_ending_zone:
                cpt += 1
            elif elf_two_starting_zone >= elf_one_starting_zone and elf_two_ending_zone <= elf_one_ending_zone:          
                cpt += 1
    return cpt

######### STEP TWO #########
def step_two():
    cpt = 0
    with open('2022_challenges/day_4/input.txt','r') as file:
        for line in file:
            elf_one_starting_zone = int(re.split(",|-", line.strip())[0])
            elf_one_ending_zone = int(re.split(",|-", line.strip())[1])

            elf_two_starting_zone = int(re.split(",|-", line.strip())[2])
            elf_two_ending_zone = int(re.split(",|-", line.strip())[3])

            if elf_one_starting_zone <= elf_two_starting_zone <= elf_one_ending_zone:          
                cpt += 1
            elif elf_two_starting_zone <= elf_one_starting_zone <= elf_two_ending_zone:
                cpt += 1
    return cpt

def main():
    print("Result of Part One:", step_one())
    print("Result of Part Two:", step_two())
    pass

if __name__ == "__main__":
    sys.exit(main())