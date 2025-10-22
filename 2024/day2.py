from math import copysign
f = open("2024/day2.txt","r")
input = f.readlines()
f.close()

def part1():
    safeReports = len(input)
    for report in input:
        report = report.split()
        unsafe = False
        levels = []
        for i in range(len(report)-1):
            levels.append(int(report[i])-int(report[i+1]))
        previousSign = 0
        for level in levels:
            if level == 0:
                unsafe = True
                break
            elif abs(level) > 3:
                unsafe = True
                break
            else:
                if previousSign == 0:
                    previousSign = copysign(1,level)
                elif previousSign != copysign(1,level):
                    unsafe = True
                    break
                else:
                    previousSign = copysign(1,level)
        if unsafe:
            safeReports -= 1
    return safeReports




def checkReport(report):
        unsafe = False
        levels = []
        for i in range(len(report)-1):
            levels.append(int(report[i])-int(report[i+1]))
        previousSign = 0
        for level in levels:
            if level == 0:
                unsafe = True
                break
            elif abs(level) > 3:
                unsafe = True
                break
            else:
                if previousSign == 0:
                    previousSign = copysign(1,level)
                elif previousSign != copysign(1,level):
                    unsafe = True
                    break
                else:
                    previousSign = copysign(1,level)
        
        return not unsafe


def part2():
    safeReports = 0
    for report in input:
        report = report.split()
        if checkReport(report):
            safeReports += 1
        else:
            for i in range(len(report)):
                tempReport = []
                for j in report:
                    tempReport.append(j)
                tempReport.pop(i)
                if checkReport(tempReport):
                    safeReports += 1
                    break
    return safeReports


print("Part 1: ", str(part1()))
print("Part 2: ", str(part2()))