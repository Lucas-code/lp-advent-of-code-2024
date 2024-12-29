from typing import List


equations = []

with open("puzzleInput.txt") as file:
    for line in file:
        testValue, numbers = line.strip().split(": ")
        numbers = [int(number) for number in numbers.split(" ")]
        equation = (int(testValue), numbers)
        equations.append(equation)

## Solved this one very quickly!
# Made use of recursive backtracking to explore all potential solutions
# When the calculation is starting to become bigger than the desired value, we return False to improve efficiency and limit recursive calls  

def part1Backtracking(testValue: int, numbers : List[int], currentValue = 0, startIndex = 0):
    if currentValue > testValue or startIndex >= len(numbers):
        return False
    elif startIndex == 0:
        currentValue = numbers[0]
        return part1Backtracking(testValue, numbers, currentValue, startIndex+1)
    else:
        currentValue1 = currentValue + numbers[startIndex]
        currentValue2 = currentValue * numbers[startIndex]

        if (currentValue1 == testValue or currentValue2 == testValue) and startIndex == len(numbers)-1:
            return True
        else:
            return part1Backtracking(testValue, numbers, currentValue1, startIndex+1) or part1Backtracking(testValue, numbers, currentValue2, startIndex+1)     

def part1():
    result = 0

    for equation in equations:
        testValue = equation[0]
        numbers = equation[1]
        isTrue = part1Backtracking(testValue, numbers)

        if isTrue:
            result += testValue
    
    return result

def part2Backtracking(testValue: int, numbers : List[int], currentValue = 0, startIndex = 0):
    if currentValue > testValue or startIndex >= len(numbers):
        return False
    elif startIndex == 0:
        currentValue = numbers[0]
        return part2Backtracking(testValue, numbers, currentValue, startIndex+1)
    else:
        currentValue1 = currentValue + numbers[startIndex]
        currentValue2 = currentValue * numbers[startIndex]
        currentValue3 = int(str(currentValue) + str(numbers[startIndex]))

        if (currentValue1 == testValue or currentValue2 == testValue or currentValue3 == testValue) and startIndex == len(numbers)-1:
            return True
        else:
            return part2Backtracking(testValue, numbers, currentValue1, startIndex+1) or part2Backtracking(testValue, numbers, currentValue2, startIndex+1) or part2Backtracking(testValue, numbers, currentValue3, startIndex+1)
   

def part2():
    result = 0

    for equation in equations:
        testValue = equation[0]
        numbers = equation[1]
        isTrue = part2Backtracking(testValue, numbers)

        if isTrue:
            result += testValue
    
    return result


print(part1())
print(part2())