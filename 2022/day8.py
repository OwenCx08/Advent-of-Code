f = open("2022/day8.txt","r")
treeGrid = f.readlines()
f.close()
forest = []
totalVisible = 0
for i in treeGrid:
    forest.append(i.strip("\n"))
visibleForest = []
for i in range(len(forest)):
    visibleForest.append([])
    for j in range(len(forest[i])):
        visibleForest[i].append(0)

#Visible from Left
for i in range(len(forest)):
    tallestTree = -1
    for j in range(len(forest[i])):
        if int(forest[i][j]) > tallestTree:
            visibleForest[i][j] = 1
            tallestTree = int(forest[i][j])

#Visible from Top
for i in range(len(forest)):
    tallestTree = -1
    for j in range(len(forest[j])):
        if int(forest[j][i]) > tallestTree:
            visibleForest[j][i] = 1
            tallestTree = int(forest[j][i])

#Visible from Right
for i in range(len(forest)):
    tallestTree = -1
    for j in range(len(forest[i])):
        if int(forest[len(forest)-i-1][len(forest)-j-1]) > tallestTree:
            visibleForest[len(forest)-i-1][len(forest)-j-1] = 1
            tallestTree = int(forest[len(forest)-i-1][len(forest)-j-1])

#Visible from Bottom
for i in range(len(forest)):
    tallestTree = -1
    for j in range(len(forest[i])):
        if int(forest[len(forest)-j-1][len(forest)-i-1]) > tallestTree:
            visibleForest[len(forest)-j-1][len(forest)-i-1] = 1
            tallestTree = int(forest[len(forest)-j-1][len(forest)-i-1])


for i in visibleForest:
    for j in i:
        if j:
            totalVisible += 1

print("Part 1: ",totalVisible)

scenicScores = []
for i in range(len(forest)):
    scenicScores.append([])
    for j in range(len(forest[i])):
        scenicScores[i].append(0)

for row in range(len(forest)):
    for column in range(len(forest)):
        scenicScore = 1
        total = 0
        for i in range(1,row+1):
            total += 1
            if forest[row][column] <= forest[row-i][column]:
                break
        scenicScore *= total
        total = 0
        for i in range(1,len(forest)-row):
            total += 1
            if forest[row][column] <= forest[row+i][column]:
                break  
        scenicScore *= total
        total = 0
        for i in range(1,column+1):
            total += 1
            if forest[row][column] <= forest[row][column-i]:
                break    
        scenicScore *= total
        total = 0
        for i in range(1,len(forest)-column):
            total += 1
            if forest[row][column] <= forest[row][column+i]:
                break

        scenicScore *= total
        scenicScores[row][column] = scenicScore
        total = 0

largestScore = 0
for i in range(len(scenicScores)):
    for j in range(len(scenicScores)):
        if scenicScores[i][j] > largestScore:
            largestScore = scenicScores[i][j]
            #print(i," ",j)
print("Part 2: ",largestScore)
