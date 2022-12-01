# Imports
import sys
import pathlib

######### STEP ONE #########
def step_one(bag):
    """
    Returns the content of the elves' bag
    """

    calories = 0
    elf_id = 1

    with open("2022_challenges/day_1/input.txt","r") as file:
        for line in file:
            if line.strip() == "":
                elf_id += 1
                calories = 0
            else:
                calories += int(line.strip())
                bag[elf_id] = calories
    return bag

######### STEP TWO #########
def step_two(bag):
    """
    Returns the total calories of the top 3 bags
    """

    calories = 0

    values = sorted(bag, key = (bag.get), reverse = True)[:3]
    for i in range(len(values)):
        calories += bag[values[i]]
    return calories

def main():
    bag = dict()
    bag = step_one(bag)
    print("Most calories carried by an elf:", max(bag.values()))

    print("The 3 biggest bags contains", step_two(bag), "calories in total")

if __name__ == "__main__":
    sys.exit(main())