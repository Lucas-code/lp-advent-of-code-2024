import re

# import os

# script_directory = os.path.dirname(os.path.abspath(__file__))

# current_directory = os.getcwd()

# if current_directory != script_directory:
#     os.chdir(script_directory)

memory = ""

with open("puzzleInput.txt") as file:
    for line in file:
        memory = memory + line.strip()
    
def part1():
    result = 0
    matches = re.findall(r"mul\((\d+),(\d+)\)", memory)

    
    for match in matches:
        x, y = match
        result += int(x) * int(y)
    
    return result

def part2():
    enabled = True

    l = 0

    result = 0

    for i in range(len(memory)):
        window = memory[l:i+1]
        # if len(window) == 200:
            # print(window)
        if enabled:
            if "don't()" in window or i == len(memory)-1:
                # print(window)
                matches = re.findall(r"mul\((\d+),(\d+)\)", window)
                # print(matches)

                for match in matches:
                    x, y = match
                    result += int(x) * int(y)
                
                l = i + 1
                enabled = False
        else:
            if "do()" in window:
                # print(window)
                l = i + 1
                enabled = True
    
    return result

if __name__ == "__main__":
    print(part1())
    print(part2())