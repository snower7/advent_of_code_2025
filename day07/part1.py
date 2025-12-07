import sys

file = "test.txt" if sys.argv[1] == "test" else "input.txt"

map = []
with open(file, "r", encoding="utf8") as f:
    for x in f:
        map.append(list(x.strip()))
      
beams = map.pop(0) 
beams[beams.index("S")] = "|"
    
count = 0
print(beams, "\n")
for m in map:
    # print(m)
    for s in range(len(m)):
        if m[s] == "^" and beams[s] == "|":
            count+=1
            beams[s] = "."
            # print(m, s, count)
            if s != 0:
                beams[s-1] = "|"
            if s != len(m) - 2:
                beams[s+1] = "|"
# print(beams)
print(count)
    