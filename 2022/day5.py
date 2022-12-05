rearrangementProcedure = open("2022/day5.txt")
crateStackLines = []
topOfStacks = ""
#Since Part 1 modifies the input a flag is used to choose which part we get the output for
PART1 = False

for i in range(10):
    crateStackLines.append(rearrangementProcedure.readline())


crateStacks = [[],[],[],[],[],[],[],[],[]]
for line in crateStackLines:
    for i in range(len(line)):
        if ord(line[i]) >= 65 and ord(line[i]) <= 90:
            crateStacks[((i+3)//4)-1].append(line[i])
            print(len(line))
            print((i+3)//4)
            print(line[i])
for crateStack in crateStacks:
    crateStack.reverse()
#Part 1
if PART1:
    for i in rearrangementProcedure:
        rearrangementStep = i.split(" from ")
        noOfMoves = rearrangementStep[0].split("move ")[1]
        for move in range(int(noOfMoves)):
            crateStacks[int(rearrangementStep[1][5])-1].append(crateStacks[int(rearrangementStep[1][0])-1][len(crateStacks[int(rearrangementStep[1][0])-1])-1])
            crateStacks[int(rearrangementStep[1][0])-1].pop()
#Part 2
else:
    for i in rearrangementProcedure:
        rearrangementStep = i.split(" from ")
        noOfMoves = rearrangementStep[0].split("move ")[1]
        tempStack = []
        for move in range(int(noOfMoves)):
            tempStack.append(crateStacks[int(rearrangementStep[1][0])-1][len(crateStacks[int(rearrangementStep[1][0])-1])-1])
            crateStacks[int(rearrangementStep[1][0])-1].pop()
        tempStack.reverse()
        for crate in tempStack:
            crateStacks[int(rearrangementStep[1][5])-1].append(crate)
for i in crateStacks:
    topOfStacks += i[len(i)-1]

print(topOfStacks)