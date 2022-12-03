# Imports
import sys

def get_priority(letter):
    """
    Get the priority of the letter using ASCII table
    Priority of 'a' should be 1
    Priority of 'Z' should be 52
    """

    # Offset to 1 so 'a' returns 1 and not 0
    offset = 1
    if letter.isupper():
        return ord(letter) - ord('A') + 26 + offset 
    return ord(letter) - ord('a') + offset

######### STEP ONE #########
def step_one():
    sum = 0

    with open('2022_challenges/day_3/input.txt','r') as file:
        for line in file:
            string = line.strip()
            first_half = string[:len(string)//2]
            second_half = string[len(string)//2:]
            
            for i in range(len(first_half)):
                if first_half[i] in second_half:
                    sum += get_priority(first_half[i])
                    break
    return sum

######### STEP TWO #########
def step_two():
    elf_group = list()
    sum = 0

    with open('2022_challenges/day_3/input.txt','r') as file:
        for line in file:
            string = line.strip()
            elf_group.append(string)

            if len(elf_group) == 3:
                for i in range(len(elf_group[0])):
                    if elf_group[0][i] in elf_group[1] and elf_group[0][i] in elf_group[2]:
                        sum += get_priority(elf_group[0][i])
                        break
                elf_group = list()
    return sum

def main():
    print(step_one())
    print(step_two())
    pass

if __name__ == "__main__":
    sys.exit(main())