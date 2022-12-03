file = open("input.txt")

som = 0

for l in file:
    print(l)
    getal = int(l)
    fuels = []

    help = (getal//3)-2
    fuels.append(help)
    while help > 0 :
        help2 = (help//3)-2
        if help2 < 0 :
            break
        help = help2
        fuels.append(help)

    print("fuels",fuels)

    for i in fuels:
        som += i

print("som =",som)
file.close()