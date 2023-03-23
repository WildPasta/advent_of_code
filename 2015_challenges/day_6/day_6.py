# Imports
import re
import sys
import time
from typing import List

def apply_instruction(grid: List[List[bool]], instruction: str) -> None:
    """
    Applies an instruction to the grid
    """
    # Extracting the action
    regex_action = re.compile(r"turn on|toggle|turn off")
    action = regex_action.search(instruction).group()

    # Extracting the start and end positions
    regex_position = re.compile(r"\d+,\d+")
    start, end = regex_position.findall(instruction)
    # end = regex_position.findall(instruction)[1]

    # Converting to tuples for better handling
    start_tuple = tuple(map(int, start.split(',')))
    end_tuple = tuple(map(int, end.split(',')))

    for i in range(start_tuple[0], end_tuple[0] + 1):
        for j in range(start_tuple[1], end_tuple[1] + 1):
            if action == 'toggle':
                grid[i][j] = not grid[i][j]
            elif action == 'turn on':
                grid[i][j] = True
            elif action == 'turn off':
                grid[i][j] = False

def apply_brightness(grid: List[List[int]], instruction: str) -> None:
    """
    Applies an instruction to the grid (brightness version)
    """
    # Extracting the action
    regex_action = re.compile(r"turn on|toggle|turn off")
    action = regex_action.search(instruction).group()

    # Extracting the start and end positions
    regex_position = re.compile(r"\d+,\d+")
    start, end = regex_position.findall(instruction)
    # end = regex_position.findall(instruction)[1]

    # Converting to tuples for better handling
    start_tuple = tuple(map(int, start.split(',')))
    end_tuple = tuple(map(int, end.split(',')))

    for i in range(start_tuple[0], end_tuple[0] + 1):
        for j in range(start_tuple[1], end_tuple[1] + 1):
            if action == 'toggle':
                grid[i][j] += 2
            elif action == 'turn on':
                grid[i][j] += 1
            elif action == 'turn off':
                grid[i][j] = max(0, grid[i][j] - 1)


######### STEP ONE #########
def step_one() -> int:
    # Initialize the grid with all lights turned off
    grid = [[False] * 1000 for _ in range(1000)]

    # Read instructions
    with open('2015_challenges/day_6/input.txt') as f:
        for line in f:
            apply_instruction(grid, line.strip())

    # Count the number of lights that are turned on
    num_lights_on = sum(sum(row) for row in grid)
    return num_lights_on

######### STEP TWO #########
def step_two() -> int:
    # Initialize the grid with all lights turned off
    grid = [[0] * 1000 for _ in range(1000)]

    # Read instructions
    with open('2015_challenges/day_6/input.txt') as f:
        for line in f:
            apply_brightness(grid, line.strip())

    # Count the number of lights that are turned on
    total_brightness = sum(sum(row) for row in grid)
    return total_brightness

def main() -> None:
    start_time = time.time()
    print("Result of Part One:", step_one())
    print("Result of Part Two:", step_two())
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    sys.exit(main())
