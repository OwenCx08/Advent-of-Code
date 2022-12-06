file = open("2022/day6.txt")
data = file.readline()
file.close()

#Part 1
def findStartOfPacket(dataStream):
    charGroup = [dataStream[0],dataStream[1],dataStream[2]]
    if dataStream[3] not in charGroup:
        return 4
    else:
        charGroup.append(dataStream[3])
        for i in range(4,len(dataStream)):
            charGroup.pop(0)
            if dataStream[i] not in charGroup and charGroup[2]!= charGroup[1] and charGroup[1] != charGroup[0] and charGroup[2] != charGroup[0]:
                return i+1
            else:
                charGroup.append(dataStream[i])

#Part 2
def findStartOfMessage(dataStream):
    charGroup = []
    skipCounter = 0
    for i in range(13):
        if dataStream[i] in charGroup:
            charGroup.reverse()
            skipCounter = len(charGroup) - charGroup.index(dataStream[i])
            charGroup.reverse()
        else:
            skipCounter -= 1
        charGroup.append(dataStream[i])
    if dataStream[13] not in charGroup:
        if skipCounter == 0:
            return 14
        else:
            charGroup.append(dataStream[i])
            skipCounter -= 1
    else:
        charGroup.reverse()
        skipCounter = len(charGroup) - charGroup.index(dataStream[i])
        charGroup.reverse()

    for i in range(14,len(dataStream)):
        charGroup.pop(0)
        if dataStream[i] not in charGroup:
            if skipCounter == 0:
                return i+1
            else:
                skipCounter -= 1
        else:
            charGroup.reverse()
            if (len(charGroup) - charGroup.index(dataStream[i])) > skipCounter:
                skipCounter = len(charGroup) - charGroup.index(dataStream[i])
            skipCounter -= 1
            charGroup.reverse()
        charGroup.append(dataStream[i])
        
          
print(findStartOfPacket(data))
print(findStartOfMessage(data))
        