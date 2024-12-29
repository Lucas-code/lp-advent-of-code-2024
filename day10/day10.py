from typing import List, Dict

hikeMap : List[str] = []

with open("example.txt") as file:
    for line in file:
        hikeMap.append(line.strip())

pathEndings : Dict[tuple,set] = {}

def part1Backtracing(currentPos : tuple, path : List[tuple]):
    char = int(hikeMap[currentPos[0]][currentPos[1]])
    
    newPath = path[:]
    newPath.append(currentPos)
    if char == 9:
        # print(currentPos)
        if newPath[0] not in pathEndings:
            pathEndings[newPath[0]] = {currentPos}
        else:
            pathEndings[newPath[0]].add(currentPos)
        # print(pathEndings[newPath[0]])

    else:
        for transform in [(0,1),(1,0),(-1,0),(0,-1)]:
            y = currentPos[0] + transform[0]
            x = currentPos[1] + transform[1]
            if (not (y < 0 or y >= len(hikeMap) or x < 0 or x >= len(hikeMap[0]))) and int(hikeMap[y][x]) == char + 1 :
                nextPos = (y, x)
                part1Backtracing(nextPos, newPath)


def part1():
    for y in range(len(hikeMap)):
        for x in range(len(hikeMap[0])):
            char = hikeMap[y][x]
            if char == "0":
                part1Backtracing((y,x), [])
    
    trailheadScores = {start : len(endings) for start,endings in pathEndings.items()}
    
    return sum(list(trailheadScores.values()))

# Got the answer for part2 while coding part 1 lol just need to change back

trailheadScores = {}

def part2Backtracing(currentPos : tuple, path : List[tuple]):
    char = int(hikeMap[currentPos[0]][currentPos[1]])
    
    newPath = path[:]
    newPath.append(currentPos)
    if char == 9:
        if newPath[0] not in trailheadScores:
            trailheadScores[newPath[0]] = 1
        else:
            trailheadScores[newPath[0]] += 1

    else:
        for transform in [(0,1),(1,0),(-1,0),(0,-1)]:
            y = currentPos[0] + transform[0]
            x = currentPos[1] + transform[1]
            if (not (y < 0 or y >= len(hikeMap) or x < 0 or x >= len(hikeMap[0]))) and int(hikeMap[y][x]) == char + 1 :
                nextPos = (y, x)
                part2Backtracing(nextPos, newPath)


def part2():
    for y in range(len(hikeMap)):
        for x in range(len(hikeMap[0])):
            char = hikeMap[y][x]
            if char == "0":
                part2Backtracing((y,x), [])
    
    
    return sum(list(trailheadScores.values()))

# print(part1())
print(part2())
