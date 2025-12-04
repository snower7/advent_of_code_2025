import re
import math

number = 50
count = 0

test = False

file = "input.txt" if not test else "testinput.txt"

with open(file, "r", encoding="utf8") as f:
    for x in f:
        amount = int(x[1:])
        clicks = amount % 100
        count += math.floor(amount / 100)
        if amount > 99:
            print("Amount = ", math.floor(amount / 100))
        if (re.search("R", x)):
            if 100 - number <= clicks:
                number = clicks - (100 - number)
                if not number == 0 and clicks > 0:
                    print("Right")
                    count+=1
            else:
                number += clicks 
        if(re.search("L", x)):
            if number == 0:
                count -= 1
            if number < clicks:
                number = 100 - (clicks - number)
                if not number == 0:
                    print("Left")
                    count+=1
            else:
                number -= clicks 
        if number == 0 and clicks > 0:
            print("Landed")
            count+=1
        print("Instruction: ", x.strip(), "\nNumber: ", number, "\n")
                
print(count)