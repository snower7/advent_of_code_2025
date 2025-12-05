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
            break
        else:
            ranges.append(x.strip().split("-"))

ranges.sort(key=lambda r: int(r[0]))
# print(ranges)
changed = False
count = 0
prevRange = [0, 0]
for r in ranges:
    r = [int(r[0]), int(r[1])]
    # print("r:", r)
    if r[0] >= prevRange[0] and r[0] <= prevRange[1] and r[1] > prevRange[1]:
        # print(r[1] - prevRange[1])
        changed = True
        count += r[1] - prevRange[1]
    elif r[1] > prevRange[1]:
        # print(r[1] - r[0] + 1)
        changed = True
        count += r[1] - r[0] + 1
    if changed:
        prevRange = r
        changed = False
    
print(count)