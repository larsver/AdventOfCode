import numpy as np

file = open("input.txt")

oplossing = 0
lines = file.readlines()
# print(lines)

lijnen = []
for i in lines:
    help = i.strip()
    chars = [int(x) for x in help]
    lijnen.append(chars)

bos = np.array(lijnen)
# print(bos)
# print(len(bos))
# print(len(bos[0]))
aant_rows = len(bos)
aant_cols = len(bos[0])

for r in range (0, aant_rows):
    row = bos[r]
    for c in range (0, aant_cols):
        boom = row[c]
        print(boom, "row :",r, " col: ", c)
        
        if (r in (0,aant_rows-1) or c in (0,aant_cols-1)):
            continue
        else:
            #check links
            links = 0
            kol = c
            while kol > 0 :
                if bos[r][kol-1] >= bos[r][c] :
                    links += 1
                    break
                links += 1
                kol -= 1
            print(links)
            
            # check rechts
            rechts = 0
            kol = c
            while kol < aant_cols-1 :
                if bos[r][kol+1] >= bos[r][c] :
                    rechts += 1
                    break
                rechts += 1
                kol += 1
            print(rechts)
            
            # check boven
            boven = 0
            rij = r
            while rij > 0 :
                if bos[rij-1][c] >= bos[r][c] :
                    boven += 1
                    break
                boven += 1
                rij -= 1
            print(boven)
            
            # check onder
            onder = 0
            rij = r
            while rij < aant_rows-1 :
                if bos[rij+1][c] >= bos[r][c] :
                    onder += 1
                    break
                onder += 1
                rij += 1
            print (onder)

            if (links*rechts*boven*onder) > oplossing:
                oplossing = (links*rechts*boven*onder)

print(oplossing)

file.close()