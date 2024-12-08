list1 = []
list2 = []

with open("puzzleInput.txt") as file:
    for line in file:
        item1, item2 = line.strip().split("   ")
        list1.append(item1)
        list2.append(item2)

# O(n) time complexity

def solve():

    sortedList1 = sorted(list1, reverse=True)
    sortedList2 = sorted(list2, reverse=True)

    result = 0

    for i in range(len(sortedList1)):
        result += abs(int(sortedList1[i]) - int(sortedList2[i]))
    
    return result

if __name__ == "__main__":
    print(solve())