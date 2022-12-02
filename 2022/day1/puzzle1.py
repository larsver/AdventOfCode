file = open("input.txt")

current = 0
highest = 0

for l in file:
    if len(l) == 1 :
        if current > highest:
            highest = current
        current = 0

    else :
        current += int(l)

print(highest)
file.close()