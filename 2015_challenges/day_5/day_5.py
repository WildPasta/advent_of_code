# Imports
import sys
import time

#########STEP ONE#########
def step_one() -> int:
    with open('day_5/input.txt','r') as file:
        count_isok = 0
        for line in file:
            if vowel_count(line.strip()) and twin(line.strip()) > 0 and forbidden(line.strip()):
                count_isok += 1
    return count_isok

def vowel_count(line: str) -> bool:
    """
    Return True if the line contains at least 3 vowels
    """
    vowels = ["a","e","i","o","u"]
    cpt = 0
    for i in range(len(vowels)):
        cpt += line.count(vowels[i])
    if cpt >= 3:
        return True
    else:
        return False

def twin(line: str) -> int:
    """
    Return the number of times a letter is repeated twice in a row
    """
    counter = 0
    for i in range(len(line) - 1):
        if line[i] == line[i+1]:
            counter += 1
    return counter

def forbidden(string):
    """
    Return True if the string doesn't contain any of the forbidden strings
    """
    unauthorized = ["ab","cd","pq","xy"]
    for i in range(len(unauthorized)):
        if unauthorized[i] in string:
            return False
    return True

#########STEP TWO#########
def step_two() -> int:
    with open('day_5/input.txt','r') as file:
        count_isok = 0
        for line in file:
            if twin_two(line) and lettercheck(line):
                count_isok += 1
    return count_isok

def twin_two(string: str) -> bool:
    """
    Return True if the string contains a pair of two letters that appears at least twice
    """
    for i in range(len(string)-1):
        for j in range(i+2, len(string)-1):
            if string[i] == string[j] and string[i+1] == string[j+1]:
                return True

def lettercheck(string: str) -> bool:
    """
    Return True if the string contains at least one letter which repeats with exactly one letter between them
    """
    for i in range(len(string)-2):
        if string[i] == string[i+2]:
            return True

def main() -> None:
    start_time = time.time()
    print("Result of Part One:", step_one())
    print("Result of Part Two:", step_two())
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    sys.exit(main())