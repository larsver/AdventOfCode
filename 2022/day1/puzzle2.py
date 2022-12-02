file = open("input.txt")

current = 0
highest = 0
list = []

for l in file:
    if len(l) == 1 :
        list.append(current)
        if current > highest:
            highest = current
        current = 0

    else :
        current += int(l)

# print(highest)
# print(list)
list.sort()
# print(list)

length = len(list)
print(list[length-1]+list[length-2]+list[length-3])
file.close()