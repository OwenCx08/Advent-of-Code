f = open("2022/day7.txt")
commandList = f.readlines()
f.close()

class tree():
    def __init__(self,name,parent=None):
        self.name = name
        self.children = []
        self.size = 0
        self.parent = parent
    
    def getParent(self):
        return self.parent

    def getName(self):
        return self.name

    def addChild(self,child):
        self.children.append(child)
    
    def setSize(self,size):
        self.size = size

    def findSize(self):
        if self.children == [] or self.size != 0:
            return self.size
        else:
            totalsize = 0
            for child in self.children:
                totalsize += child.findSize()
            self.setSize(totalsize)
            return self.size

root = tree("/")
directories = [root]
activeTree = None
for i in commandList:
    if activeTree == None:
        activeTree = directories[0]
    command = i.strip("\n").split(" ")
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == ".." and activeTree.getName != "/":
                
                activeTree = activeTree.getParent()
                #print(activeTree.getName())
            for item in directories:
                if command[2] == item.getName() and item.getParent() == activeTree:
                    activeTree = item
                    break

    elif command[0] == "dir":
        newDirectory = tree(command[1],parent=activeTree)
        directories.append(newDirectory)
        activeTree.addChild(newDirectory)
    else:
        newDirectory = tree(command[1],parent=activeTree)
        newDirectory.setSize(int(command[0]))
        #directories.append(newDirectory)
        activeTree.addChild(newDirectory)
        
totalSize = 0
for i in directories:
    size = i.findSize()
    if size <= 100000:
        totalSize += size
spaceNeeded = 30000000 - (70000000 - directories[0].findSize())
smallestSize = directories[0].findSize()
for i in directories:
    size = i.findSize()
    if size >= spaceNeeded and size < smallestSize:
        smallestSize = size

print("Part 1: ",totalSize)
print("Part 2: ",smallestSize)
