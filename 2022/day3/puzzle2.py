import textwrap
file = open("input.txt")


sum = 0
i = 0
print(file)
lines = file.readlines()
print(lines)
print(len(lines))
while i < len(lines):
    
    string1 = lines[i].strip()
    string2 = lines[i+1].strip()
    string3 = lines[i+2].strip()
    print(string1)
    print(string2)
    print(string3)
    print("")
    common = (set(string1).intersection(string2)).intersection(string3)
    print(common)
    common = str(common)
    print(common[2])
    help = common[2]
    if (help.isupper()):
        sum += ord(help) - ord('A') + 27
    
    else :
        sum += ord(help) - ord('a') + 1


    i += 3

print(sum)
file.close()