import textwrap
file = open("input.txt")


sum = 0

for l in file:
    print(l)
    length = len(l)
    part1 = slice(0,length//2)
    part2 = slice(length//2,length)
    
    string1 = l[part1]
    string2 = l[part2]
    print(string1)
    print(string2)
    common = set(string1).intersection(string2)
    common = str(common)
    print(common[2])
    print(ord(common[2]))
    if (common[2].isupper()):
        print(ord(common[2]) - ord('A') + 27)
        sum += ord(common[2]) - ord('A') + 27
    
    else :
        print(ord(common[2]) - ord('a') + 1)
        sum += ord(common[2]) - ord('a') + 1
    

print("")
print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))
print(sum)
file.close()