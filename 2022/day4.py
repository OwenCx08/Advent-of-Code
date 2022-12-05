assignments = open("2022/day4.txt")
part1Total = 0
part2Total = 0

for i in assignments:
    assignment = i.strip("\n")
    elf1Start = ""
    elf1End = ""
    elf2Start = ""
    elf2End = ""
    elf2 = False
    end = False
    for character in assignment:
        if character == ",":
            end = False
            elf2 = True
        elif character == "-":
            end = True
        elif elf2 and end:
            elf2End += character
        elif elf2 and not end:
            elf2Start += character
        elif not elf2 and end:
            elf1End += character
        else:
            elf1Start += character
    #Part 1
    if int(elf1Start) <= int(elf2Start) and int(elf1End) >= int(elf2End) or int(elf1Start) >= int(elf2Start) and int(elf1End) <= int(elf2End):
        part1Total += 1
    #Part 2
    if int(elf1Start) <= int(elf2Start) and int(elf1End) >= int(elf2Start) or int(elf2Start) <= int(elf1Start) and int(elf2End) >= int(elf1Start):
        part2Total += 1
assignments.close()
print(part1Total)
print(part2Total)
