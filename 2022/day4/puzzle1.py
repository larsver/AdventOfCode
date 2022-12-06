file = open("input.txt")

oplossing = 0

for l in file:
    print(l)
    help = (l.strip()).split(',')
    print(help)
    section1 = help[0].split('-')
    section2 = help[1].split('-')
    print(section1)
    print(section2)

    if (int(section1[0]) >= int(section2[0]) and int(section1[1]) <= int(section2[1])): #section1 in section2
        oplossing += 1
    elif (int(section2[0]) >= int(section1[0]) and int(section2[1]) <= int(section1[1])): #section2 in section1
        oplossing += 1

print(oplossing)
file.close()