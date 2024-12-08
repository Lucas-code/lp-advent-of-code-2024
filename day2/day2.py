from typing import List

reports = []

with open("puzzleInput.txt") as file:
    for line in file:
        reports.append([int(level) for level in line.strip().split(" ")])

def isSafe(report : List[int]):
    # print(report)
    increasing = False
    decreasing = False
    for i in range(len(report)-1):
        diff = abs(report[i] - report[i+1])
        if diff < 1 or diff > 3:
            return False
        
        if report[i] > report[i+1]:
            decreasing = True
        else:
            increasing = True
        
        if increasing and decreasing:
            return False
    
    return True

def isSafePart2(report : List[int]):
    if isSafe(report):
        return True
    else:
        for i in range(len(report)):
            if isSafe(report[:i] + report[i+1:]):
                return True
        
        return False
    


def solvePart1():
    result = 0

    for report in reports:
        if isSafe(report):
            result += 1

    return result

def solvePart2():
    result = 0

    for report in reports:
        if isSafePart2(report):
            result += 1

    return result

if __name__ == "__main__":
    # print(solvePart1())
    print(solvePart2())