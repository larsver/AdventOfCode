import numpy
import sys


with open("input.txt") as f:
  data = f.readlines()

crabs_pos = []

#get crab positions
for line in data:
    crab_list = line.split(",")
for c in crab_list:
    pos = c.strip()
    crabs_pos.append(int(pos))

def sumUp(x):
    return x* (x-1) // 2

least = sys.maxsize

maxrange = 0
for r in crabs_pos:
    if r >maxrange:
        maxrange=r

for m in range(0,maxrange):
    value = 0
    for i in range(0,len(crabs_pos)):
        value += sumUp(abs(crabs_pos[i]-m)+1)
    if value < least:
        least = value
    
print(least)

