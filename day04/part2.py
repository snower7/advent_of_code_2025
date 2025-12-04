import sys

file = "test.txt" if sys.argv[1] == "test" else "input.txt"

map = []

with open(file, "r", encoding="utf8") as f:
    for x in f:
        map.append(list(x.strip()))

sum = 0
run_num = 0
count = -1
while not count == 0:
    # run_num += 1
    # for y in map:
    #     for x in y:
    #         print(x, end="")
    #     print("")
    # print()
    count = 0
        
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "@":
                transforms_y = [0]
                transforms_x = [0]
                if not y == 0:
                    transforms_y.append(-1)
                if not x == 0:
                    transforms_x.append(-1)
                if not y == len(map) - 1:
                    transforms_y.append(1)
                if not x == len(map[0]) - 1:
                    transforms_x.append(1)
                blocked = 0
                if (len(transforms_x) * len(transforms_y) < 4):
                    map[y][x] = "."
                    count += 1
                else:
                    for ty in transforms_y:
                        for tx in transforms_x:
                            if ty == 0 and tx == 0:
                                continue
                            elif map[y + ty][x+tx] == "@":
                                blocked += 1
                    if blocked < 4:
                        map[y][x] = "."
                        count+=1
    sum += count
print(sum)