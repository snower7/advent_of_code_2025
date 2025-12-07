import sys

file = "test.txt" if sys.argv[1] == "test" else "input.txt"

map = []
with open(file, "r", encoding="utf8") as f:
    for x in f:
        temp = list(x.strip())
        if "S" in temp:
            map.append(temp)
        elif "^" in temp:
            map.append(temp)
      
beams = map.pop(0) 
beams[beams.index("S")] = "|"
    
beam_dict = {}
count = 0
def split(map_index: int, beam: list):
    if map_index == len(map):
        # print("found", beam)
        return 1
    c = 0
    if beam_dict.get(str(map_index)) != None and beam_dict[str(map_index)].get(str(beam.index("|"))) != None:
            return beam_dict[str(map_index)][str(beam.index("|"))]
    for s in range(len(beam)):
        if map[map_index][s] == "^" and beam[s] == "|":
            if s != 0:
                a = beam.copy()
                a[s] = "."
                a[s-1] = "|"
                # print("l", a)
                
                c += split(map_index + 1, a)
            else:
                c += 1
            if s != len(map[map_index]) - 2:
                a = beam.copy()
                a[s+1] = "|"
                a[s] = "."
                # print("r", a)
                c += split(map_index + 1, a)
            else:
                c += 1
        elif beam[s] == "|":
            # print("c", beam)
            c += split(map_index + 1, beam)
    # print(map_index, beam.index("|"))
    if beam_dict.get(str(map_index)) == None:
        beam_dict[str(map_index)] = {}
    # print(beam_dict)
    if beam_dict[str(map_index)].get(str(beam.index("|"))) == None:
        beam_dict[str(map_index)][str(beam.index("|"))] = c
    return c

print(split(0, beams))
    