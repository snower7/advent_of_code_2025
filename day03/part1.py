import sys

file = "test.txt" if sys.argv[1] == "test" else "input.txt"

sum = 0

with open(file, "r", encoding="utf8") as f:
    for x in f:
        x = x.strip()
        batteries = list(x)
        batteries.sort(reverse=True)
        if (x.index(batteries[0]) == len(x) - 1):
            amount = batteries[1] + batteries[0]
        else:
            second = list(x[x.index(batteries[0]) + 1:])
            second.sort(reverse=True)
            # print(second)
            amount = batteries[0] + second[0]
        sum += int(amount)
        print(amount.strip())
        
print("\nSum: ", sum)