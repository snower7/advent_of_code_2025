import sys

file = "test.txt" if sys.argv[1] == "test" else "input.txt"


equations = []
with open(file, "r", encoding="utf8") as f:
    for x in f:
        eq = x.strip().split()
        # print(eq)
        if equations == []:
            for i in range(len(eq)):
                equations.append([eq[i]])
        else:
            for i in range(len(equations)):
                # print(eq[i])
                equations[i].append(eq[i])
    
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
        # print(len(e[1]) ,count)
    total += count
    
print(total)