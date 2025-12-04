import sys

def nextNum(left, picks, num):
    # print("String:", left, "\nNumber:", num, "\n")
    if picks == 0:
        return num
    
    sorting = list(left)
    sorting.sort(reverse=True)
    i = 0
    while(i < len(sorting) - 1 and left.index(sorting[i]) > len(left) - picks):
        i += 1
    num += sorting[i]
    
    return nextNum(left[left.index(sorting[i]) + 1:], picks - 1, num)

file = "test.txt" if sys.argv[1] == "test" else "input.txt"

sum = 0

with open(file, "r", encoding="utf8") as f:
    for x in f:
        x = x.strip()
        amount = nextNum(x, 12, "")
        print(amount)
        sum += int(amount)
print("\nSum: ", sum)