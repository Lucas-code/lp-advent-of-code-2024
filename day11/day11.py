from typing import List, Dict

stones : List[str] = []

with open("puzzleInput.txt") as file:
    stones = file.readline().strip().split(" ")

def part1():
    global stones
    localStones = stones.copy()
    for _ in range(25):
        newStones = []
        for i in range(len(localStones)):
            if localStones[i] == "0":
                newStones.append("1")
            elif len(localStones[i]) % 2 == 0:
                halfLen = len(localStones[i]) // 2
                newStones.append(localStones[i][:halfLen])
                newStones.append(str(int(localStones[i][halfLen:])))
            else:
                newStones.append(str(int(localStones[i])*2024))
        localStones = newStones
        # print(len(localStones))
    
    return len(localStones)

# part1 implementation doesn't work for part2, too inefficient
# Applied memoization, but still couldn't run in a reasonable amount of time
# Then applied DFS, which didn't work (but ended up being helpful for my final implementation)
# Hardest problem so far in AoC
# Had to go to the AoC reddit for clues
# Solved the problem by adding more memoization
# Previously memoized the next transformation, but to further reduce computation, I memoized the length of the list at the end of all blinks from a specific stone at a specific depth
# Didn't store in a list to reduce space complexity


def dfs(stone, memoTrans, memoFinal, depth):
    # Base case: transformation process is done
    if depth == 75:  # Limit depth or recursion limit based on iteration count
        return 1

    result = []

    # If the stone has been processed before, return the stored result
    if (stone,depth) in memoFinal:
        return memoFinal[(stone,depth)]
    elif stone in memoTrans:
        result = memoTrans[stone]
    # Perform transformations
    elif len(stone) % 2 == 0:
        halfLen = len(stone) // 2
        item1 = stone[:halfLen]
        item2 = str(int(stone[halfLen:]))
        result = [item1, item2]
    else:
        item1 = str(int(stone) * 2024)
        result = [item1]

    # Save the result for the current stone in memo
    memoTrans[stone] = result

    # Recursively explore transformations of each result string
    total = 0
    for r in result:
        next = dfs(r, memoTrans, memoFinal, depth + 1)
        total += next
    
    memoFinal[(stone,depth)] = total
    return total

def part2():
    global stones
    localStones = stones.copy()

    memoTrans = {'0': ['1']}  # Memoization initialization for known base case
    memoFinal = {}
    
    # Use DFS to handle transformations
    result = 0
    for stone in localStones:
        result += dfs(stone, memoTrans, memoFinal, 0)

    return result

print(part2())