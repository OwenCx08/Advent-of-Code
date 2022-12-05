rucksacks = open("2022/day3.txt","r")
part1Total = 0
part2Total = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"
groupCount = 0
for i in rucksacks:
    sack = i.strip("\n")
    #Part 1
    compartment1, compartment2 = sack[:len(sack)//2], sack[len(sack)//2:]
    for item in compartment1:
        if item in compartment2:
            if item.islower():
                part1Total += alphabet.find(item) + 1
            else:
                part1Total += alphabet.find(item.lower()) + 27
            break
    
    #Part 2
    if groupCount == 0:
        firstMember = sack
        groupCount += 1
    elif groupCount == 1:
        secondMember = sack
        groupCount += 1
    else:
        for item in sack:
            if item in firstMember and item in secondMember:
                if item.islower():
                    part2Total += alphabet.find(item) + 1
                else:
                    part2Total += alphabet.find(item.lower()) + 27
                break
        groupCount = 0
rucksacks.close()
print(part1Total)
print(part2Total)
