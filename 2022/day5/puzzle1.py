import numpy as np
import re

file = open("input.txt")

oplossing = ""

stacks = False
lines = file.readlines()
aant_col = 0
aant_row = 0

for i in range (0,len(lines)):
    if lines[i].strip() == "" :
        print("ok")
        aant_row = i-1
        help = lines[i-1].strip().split(" ")
        aant_col = help[len(help)-1]
        print(aant_row)
        print(aant_col)
        break

stacks = []
for row in range(0,aant_row+1):     
    help = []
    stacks.append(help)

for j in range(aant_row-1,0-1,-1):
    # print(lines[j])
    # print(lines[j].strip("\n").split(" "))
    help = lines[j]
    tel = 0
    for t in range(1,len(help)-1,4):
        print(t," : ",help[t])
        if not(help[t] == " "):
            stacks[tel].append(help[t])
        tel += 1

print(stacks)   #stacks created

print(lines[aant_row+2])
for a in range(aant_row+2,len(lines)):
    print(lines[a])
    x = re.search("move (.*) from (.) to (.)", lines[a].strip("\n"))
    aant = int(x[1])
    van = int(x[2])
    naar = int(x[3])

    while aant > 0:
        # print("van:",stacks[van-1])
        test = stacks[van-1].pop()
        # print(test)
        # print("van:",stacks[van-1])

        # print("naar",stacks[naar-1])
        stacks[naar-1].append(test)
        # print("naar",stacks[naar-1])
        aant -= 1


for b in range(0,len(stacks)):
    print(stacks[b])
    help = stacks[b]
    oplossing = oplossing + help[len(help)-1]
# print(stacks)
print(oplossing)

file.close()