import sys

file = "test.txt" if sys.argv[1] == "test" else "input.txt"

with open(file, "r", encoding="utf8") as f:
    for x in f:
        content = 0