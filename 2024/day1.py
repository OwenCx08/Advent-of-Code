f = open("2024/day1.txt")
input = f.readlines()
f.close()


listA = []
listB = []
for i in input:
    listA.append(int(i[:5]))
    listB.append(int(i[8:]))

listA.sort()
listB.sort()

def part1():
    totaldist = 0
    for i in range(len(listA)):
        totaldist += abs(listA[i]-listB[i])
    return totaldist

def part2():
    simScore = 0
    for i in range(len(listA)):
        simScore += listA[i] * listB.count(listA[i])
    return simScore

print("Part 1: ", str(part1()))
print("Part 2: ", str(part2()))