import sys

file = "test.txt" if sys.argv[1] == "test" else "input.txt"

coords = []
with open(file, "r", encoding="utf8") as f:
    for x in f:
        c = x.strip().split(",")
        coords.append([int(c[0]), int(c[1])])

largest = 0
for i in range(len(coords) - 1):
    for j in range(i + 1, len(coords)):
        tileA = coords[i]
        tileB = coords[j]
        area = (abs(tileA[0] - tileB[0]) + 1)* (abs(tileA[1] - tileB[1]) + 1)
        if largest < area:
            largest = area

print(largest)