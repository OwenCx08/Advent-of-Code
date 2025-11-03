f = open("2024/day3.txt","r")
input = ""
for i in f:
    input += i
f.close()

inputs = input.split("mul")
#print(inputs)

active = True

def checkActive(input,charPointer,currentActive):
    newActive = currentActive
    for i in range(len(input)):
        try:
            if input[charPointer:charPointer+4] == "do()":
                newActive = True
            elif input[charPointer:charPointer+7] == "don't()":
                newActive = False
            charPointer += 1
        except IndexError:
            return newActive
    return newActive

output = 0
for i in inputs:
    charPointer = 0
    try:
        if i[0] == "(":
            charPointer += 1
            if i[charPointer:charPointer+3].isnumeric():
                num1 = int(i[charPointer:charPointer+3])
                charPointer += 3
            elif i[charPointer:charPointer+2].isnumeric():
                num1 = int(i[charPointer:charPointer+2])
                charPointer +=2
            elif i[charPointer:charPointer+1].isnumeric():
                num1 = int(i[charPointer:charPointer+1])
                charPointer += 1
            else:
                print("no Num1",i)
                active = checkActive(i,charPointer,active)
                pass

            if i[charPointer] == ",":
                charPointer +=1
                if i[charPointer:charPointer+3].isnumeric():
                    num2 = int(i[charPointer:charPointer+3])
                    charPointer += 3
                elif i[charPointer:charPointer+2].isnumeric():
                    num2 = int(i[charPointer:charPointer+2])
                    charPointer +=2
                elif i[charPointer:charPointer+1].isnumeric():
                    num2 = int(i[charPointer:charPointer+1])
                    charPointer += 1
                else:
                    print("no Num2",i)
                    active = checkActive(i,charPointer,active)
                    pass
                if i[charPointer] == ")":
                    charPointer += 1
                    #print(i[0:charPointer])
                    #print(num1,num2, (num1*num2))
                    #print(output)
                    if active:
                        output += num1 * num2
                    active = checkActive(i,charPointer,active)
                else:
                    active = checkActive(i,charPointer,active)
                    print("no Close Bracket",i)
                    pass
            else:
                active = checkActive(i,charPointer,active)
                print("No comma",i)
                pass
        else:
            active = checkActive(i,charPointer,active)
            print("No Open Bracket",i)
            pass
    except IndexError:
        print("Too Short",i)
        active = checkActive(i,charPointer,active)
        pass

print(output)

