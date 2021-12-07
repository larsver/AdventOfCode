import numpy

with open("input.txt") as f:
  data = f.readlines()

crabs_pos = []
crabs_fuel = []
print(data)

for line in data:
    crab_list = line.split(",")
for c in crab_list:
    pos = c.strip()
    crabs_pos.append(int(pos))
    crabs_fuel.append(0)
print(crabs_pos)

median_crabs = numpy.median(crabs_pos)
print(median_crabs)

for i in range(0,len(crabs_pos)):
    crabs_fuel[i] = abs(crabs_pos[i] - median_crabs)
    
print(crabs_fuel)
result = 0
for f in crabs_fuel:
    result += f
    
print(result)