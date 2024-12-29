import re

diskMap = ""

with open("puzzleInput.txt") as file:
    diskMap = file.readline().strip()

# Originally was storing blocks in a string, but I didn't account for double digit ids, giving me an incorrect calculation
# Had to use a list instead of string (also made it easier to perform swaps)

def part1():
    # Converting to blocks
    isFile = True
    id = 0
    blocks = []
    for digit in diskMap:
        if isFile:
            for _ in range(int(digit)):
                blocks.append(str(id))
            id += 1
        else:
            for _ in range(int(digit)):
                blocks.append(".")
        
        isFile = not isFile
    
    # Compression
    endPointer = len(blocks) - 1
    startPointer = 0
    # print(blocks)

    while endPointer > startPointer:
        if blocks[startPointer] != ".":
            startPointer += 1
            continue

        if blocks[endPointer] == ".":
            endPointer -= 1
            continue

        temp1 = blocks[startPointer]
        temp2 = blocks[endPointer]
        blocks.pop(startPointer)
        blocks.insert(startPointer,temp2)
        blocks.pop(endPointer)
        blocks.insert(endPointer,temp1)
        # blocks = blocks[:startPointer] + blocks[endPointer] + blocks[startPointer+1:endPointer] + temp + blocks[endPointer+1:]
        endPointer -= 1
        startPointer += 1
        # print(blocks)
    
    # print(blocks)
    # Checksum calculation
    checksum = 0
    for m in range(len(blocks)):
        if blocks[m] == ".":
            continue

        checksum += m * int(blocks[m])
    
    return checksum

# Part 2 Compression Step - Go through each block of files and in each iteration, loop through blocks to find a free space
# Worst case O(n^2) - not efficient

def part2():
    # Converting to blocks
    fileDict = {}
    freeSpaces = []
    isFile = True
    id = 0
    blocks = []
    for digit in diskMap:
        start = len(blocks)
        end = start + int(digit)
        if isFile:
            for _ in range(int(digit)):
                blocks.append(str(id))
            fileDict[id] = [start,end]
            id += 1
        else:
            freeSpaces.append([start,end])
            for _ in range(int(digit)):
                blocks.append(".")
        
        isFile = not isFile
    
    # Compression
    fileIds = list(fileDict.keys())

    while fileIds:
        currentFile = fileIds.pop()

        for space in freeSpaces[:]: #Loops through a shallow copy
            if space[1] > fileDict[currentFile][0]:
                break
            
            freeSpaceSize = space[1] - space[0]
            fileSize = fileDict[currentFile][1] - fileDict[currentFile][0]
            
            if freeSpaceSize < fileSize:
                continue
            
            for i in range(fileSize):
                blocks.pop(space[0]+i)
                blocks.insert(space[0]+i,str(currentFile))
                blocks.pop(fileDict[currentFile][0]+i)
                blocks.insert(fileDict[currentFile][0]+i,".")
            
            if freeSpaceSize == fileSize:
                freeSpaces.remove(space)
            else:
                space[0] = space[0] + fileSize
            
            break
    

    # Checksum calculation
    checksum = 0
    for m in range(len(blocks)):
        if blocks[m] == ".":
            continue

        checksum += m * int(blocks[m])
    
    return checksum

print(part1())
print(part2())
