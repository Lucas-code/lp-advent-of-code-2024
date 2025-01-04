from typing import List, Dict
import math

configs: List[Dict[str,tuple]] = []

with open("puzzleInput.txt") as file:
    buttonA = ()
    buttonB = ()
    prize = ()
    for line in file:
        if line.strip() != "":
            button, coords = line.strip().split(": ")
            x, y = coords.split(", ")
            x = int(x[2:])
            y = int(y[2:])

            if "A" in button:
                buttonA = (x,y)
            if "B" in button:
                buttonB = (x,y)
            else:
                prize = (x,y)
                configs.append({"A": buttonA, "B": buttonB, "Prize" : prize})

explroedCombos = set()

def part1Recur(config : Dict[str,tuple], pos : tuple, spent : int, APressed: int, BPressed: int, APressedLast : bool):
    explroedCombos.add((APressed,BPressed))
    # print(spent, APressed, BPressed, pos)
    
    if pos == config["Prize"]:
        return spent
    elif pos[0] > config["Prize"][0] or pos[1] > config["Prize"][1] or APressed > 100 or BPressed > 100:
        return False
    else:
        if APressedLast:
            result = False
        else:
            newPos = (pos[0] + config["B"][0], pos[1] + config["B"][1])
            result = part1Recur(config, newPos, spent + 1, APressed, BPressed + 1, False)
        if result != False:
            return result
        else:

            newPos = (pos[0] + config["A"][0], pos[1] + config["A"][1])
            result = part1Recur(config, newPos, spent + 3, APressed + 1, BPressed, True)
            return result

def part1():
    result = 0
    # print(configs)
    for config in configs:
        # Checking if we can reach the prize before running the recursive func (more efficient)
        # Get the Greatest Common Divisor (GCD) and check if target is divisible by the GCD
        # This part runs in O(log(min(a,b))) - fairly efficient
        gcdX = math.gcd(config["A"][0],config["B"][0])
        gcdY = math.gcd(config["A"][1],config["B"][1])

        if config["Prize"][0] % gcdX != 0 or config["Prize"][1] % gcdY != 0:
            # print("huh")
            continue

        # Now we can run recursion
        cost = part1Recur(config,(0,0),0,0,0,False)
        if cost != False:
            result += cost
    
    return result

# Had to check reddit again :(
# After looking at comments I reaslised that this is more of a mathematical problem than a algorithmic problem
# Basically finding the two unknown values of x and y in the equation a * x + b * y = c that is the cheapest
# Solved using Cramer's Rule (https://www.youtube.com/watch?v=eDb6iugi6Uk&ab_channel=TheOrganicChemistryTutor)
# Shows that the small details and hints in the question and thinking outside the box is important to solving problems

def part2():
    result = 0
    for config in configs:

        config["Prize"] = (config["Prize"][0] + 10000000000000, config["Prize"][1] + 10000000000000)
        # print(config["Prize"])
        # Checking if we can reach the prize
        # Get the Greatest Common Divisor (GCD) and check if target is divisible by the GCD
        # This part runs in O(log(min(a,b))) - fairly efficient
        gcdX = math.gcd(config["A"][0],config["B"][0])
        gcdY = math.gcd(config["A"][1],config["B"][1])

        if config["Prize"][0] % gcdX != 0 or config["Prize"][1] % gcdY != 0:
            continue

        x = (config["Prize"][0] * config["B"][1] - config["Prize"][1] * config["B"][0]) // (config["A"][0] * config["B"][1] - config["A"][1] * config["B"][0])
        y = (config["A"][0] * config["Prize"][1] - config["A"][1] * config["Prize"][0]) // (config["A"][0] * config["B"][1] - config["A"][1] * config["B"][0])

        # result += x*3 + y
        test = (config["A"][0] * x + config["B"][0] * y, config["A"][1] * x + config["B"][1] * y)
        # print(test, config["Prize"])
        if test == config["Prize"]:
            result += x*3 + y
        # print(x,y)
    return result

print(part2())