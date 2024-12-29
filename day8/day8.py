from typing import List, Dict

antennaMap : List[str] = []

with open("example.txt") as file:
    for line in file:
        antennaMap.append(line.strip())

def part1():
    antennaDict : Dict[str,List[tuple]] = {}
    antinodeLocations = set()
    for y in range(len(antennaMap)):
        for x in range(len(antennaMap[0])):
            char = antennaMap[y][x]
            if char not in [".","#"]:
                if char in antennaDict:
                    for pos in antennaDict[char]:
                        diff = (y - pos[0], x - pos[1]) 
                        antinode1 = (pos[0] - diff[0], pos[1] - diff[1])
                        antinode2 = (y + diff[0], x + diff[1])
                        # print((y,x),pos,diff,antinode1,antinode2)
                        if not (antinode1[0] < 0 or antinode1[0] >= len(antennaMap) or antinode1[1] < 0 or antinode1[1] >= len(antennaMap[0])):
                            antinodeLocations.add(antinode1)
                        if not (antinode2[0] < 0 or antinode2[0] >= len(antennaMap) or antinode2[1] < 0 or antinode2[1] >= len(antennaMap[0])):
                            antinodeLocations.add(antinode2)
                    antennaDict[char].append((y,x))
                else:
                    antennaDict[char] = [(y,x)]
    
    # print(antinodeLocations)

    return len(antinodeLocations)

def part2():
    antennaDict : Dict[str,List[tuple]] = {}
    antinodeLocations = set()
    for y in range(len(antennaMap)):
        for x in range(len(antennaMap[0])):
            char = antennaMap[y][x]
            if char not in [".","#"]:
                if char in antennaDict:
                    for pos in antennaDict[char]:
                        diff = (y - pos[0], x - pos[1])
                        multiplier = 1
                        while True:
                            antinode1 = (pos[0] - diff[0] * multiplier, pos[1] - diff[1] * multiplier)
                            antinode2 = (y + diff[0] * multiplier, x + diff[1] * multiplier)

                            if all(an[0] < 0 or an[0] >= len(antennaMap) or an[1] < 0 or an[1] >= len(antennaMap[0]) for an in [antinode1,antinode2]):
                                break

                            if not (antinode1[0] < 0 or antinode1[0] >= len(antennaMap) or antinode1[1] < 0 or antinode1[1] >= len(antennaMap[0])):
                                antinodeLocations.add(antinode1)
                            if not (antinode2[0] < 0 or antinode2[0] >= len(antennaMap) or antinode2[1] < 0 or antinode2[1] >= len(antennaMap[0])):
                                antinodeLocations.add(antinode2)
                            
                            multiplier += 1
                        antinodeLocations.add((y,x))
                        antinodeLocations.add((pos[0], pos[1]))

                        # print((y,x),pos,diff,antinode1,antinode2)
                        
                    antennaDict[char].append((y,x))
                else:
                    antennaDict[char] = [(y,x)]
    
    return len(antinodeLocations)

# print(part1())
print(part2())