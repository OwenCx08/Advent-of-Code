elves = open("2022/day1.txt","r")
biggest = [0,0,0]
total = 0

for i in elves:
    calorie = i.strip("\n")
    if calorie == "":
        if biggest[0] < total:
            biggest.pop(0)
            biggest.append(total)
            biggest.sort()
        total = 0
    else:
        total += int(calorie)
elves.close()
total = 0
for i in biggest:
    total += i

print(biggest[2])
print(total)
