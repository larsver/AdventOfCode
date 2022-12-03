file = open("input.txt")

som = 0

for l in file:
    print(l)
    getal = int(l)
    help = (getal//3)-2
    som += help

print(som)
file.close()