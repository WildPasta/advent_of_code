# Imports
import sys
import time

#########STEP ONE#########
def step_one() -> int:
    needed_paper = 0
    
    with open('2015_challenges/day_2/input.txt','r') as file:
        for line in file:
            string = line.rstrip()
            dimensions = string.split("x")
    
            length = int(dimensions[0])
            width = int(dimensions[1])
            height = int(dimensions[2])
    
            slack = [length*width,width*height,height*length]
            needed_paper += 2*length*width + 2*width*height + 2*height*length + sorted(slack)[0]
    return needed_paper


#########STEP TWO#########
def step_two() -> int:
    needed_paper = 0
    needed_ribbon = 0

    with open('2015_challenges/day_2/input.txt','r') as file:
        for line in file:
            string = line.rstrip()
            dimensions = string.split("x")

            length = int(dimensions[0])
            width = int(dimensions[1])
            height = int(dimensions[2])
            dimensions = [length,width,height]

            slack = [length*width,width*height,height*length]
            needed_paper += 2*length*width + 2*width*height + 2*height*length + sorted(slack)[0]
            needed_ribbon += 2*sorted(dimensions)[0] + 2*sorted(dimensions)[1] + length*width*height

    return needed_ribbon

def main() -> None:
    start_time = time.time()
    print("Result of Part One:", step_one())
    print("Result of Part Two:", step_two())
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    sys.exit(main())