import sys
import re

def checkID(id):
    for j in range(1, len(id)):
        num = id[0:j]
        if (re.search("^(" + num + "){1,}$", id[j:])):
            print("Invalid: ", id)
            return False
    return True

file = "test.txt" if sys.argv[1] == "test" else "input.txt"

ranges = []

with open(file, "r", encoding="utf8") as f:
    for x in f:
        ranges = x.strip().split(",")
        
count = 0
for r in ranges:
    limits = r.split("-")
    for id in range(int(limits[0]), int(limits[1]) + 1):
        count += 0 if checkID(str(id)) else id
        
print(count)