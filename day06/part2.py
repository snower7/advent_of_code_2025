import sys
import re

file = "test.txt" if sys.argv[1] == "test" else "input.txt"


equations = []
normal = []
with open(file, "r", encoding="utf8") as f:
    for x in f:
        eq = list(re.sub("\n", "", x))
        # print(eq)
        normal.append(eq)
    
operations = "".join(normal.pop(-1)).split()
temp = [""]

for i in range(len(normal[0])):
    notBlank = False
    for n in normal:
        if n[i] != " ":
            notBlank = True
            temp[-1] += n[i]
    if notBlank:
        temp.append("")
    else:
        temp.pop(-1)
        temp.append(operations.pop(0))
        equations.append(temp)
        temp = [""]
        # print(n[i])
    # print(temp)
temp.pop(-1)
temp.append(operations.pop(0))
equations.append(temp)
# print(equations)
total = 0           
for e in equations:
    # print(e)
    mult = True if e[-1] == "*" else False
    # print(mult)
    count = 0
    for num in range(len(e) - 1):
        if mult:
            if count == 0:
                count = 1
            count *= int(e[num])
        else:
            count += int(e[num])
        # print(len(e[num]) ,count)
    total += count
    
print(total)