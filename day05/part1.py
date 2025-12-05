import sys

file = "test.txt" if sys.argv[1] == "test" else "input.txt"

ranges = []
ids = []

def checkID(id):
    for r in ranges:
        if id in range(int(r[0]), int(r[1]) + 1):
            return True
    return False

blankPassed = False
with open(file, "r", encoding="utf8") as f:
    for x in f:
        if x == "\n":
            blankPassed = True
        elif blankPassed:
            ids.append(int(x.strip()))
        else:
            ranges.append(x.strip().split('-'))

count = 0
for id in ids:
    if checkID(id):
        # print(id)
        count+=1
        
print(count)