list1 = []
list2 = []

with open("puzzleInput.txt") as file:
    for line in file:
        item1, item2 = line.strip().split("   ")
        list1.append(item1)
        list2.append(item2)

# O(n) time complexity

def solve():

    list2_freq = {}

    for item in list2:
        if item not in list2_freq:
            list2_freq[item] = 1
        else:
            list2_freq[item] += 1
    
    result = 0

    for item in list1:
        if item in list2_freq:
            result += int(item) * list2_freq[item]

    return result

if __name__ == "__main__":
    print(solve())