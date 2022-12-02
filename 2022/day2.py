rounds = open("2022/day2.txt","r")
total = 0
part2total = 0
playerChoice = ["X","Y","Z"]
adversaryChoice = ["A","B","C"]

for i in rounds:
    #Part 1
    round = i.strip("\n")
    if adversaryChoice.index(round[0])== ((playerChoice.index(round[2])-1)%3):
        total += 6
    elif adversaryChoice.index(round[0]) == playerChoice.index(round[2]):
        total += 3
    total += playerChoice.index(round[2])+1

    #Part 2
    if round[0] == "A":
        part2total += ((playerChoice.index(round[2])-1)%3)+1
    elif round[0] == "B":
        part2total += playerChoice.index(round[2])+1
    else:
        part2total += ((playerChoice.index(round[2])+1)%3)+1
    part2total += playerChoice.index(round[2])*3
rounds.close()

print(total)
print(part2total)
