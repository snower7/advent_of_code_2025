import sys
from operator import itemgetter
from PIL import Image

file = "test copy.txt" if sys.argv[1] == "test" else "input.txt"

coords = []
with open(file, "r", encoding="utf8") as f:
    for x in f:
        c = x.strip().split(",")
        coords.append([int(c[0]), int(c[1])])

coords.sort(key=itemgetter(0,1))

x_coords = set()
y_coords = set()
y_dict = {} # y_index : [[x, y], [x, y]]
x_dict = {}
for c in coords:
    x_coords.add(c[0])
    y_coords.add(c[1])
    try:
        y_dict[c[1]].append(c)
    except:
        y_dict[c[1]] = [c]
    
    try:
        x_dict[c[0]].append(c)
    except:
        x_dict[c[0]] = [c]
    
x_coords = list(x_coords)
y_coords = list(y_coords)
x_coords.sort()
y_coords.sort()
map = [["." for _ in range(len(x_coords))] for _ in range(len(y_coords))]


map_coords = []
for c in coords:
    # print(c, y_coords.index(c[1]), x_coords.index(c[0]))
    map_coords.append([x_coords.index(c[0]), y_coords.index(c[1])])
    map[y_coords.index(c[1])][x_coords.index(c[0])] = "X"
    
    
def fence():
    y_sort = map_coords.copy()
    y_sort.sort(key = itemgetter(1,0))
    
    x_sort = map_coords.copy()
    x_sort.sort(key = itemgetter(0,1))
    # print(y_sort, "\n", x_sort)
    for i in range(0, len(y_sort), 2):
        # print(y_sort[i], y_sort[i + 1])
        for j in range(y_sort[i][0] + 1, y_sort[i+1][0]):
            map[y_sort[i][1]][j] = "-"
            # print(j, i)
            
    for i in range(0, len(x_sort), 2):
        for j in range(x_sort[i][1] + 1, x_sort[i+1][1]):
            map[j][x_sort[i][0]] = "|"
            
    # print("y_coords", y_coords)
    for y in y_coords:
        xs = y_dict[y]
        for i in range(0, len(xs), 2):
            # print([y_coords.index(y)], [x_coords.index(xs[0][0])])
            if x_dict[xs[i][0]].index(xs[i]) % 2 != 0:
                # print("L")
                map[y_coords.index(y)][x_coords.index(xs[i][0])] = "L"
            else:
                # print("r")
                map[y_coords.index(y)][x_coords.index(xs[i][0])] = "r"
                
            if x_dict[xs[i+1][0]].index(xs[i+1]) % 2 != 0:
                # print("J")
                map[y_coords.index(y)][x_coords.index(xs[i+1][0])] = "J"
            else:
                # print("7")
                map[y_coords.index(y)][x_coords.index(xs[i+1][0])] = "7"
            # print(xs)
        
print("fencing")
fence()
    
# def spread(y, x):
#     # print(y ,x)
#     try:
#         if map[y][x] == "X":
#             return
#     except:
#         return
#     map[y][x] = "X"
#     spread(y - 1, x)
#     spread(y + 1, x)
#     spread(y, x + 1)
#     spread(y, x - 1)
    
def fill():
    for y in range(len(map)):
        inside = False
        prev = "."
        for x in range(len(map[0])):
            coord = map[y][x]
            if (prev == "r" and coord == "J") or prev == "L" and coord == "7":
                inside = not inside
            elif coord == "|":
                inside = not inside
            elif inside and coord == ".":
                # print(y, x)
                map[y][x] = "X"
            elif coord == "r" or coord == "L":
                prev = coord
            
        #     print(inside, y[x])
        # print()
    
with open("output1.txt", "w", encoding="utf8") as f:
    for m in map:
        for i in m:
            f.write(i)
        f.write("\n")
print("filling")
fill()
with open("output2.txt", "w", encoding="utf8") as f:
    for m in map:
        for i in m:
            f.write(i)
        f.write("\n")

areas = {}
for i in range(len(coords) - 1):
    for j in range(i + 1, len(coords)):
        tileA = coords[i]
        tileB = coords[j]
        area = (abs(tileA[0] - tileB[0]) + 1) * (abs(tileA[1] - tileB[1]) + 1)
        try:
            areas[area].append([tileA, tileB])
        except:
            areas[area] = [[tileA, tileB]]
        
keys = list(areas.keys())
keys.sort(reverse=True)
# print(keys)


def check_valid(tiles):
    ys = [tiles[0][1], tiles[1][1]]
    xs = [tiles[0][0], tiles[1][0]]
    ys.sort()
    xs.sort()
    # print(tiles)
    # print()
    for y in range(y_coords.index(ys[0]), y_coords.index(ys[1]) + 1):
        # print(y, xs)
        if map[y][x_coords.index(xs[0])] == ".":
            # print("Failed:", y, x_coords.index(xs[0]))
            return False
        if map[y][x_coords.index(xs[1])] == ".":
            # print("Failed:", y, x_coords.index(xs[1]))
            return False
    for x in range(x_coords.index(xs[0]), x_coords.index(xs[1]) + 1):
        # print(ys, xs)
        if map[y_coords.index(ys[0])][x] == ".":
            # print("Failed:", y_coords.index(ys[0]), x)
            return False
        if map[y_coords.index(ys[1])][x] == ".":
            # print("Failed:", y_coords.index(ys[1]), x)
            return False
    for y in range(y_coords.index(ys[0]) + 1, y_coords.index(ys[1])):
        for x in range(x_coords.index(xs[0]) + 1, x_coords.index(xs[1])):
            if map[y][x] != "X":
                return False
            
    return True
    
found = False
result = []
for k in keys:
    for pair in areas[k]:
        print("Checking:" , k, ":", pair)
        if check_valid(pair):
            print("Coords:", pair)
            print("Result", k)
            result = pair
            found = True
            break
    if found:
        break
    
img = Image.new(mode="RGB", size=(len(map[0]), len(map)), color=(255,255,255))
pixels = img.load()
for x in range(img.size[0]):
    for y in range(img.size[1]):
        if map[y][x] == "X":
            pixels[x,y] = (255,155,155)
        elif map[y][x] != ".":
            pixels[x,y] = (0,0,0)
            
            
# img.show()
xs = [result[0][0], result[1][0]]
ys = [result[0][1], result[1][1]]
xs.sort()
ys.sort()
for x in range(x_coords.index(xs[0]), x_coords.index(xs[1]) + 1):
    for y in range(y_coords.index(ys[0]), y_coords.index(ys[1]) + 1):
        if pixels[x,y] == (255,255,255):
            pixels[x,y] = (0, 26, 255)
        elif pixels[x,y] == (0,0,0):
            pixels[x,y] = (65, 255, 36)
        else:
            pixels[x,y] = (255, 149, 36)
            
img.show()