import numpy as np

file = open("input.txt")

oplossing = 0

lines = file.readlines()
print(lines)

lijnen = []
for i in lines:
    help = i.strip()
    chars = [int(x) for x in help]
    lijnen.append(chars)

bos = np.array(lijnen)
print(bos)
print(len(bos))
print(len(bos[0]))
aant_rows = len(bos)
aant_cols = len(bos[0])

for r in range (0, aant_rows):
    row = bos[r]
    for c in range (0, aant_cols):
        boom = row[c]
        print(boom, "row :",r, " col: ", c)
        
        if (r in (0,aant_rows-1) or c in (0,aant_cols-1)):
            oplossing += 1
        else:
            nope = 0
            #check links
            kol = c
            while kol > 0 :
                # print("kol",kol)
                if bos[r][kol-1] >= bos[r][c] :
                    # print("ziet niet")
                    nope += 1
                    break
                kol -= 1
            
            # check rechts
            kol = c
            while kol < aant_cols-1 :
                # print("kol",kol)
                if bos[r][kol+1] >= bos[r][c] :
                    # print("ziet niet")
                    nope += 1
                    break
                kol += 1
            
            # check boven
            rij = r
            while rij > 0 :
                # print("rij",rij)
                if bos[rij-1][c] >= bos[r][c] :
                    # print("ziet niet")
                    nope += 1
                    break
                rij -= 1
            
            # check onder
            rij = r
            while rij < aant_rows-1 :
                # print("rij",rij)
                if bos[rij+1][c] >= bos[r][c] :
                    # print("ziet niet")
                    nope += 1
                    break
                rij += 1

            # count if zichtbaar
            if nope < 4:
                oplossing += 1
                print("ok")

print(oplossing)

file.close()