from typing import List, Dict

plot = []

with open("puzzleInput.txt") as file:
    for line in file:
        plot.append(line.strip())

# Made use of backtracking approach for part1 (similar to day 10)

explored = set()

def part1Backtracking(pos: tuple,region: List[tuple],perimeters: List[int]):
    explored.add(pos)
    region.append(pos)
    y, x = pos[0], pos[1]
    letter = plot[y][x]
    perimeter = 4


    for transform in [(0,1),(1,0),(-1,0),(0,-1)]:
            ny = y + transform[0]
            nx = x + transform[1]
            nextPos = (ny, nx)
            if not (ny < 0 or ny >= len(plot) or nx < 0 or nx >= len(plot[0])):
                nextLetter = plot[ny][nx]
                if nextLetter == letter:
                    perimeter -= 1
                    if nextPos not in explored:
                        part1Backtracking(nextPos,region,perimeters)
    
    perimeters.append(perimeter)
    
    if pos == region[0]:
        area = len(region)
        # print(area,sum(perimeters),area * sum(perimeters))
        # print(region)
        # print(explored)
        return area * sum(perimeters)



def part1():
    # explored = set()
    result = 0
    for y in range(len(plot)):
        for x in range(len(plot[0])):
            # print((y,x),explored)
            if (y,x) in explored:
                continue
            else:
                # print((y,x),explored)
                result += part1Backtracking((y,x),[],[])
    
    return result

# Part 2 was also tough, had to consult reddit for help
# Difficulty lied in finding out how to calculate sides of a region

explored = set()

def part2Backtracking(pos: tuple,region: List[tuple], sides : Dict[str,set[tuple]]):
    explored.add(pos)
    region.append(pos)
    y, x = pos[0], pos[1]
    letter = plot[y][x]
    top = bottom = left = right = True


    for transform in [(0,1),(1,0),(-1,0),(0,-1)]:
            ny = y + transform[0]
            nx = x + transform[1]
            nextPos = (ny, nx)
            if not (ny < 0 or ny >= len(plot) or nx < 0 or nx >= len(plot[0])):
                nextLetter = plot[ny][nx]
                if nextLetter == letter:
                    if transform == (0,1):
                        right = False
                    elif transform == (0,-1):
                        left = False
                    elif transform == (1,0):
                        bottom = False
                    elif transform == (-1,0):
                        top = False
                    
                    if nextPos not in explored:
                        part2Backtracking(nextPos, region, sides)
    
    if top:
        sides["TOP"].add((y,x))
    if bottom:
        sides["BOTTOM"].add((y,x))
    if left:
        sides["LEFT"].add((y,x))
    if right:
        sides["RIGHT"].add((y,x))
    
    if pos == region[0]:
        area = len(region)
        numSides = 0
        for pol,coords in sides.items():
            for coord in coords:
                checking = ()
                if pol in ["TOP","BOTTOM"]:
                    checking = (coord[0],coord[1]-1)
                else:
                    checking = (coord[0]-1,coord[1])
                
                if checking not in coords:
                    numSides += 1
            
        # print(area,sum(perimeters),area * sum(perimeters))
        # print(region)
        # print(explored)
        return area * numSides



def part2():
    # explored = set()
    result = 0
    for y in range(len(plot)):
        for x in range(len(plot[0])):
            # print((y,x),explored)
            if (y,x) in explored:
                continue
            else:
                # print((y,x),explored)
                result += part2Backtracking((y,x),[],{"TOP": set(), "BOTTOM": set(), "LEFT": set(), "RIGHT": set()})
    
    return result

print(part2())