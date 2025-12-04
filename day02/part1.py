import sys
import re
import math
def checkID(id):
    return False if id[0:math.floor(len(id) / 2)] == id[math.floor(len(id) / 2):] else True

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