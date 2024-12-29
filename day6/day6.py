from typing import List

labMap : List[str] = []

guardPosition = []

with open("puzzleInput.txt") as file:
    for line in file:
        index = line.find("^")
        
        if index != -1:
            # print(line)
            guardPosition = [len(labMap), index]
            # print(len(labMap),index)
        
        labMap.append(line.strip())

def part1():
    visitedLocations = set()

    while True:
        # for line in labMap:
        #     print(line)
        
        # print("\n")

        y, x = guardPosition[0], guardPosition[1]
        visitedLocations.add((y,x))

        guardDirection = labMap[y][x]

        nextLocation = ()
        
        if guardDirection == "^":
            nextLocation = (y-1,x)
        elif guardDirection == ">":
            nextLocation = (y,x+1)
        elif guardDirection == "v":
            nextLocation = (y+1,x)
        elif guardDirection == "<":
            nextLocation = (y,x-1)
        
        if nextLocation[0] >= len(labMap) or nextLocation[0] < 0  or nextLocation[1] >= len(labMap[0]) or nextLocation[1] < 0:
            labMap[y] = labMap[y][:x] + "X" + labMap[y][x+1:]
            break
        else:
        
            if labMap[nextLocation[0]][nextLocation[1]] == "#":
                if guardDirection == "^":
                    nextLocation = (y,x+1)
                elif guardDirection == ">":
                    nextLocation = (y+1,x)
                elif guardDirection == "v":
                    nextLocation = (y,x-1)
                elif guardDirection == "<":
                    nextLocation = (y-1,x)
                
                if nextLocation[0] >= len(labMap) or nextLocation[0] < 0  or nextLocation[1] >= len(labMap[0]) or nextLocation[1] < 0:
                    labMap[y] = labMap[y][:x] + "X" + labMap[y][x+1:]
                    break
                else:
                    labMap[y] = labMap[y][:x] + "X" + labMap[y][x+1:]
                    guardPosition[0], guardPosition[1] = nextLocation[0], nextLocation[1]
                    if guardDirection == "^":
                        labMap[guardPosition[0]] = labMap[guardPosition[0]][:guardPosition[1]] + ">" + labMap[guardPosition[0]][guardPosition[1]+1:]
                    elif guardDirection == ">":
                        labMap[guardPosition[0]] = labMap[guardPosition[0]][:guardPosition[1]] + "v" + labMap[guardPosition[0]][guardPosition[1]+1:]
                    elif guardDirection == "v":
                        labMap[guardPosition[0]] = labMap[guardPosition[0]][:guardPosition[1]] + "<" + labMap[guardPosition[0]][guardPosition[1]+1:]
                    elif guardDirection == "<":
                        labMap[guardPosition[0]] = labMap[guardPosition[0]][:guardPosition[1]] + "^" + labMap[guardPosition[0]][guardPosition[1]+1:]
            else:
                labMap[y] = labMap[y][:x] + "X" + labMap[y][x+1:]
                guardPosition[0], guardPosition[1] = nextLocation[0], nextLocation[1]
                labMap[guardPosition[0]] = labMap[guardPosition[0]][:guardPosition[1]] + guardDirection + labMap[guardPosition[0]][guardPosition[1]+1:]
    
    return len(visitedLocations)


def step(labMap, guardPosition):

    if labMap == "break":
        return ("break", None)

    y, x = guardPosition[0], guardPosition[1]

    guardDirection = labMap[y][x]

    nextLocation = ()

    if guardDirection == "^":
        nextLocation = (y-1,x)
    elif guardDirection == ">":
        nextLocation = (y,x+1)
    elif guardDirection == "v":
        nextLocation = (y+1,x)
    elif guardDirection == "<":
        nextLocation = (y,x-1)
    else:
        print(x, y, guardDirection)
    
    if nextLocation[0] >= len(labMap) or nextLocation[0] < 0  or nextLocation[1] >= len(labMap[0]) or nextLocation[1] < 0:
        return ("break", None)
    else:
    
        if labMap[nextLocation[0]][nextLocation[1]] in ["#", "O"]:
            while labMap[nextLocation[0]][nextLocation[1]] in ["#", "O"]:
                # print(guardDirection, y, x, nextLocation)
                if guardDirection == "^":
                    nextLocation = (y,x+1)
                    guardDirection = ">"
                elif guardDirection == ">":
                    nextLocation = (y+1,x)
                    guardDirection = "v"
                elif guardDirection == "v":
                    nextLocation = (y,x-1)
                    guardDirection = "<"
                elif guardDirection == "<":
                    nextLocation = (y-1,x)
                    guardDirection = "^"
                
                # print(guardDirection, y, x, nextLocation)
                labMap[y] = labMap[y][:x] + guardDirection + labMap[y][x+1:]
                # print(labMap[y])
            
            if nextLocation[0] >= len(labMap) or nextLocation[0] < 0  or nextLocation[1] >= len(labMap[0]) or nextLocation[1] < 0:
                return ("break", None)
            else:
                labMap[y] = labMap[y][:x] + "X" + labMap[y][x+1:]
                guardPosition[0], guardPosition[1] = nextLocation[0], nextLocation[1]
                labMap[guardPosition[0]] = labMap[guardPosition[0]][:guardPosition[1]] + guardDirection + labMap[guardPosition[0]][guardPosition[1]+1:]
                # if guardDirection == "^":
                #     labMap[guardPosition[0]] = labMap[guardPosition[0]][:guardPosition[1]] + ">" + labMap[guardPosition[0]][guardPosition[1]+1:]
                # elif guardDirection == ">":
                #     labMap[guardPosition[0]] = labMap[guardPosition[0]][:guardPosition[1]] + "v" + labMap[guardPosition[0]][guardPosition[1]+1:]
                # elif guardDirection == "v":
                #     labMap[guardPosition[0]] = labMap[guardPosition[0]][:guardPosition[1]] + "<" + labMap[guardPosition[0]][guardPosition[1]+1:]
                # elif guardDirection == "<":
                #     labMap[guardPosition[0]] = labMap[guardPosition[0]][:guardPosition[1]] + "^" + labMap[guardPosition[0]][guardPosition[1]+1:]
        else:
            labMap[y] = labMap[y][:x] + "X" + labMap[y][x+1:]
            guardPosition[0], guardPosition[1] = nextLocation[0], nextLocation[1]
            labMap[guardPosition[0]] = labMap[guardPosition[0]][:guardPosition[1]] + guardDirection + labMap[guardPosition[0]][guardPosition[1]+1:]
    
    return (labMap,guardPosition)

# Using fast and slow pointer to detect loops
# Naive Approach:
# Go through every "." in the map and replace with new obstacle "O"
# Within that iteration, compute the guard's path from the beginning
# Use fast and slow pointer to detect loops
# Too inefficient to run in a reasonable amount of time

def part2Naive():
    obstructions = set()

    for y in range(len(labMap)):
        for x in range(len(labMap[0])):
            if labMap[y][x] != ".":
                continue 
            newMap = labMap.copy()
            newMap[y] = newMap[y][:x] + "O" + newMap[y][x+1:]
            fastMap = newMap.copy()
            fastGuardPos = guardPosition.copy()
            slowMap = newMap.copy()
            slowGuardPos = guardPosition.copy()
            loopDetected = False
            while not loopDetected:
                slowMap,slowGuardPos = step(slowMap, slowGuardPos)

                fastMap, fastGuardPos = step(fastMap, fastGuardPos)
                fastMap, fastGuardPos = step(fastMap, fastGuardPos)

                if slowMap == "break" or fastMap == "break":
                    break
                
                if slowGuardPos == fastGuardPos:
                    loopDetected = True
            
            if loopDetected:
                obstructions.add((y,x))
    
    return len(obstructions)

# More optimal approach:
# Run guard's path once
# Only look at the places that the guard has explored (the "X"s) as potential places to put a new object and use same method as naive approach
# Cuts down on the amount of places to check
# Still not the fastest but runs in a bearable amount of time
# Need a faster approach to identify loop

def part2():
    startingGuardPos = guardPosition.copy()
    part1()
    labMap[startingGuardPos[0]]= labMap[startingGuardPos[0]][:startingGuardPos[1]] + "^" +  labMap[startingGuardPos[0]][startingGuardPos[1]+1:]

    obstructions = set()

    # print(labMap)

    # count = 0

    for y in range(len(labMap)):
        for x in range(len(labMap[0])):
            if labMap[y][x] != "X":
                continue
            # count += 1
            # continue
            newMap = labMap.copy()
            newMap[y] = newMap[y][:x] + "O" + newMap[y][x+1:]
            fastMap = newMap.copy()
            fastGuardPos = startingGuardPos.copy()
            slowMap = newMap.copy()
            slowGuardPos = startingGuardPos.copy()
            loopDetected = False
            while not loopDetected:
                slowMap,slowGuardPos = step(slowMap, slowGuardPos)

                # if (y,x) == (2,8):
                    # print("slowMap")
                    # for line in slowMap:
                    #     print(line)
                    
                    # print("\n")

                    # print("fastMap")
                    # for line in fastMap:
                    #     print(line)
                    
                    # print("\n")

                fastMap, fastGuardPos = step(fastMap, fastGuardPos)
                fastMap, fastGuardPos = step(fastMap, fastGuardPos)

                if slowMap == "break" or fastMap == "break":
                    break
                
                if slowGuardPos == fastGuardPos and slowMap[slowGuardPos[0]][slowGuardPos[1]] == fastMap[fastGuardPos[0]][fastGuardPos[1]]:
                    loopDetected = True
            
            if loopDetected:
                # for line in slowMap:
                #     print(line)
                
                # print("\n")
                obstructions.add((y,x))
                # print((y,x))
    
    # print(obstructions)
    
    return len(obstructions)



print(part1())
print(part2())