with open("input.txt") as f:
  data = f.read()
  
floor = 0
pos = 0
for k in data:
    if (k=="("):
        floor += 1
    elif(k == ")"):
        floor -= 1
    pos += 1
    if (floor<0):
        break
print(floor)
print(pos)