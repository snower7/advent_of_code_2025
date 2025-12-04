import re

number = 50
count = 0
test = False

file = "input.txt" if not test else "testinput.txt"

with open(file, "r", encoding="utf8") as f:
    for x in f:
        clicks = int(x[1:]) % 100
        if (re.search("R", x)):
            if 100 - number <= clicks:
                number = clicks - (100 - number)
            else:
                number += clicks 
        if(re.search("L", x)):
            if number < clicks:
                number = 100 - (clicks - number)
            else:
                number -= clicks 
        if number == 0:
            count+=1
        print("Instruction: ", x.strip(), "\nNumber: ", number, "\n")
                
print(number)                
print(count)