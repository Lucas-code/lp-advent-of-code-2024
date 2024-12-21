from typing import List

wordSearch : List[str] = []

with open("puzzleInput.txt") as file:
    for line in file:
        wordSearch.append(line.strip())

maxY = len(wordSearch)
maxX = len(wordSearch[0])

# Solutions could be simplified

def part1():
    wordToSearch = "XMAS"
    wordLen = len(wordToSearch)

    result = 0
    
    for i in range(maxY):
        for j in range(maxX):
            for transY in range(-1,2):
                for transX in range(-1,2):
                    if transX == 0 and transY == 0:
                        continue

                    wordToCheck = wordSearch[i][j]
                    tempY = i
                    tempJ = j
                    for _ in range(wordLen-1):
                        tempY += transY
                        tempJ += transX
                        if tempY < 0 or tempY >= maxY or tempJ < 0 or tempJ >= maxX:
                            break
                        wordToCheck = wordToCheck + wordSearch[tempY][tempJ]
                    if wordToCheck == wordToSearch or wordToCheck[::-1] == wordToSearch:
                        result += 1

    return int(result/2)

# First Time using frozenset (an immutable set) to help with checking membership

def part2():
    potentialCrossovers = set()
    visitedCrossovers = set()

    discoveredWords = set()

    wordToSearch = "MAS"
    wordLen = len(wordToSearch)

    result = 0
    
    for i in range(maxY):
        for j in range(maxX):
            for transY, transX in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                wordToCheck = wordSearch[i][j]
                potentialDW = [(i,j)]
                tempY = i
                tempJ = j
                potentialCrossover = (tempY + transY, tempJ + transX)
                for _ in range(wordLen-1):
                    tempY += transY
                    tempJ += transX
                    if tempY < 0 or tempY >= maxY or tempJ < 0 or tempJ >= maxX:
                        break
                    potentialDW.append((tempY,tempJ))
                    wordToCheck = wordToCheck + wordSearch[tempY][tempJ]
                if wordToCheck == wordToSearch or wordToCheck[::-1] == wordToSearch:
                    potentialDW = frozenset(potentialDW)
                    if potentialDW not in discoveredWords:

                        if potentialCrossover not in visitedCrossovers:
                            if potentialCrossover in potentialCrossovers:
                                result += 1
                                # print(potentialCrossover)
                                visitedCrossovers.add(potentialCrossover)
                                potentialCrossovers.remove(potentialCrossover)
                            else:
                                potentialCrossovers.add(potentialCrossover)
                    
                        discoveredWords.add(frozenset(potentialDW))
    
    
    return result

print(part1())
print(part2())