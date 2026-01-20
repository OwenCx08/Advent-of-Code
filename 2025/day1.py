f = open("2025/day1.txt","r")
input = f.readlines()
f.close()

def part1():
    position = 50
    timesAtZero = 0
    for i in input:
        if i[0] == "L":
            position = (position - int(i[1:])) % 100
        else:
            position = (position + int(i[1:])) % 100
        if position == 0:
            timesAtZero += 1
    return timesAtZero

def part2():
    position = 50
    timesAtZero = 0
    for i in input:
        i = i.strip("\n")
        if i[0] == "L":
            for j in range(int(i[1:])):
                position = (position - 1) % 100
                if position == 0:
                    timesAtZero += 1
        else:
            for j in range(int(i[1:])):
                position = (position + 1) % 100
                if position == 0:
                    timesAtZero += 1
    return timesAtZero

print("Part 1:",part1())
print("Part 2:",part2())