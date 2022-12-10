f = open("2022/day10.txt","r")
commandList = f.readlines()
f.close()

def drawPixel(X,cycle):
    cycle = cycle % 40
    if X+1 == cycle or X+1 == cycle-1 or X+1 == cycle+1:
        print("#",end="")
    else:
        print(".",end="")
    if cycle ==0:
        print("\n",end="")


cycle = 1
X = 1
cycleChecks = [20,60,100,140,180,220]
totalStrength = 0
for i in commandList:
    command = i.strip("\n").split(" ")
    if command[0] == "noop":
        if cycle in cycleChecks:
            totalStrength += cycle*X
        drawPixel(X,cycle)
        cycle += 1


    else:
        if cycle in cycleChecks:
            totalStrength += cycle*X
        drawPixel(X,cycle)
        cycle += 1
        if cycle in cycleChecks:
            totalStrength += cycle*X
        drawPixel(X,cycle)
        X += int(command[1])
        cycle += 1
           
print("Part 1: ",totalStrength)
