monkeyPlans = open("2022/day11.txt","r")
part2 = True


class Monkey():
    
    def __init__(self,items,operationNum,operationType,test,trueM,falseM):
        self.items = items
        self.operationNum = operationNum
        self.operationType = operationType
        self.test = test
        self.trueM = trueM
        self.falseM = falseM
        self.monkeyBusiness = 0
    
    def applyOp(self,item):
        if self.operationNum == 'old':
            return item*item
        elif self.operationType == '+':
            return item+int(self.operationNum)
        else:
            return item*int(self.operationNum)
    
    def addItem(self,item):
        self.items.append(item)
    
    def getItems(self):
        return self.items
    
    def testItem(self,item):
        if item % self.test == 0:
            return self.trueM
        else:
            return self.falseM

    def emptyItems(self):
        self.items = []
    
    def getMonkeyBusiness(self):
        return self.monkeyBusiness
    
    def updateBusiness(self,amount):
        self.monkeyBusiness += amount

    def getTest(self):
        return self.test

items = []
monkeys=[]
for i in range(8):
    monkeyPlans.readline()
    items = monkeyPlans.readline().strip(" \n").split(" ")[2:]
    for item in range(len(items)):
        items[item] = int(items[item].strip(","))
    operation = monkeyPlans.readline().strip(" \n").split(" ")[4:]
    test = int(monkeyPlans.readline().strip(" \n").split(" ")[3])
    trueM = int(monkeyPlans.readline().strip(" \n").split(" ")[5])
    falseM = int(monkeyPlans.readline().strip(" \n").split(" ")[5])
    newMonkey = Monkey(items,operation[1],operation[0],test,trueM,falseM)
    monkeys.append(newMonkey)
    monkeyPlans.readline()

managementConstant = 1
if part2:
    for monkey in monkeys:
        managementConstant *= monkey.getTest()

for i in range(10000):
    for monkey in monkeys:
        for thing in monkey.getItems():
            if part2:
                newItem = monkey.applyOp(thing)%managementConstant
            else:
                newItem = monkey.applyOp(thing)//3
            monkeys[monkey.testItem(newItem)].addItem(newItem)
            monkey.updateBusiness(1)
            monkey.emptyItems()

            
businesses = []
for monkey in monkeys:
    businesses.append(monkey.getMonkeyBusiness())
businesses.sort()
totalMonkeyBusiness = businesses[len(businesses)-1]*businesses[len(businesses)-2]
monkeyPlans.close()
print(businesses)
print("Monkey Business:", totalMonkeyBusiness)
