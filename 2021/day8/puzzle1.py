with open("input.txt") as f:
  data = f.readlines()

#print(data)
codes = []
for line in data:
    print(line)
    print(line.split("|"))
    rechterdeel = line.split("|")[1]
    print(rechterdeel.split())
    help = rechterdeel.split()
    for a in help:    
        codes.append(a.strip())

count = 0
for c in codes:
    print(c)
    if (len(c) == 2 or len(c) == 4 or len(c) == 3 or len(c) == 7):
        count += 1
        
print(count)
