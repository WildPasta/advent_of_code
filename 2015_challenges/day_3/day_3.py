# Imports
import sys
import time

#########STEP ONE#########
def step_one() -> int:
    x = 0
    y = 0
    visited_location = []
    
    with open('2015_challenges/day_3/input.txt','r') as file:
        current_location = [x,y]
        visited_location.append(current_location)
    
        for line in file:
            string = line.rstrip()
    
            for i in range(len(string)):
                if(string[i] == "^"):
                    # print("UP")
                    y += 1
                elif(string[i] == "<"):
                    # print("LEFT")
                    x -= 1
                elif(string[i] == ">"):
                    # print("RIGHT")
                    x +=1
                elif(string[i] == "v"):
                    # print("DOWN")
                    y -= 1
    
                current_location = [x,y]
                if(current_location not in visited_location):
                    visited_location.append(current_location)
                else:
                    pass
    # print(visited_location)
    return len(visited_location)

#########STEP TWO#########
def step_two() -> int:
    x = 0
    y = 0
    a = 0
    b = 0
    robot_current_location = []
    visited_location = []

    with open('2015_challenges/day_3/input.txt','r') as file:
        santa_current_location = [x,y]
        robot_current_location = [a,b]
        visited_location.append(santa_current_location)

        for line in file:
            string = line.rstrip()
            santa_steps = string[::2]
            robot_steps = string[1::2]

            for i in range(len(santa_steps)):
                if(santa_steps[i] == "^"):
                    # print("UP")
                    y += 1
                elif(santa_steps[i] == "<"):
                    # print("LEFT")
                    x -= 1
                elif(santa_steps[i] == "v"):
                    # print("DOWN")
                    y -= 1
                elif(santa_steps[i] == ">"):
                    # print("RIGHT")
                    x +=1

                santa_current_location = [x,y]
                if(santa_current_location not in visited_location):
                    visited_location.append(santa_current_location)
                else:
                    pass

            for i in range(len(robot_steps)):
                if(robot_steps[i] == "^"):
                    # print("UP")
                    b += 1
                elif(robot_steps[i] == "<"):
                    # print("LEFT")
                    a -= 1
                elif(robot_steps[i] == "v"):
                    # print("DOWN")
                    b -= 1
                elif(robot_steps[i] == ">"):
                    # print("RIGHT")
                    a +=1
                robot_current_location = [a,b]
                if(robot_current_location not in visited_location):
                    visited_location.append(robot_current_location)

    # print(visited_location)
    return len(visited_location)

def main() -> None:
    start_time = time.time()
    print("Result of Part One:", step_one())
    print("Result of Part Two:", step_two())
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    sys.exit(main())