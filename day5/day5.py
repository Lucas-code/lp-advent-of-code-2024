from typing import Dict, List

pagesToLookFor : Dict[int,set] = {}
updates : List[List[int]] = []

with open("puzzleInput.txt") as file:
    for line in file:
        line = line.strip()
        if line.find("|") != -1:
            first, second = line.split("|")
            first, second = int(first), int(second)
            if first in pagesToLookFor:
                pagesToLookFor[first].add(second)
            else:
                pagesToLookFor[first] = set([second])
        elif line.find(",") != -1:
            update = line.split(",")
            update = list(map(int, update))
            updates.append(update)

# print(pagesToLookFor)
# print(updates)

def part1():
    result = 0

    for update in updates:
        isValid = True
        print(update)
        for i in range(len(update)-1,0,-1):
            # print(update)
            if update[i] in pagesToLookFor:
                pagesToCheck = set(update[:i])
                valid = True
                # valid = not any(page in pagesToLookFor[update[i]] for page in pagesToCheck)
                for page in pagesToCheck:
                    if page in pagesToLookFor[update[i]]:
                        valid = False
                        # print(page, update[i])
                # print(pagesToLookFor[update[i]], pagesToCheck)
                if not valid:
                    isValid = False
                    # break
        
        if isValid:
            # print(update, update[int(len(update) / 2) + 1])
            result += update[int((len(update) -1 ) / 2) ]
        # else:
        #     print(update)
        #     for page in pagesToCheck:
        #         if page in pagesToLookFor[update[i]]
        #     print(list(page, update[i]) for page in pagesToCheck if page in pagesToLookFor[update[i]] )

    return result

def part2():
    result = 0

    for update in updates:
        # update = [54, 97, 33, 21, 43, 14, 11, 75, 73, 71, 78, 17, 41] # updates[-1]
        visited = set()
        visitStack = update.copy()
        valid = True
        print(f"initial list {update}")
        while visitStack:
            current = visitStack.pop()

            if current in visited:
                continue

            if current in pagesToLookFor:
                restart = True
                while restart:
                    restart = False
                    pagesToCheck = set(update[:update.index(current)])
                    for page in pagesToCheck:
                        if page in pagesToLookFor[current]:
                            valid = False
                            print(page, current, page in visited)
                            if page not in visited:
                                #replacement
                                # print(page)
                                update.remove(page)
                                # print(f"r list {update}")
                                # print(current, update.index(current))
                                update.insert(update.index(current)+1,page)
                                print(f"m list {update}")
                                visitStack.append(page)
                            else:
                                update.remove(current)
                                # print(f"r list {update}")
                                # print(current, update.index(current))
                                update.insert(update.index(page),current)
                                restart = True
                                print(f"m list {update}")
                                break
                                # visitStack.append(current)


                            # print(f"modified list {update}")
                            # print(page, update[i])
                # print(pagesToLookFor[update[i]], pagesToCheck)
            
            visited.add(current)
        
        if not valid:
            print(f"final list {update}")   
        
        if not valid:
            result += update[int((len(update) -1 ) / 2) ]
    return result

print(part2())
# part2()