import math
from typing import List, Dict

maxWidth = 101
maxHeight = 103

robotPositions : List[Dict] = []

with open("puzzleInput.txt") as file:
    for line in file:
        position, velocity = line.strip().split(" ")
        posX, posY = position[2:].split(",")
        velX, velY = velocity[2:].split(",")

        robotPositions.append({"currentPos" : (int(posX),int(posY)), "velocity": (int(velX), int(velY))})

def part1():
    for _ in range(100):
        for rp in robotPositions:
            currentPos = rp["currentPos"]

            newX = currentPos[0] + rp["velocity"][0]

            if newX >= maxWidth:
                newX -= maxWidth
            elif newX < 0:
                newX += maxWidth

            newY = currentPos[1] + rp["velocity"][1]

            if newY >= maxHeight:
                newY -= maxHeight
            elif newY < 0:
                newY += maxHeight

            newPos = (newX, newY)
            rp["currentPos"] = newPos
    
    quadrants = [0,0,0,0]
    
    for rp in robotPositions:
        currentPos = rp["currentPos"]
        print(currentPos)
        quadrantWidth = (maxWidth-1)/2
        quadrantHeight = (maxHeight-1)/2

        if currentPos[0] < quadrantWidth:
            if currentPos[1] < quadrantHeight:
                quadrants[0] += 1
            elif currentPos[1] > quadrantHeight:
               quadrants[2] += 1
        elif currentPos[0] > quadrantWidth:          
            if currentPos[1] < quadrantHeight:
                quadrants[1] += 1
            elif currentPos[1] > quadrantHeight:
               quadrants[3] += 1
    
    print(quadrants)
    
    return math.prod(quadrants)

print(part1())