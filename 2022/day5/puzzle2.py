import numpy as np
import re

file = open("input.txt")

oplossing = ""
lines = file.readlines()
aant_col = 0
aant_row = 0

for i in range (0,len(lines)):
    if lines[i].strip() == "" :
        aant_row = i-1
        help = lines[i-1].strip().split(" ")
        aant_col = help[len(help)-1]
        break

stacks = []
for row in range(0,aant_row+1):     
    help = []
    stacks.append(help)

for j in range(aant_row-1,0-1,-1):
    help = lines[j]
    tel = 0
    for t in range(1,len(help)-1,4):
        if not(help[t] == " "):
            stacks[tel].append(help[t])
        tel += 1

print(stacks)   #stacks created

for a in range(aant_row+2,len(lines)):
    x = re.search("move (.*) from (.) to (.)", lines[a].strip("\n"))
    aant = int(x[1])
    van = int(x[2])
    naar = int(x[3])

    print(lines[a])
    print(stacks[van-1])
    helpstack = []
    while aant > 0:
        test = stacks[van-1].pop()
        helpstack.append(test)
        aant -= 1
    
    print(helpstack)
    for s in range(len(helpstack)-1,-1,-1):
        stacks[naar-1].append(helpstack[s])


#oplossing berekening
for b in range(0,len(stacks)):
    print(stacks[b])
    help = stacks[b]
    oplossing = oplossing + help[len(help)-1]
# print(stacks)
print(oplossing)

file.close()