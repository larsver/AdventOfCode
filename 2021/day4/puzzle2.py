import numpy as np

def checkBingo(bkaart2):
    for r in range(0,5):
        result = np.all(bkaart2[r] == 1)
        if result:
            return True
        
    for k in range(0,5):
        ok = 0
        for r in range(0,5):
            if (bkaart2[r][k] == 1) :
                ok +=1
                
        if (ok == 5) :
            return True
    
    
    return False
def maakOngeldig(bkaart,a):
    for r in range(0,5):
        for k in range(0,5):
            bkaart[r][k] = a
    
def stop(bkaart,bkaart2,a):
    print("bingo!!")
    print(bkaart)
    print(bkaart2)
    print(a)
    usum = 0
    for r in range(0,5):
        for k in range(0,5):
            if (bkaart2[r][k]==0):
                usum += bkaart[r][k]
    print(usum)
    print(usum*int(a))

with open("input.txt") as f:
  getallen =f.readline()
  data = f.readlines()
 
print(getallen)
bingo = getallen.split(",")
print bingo

bkaart = []
bkaart2 = []
count = 0
kaartcount = 0
for line in data:
    if line == "\n":
        #print("empty")
        bkaart.append(np.zeros( (5, 5) ))
        bkaart2.append(np.zeros( (5, 5) ))
        count = 0
        kaartcount += 1
    else :
        #print(line)
        linehelp = []
        for i in range(0,len(line)-1,3):
            linehelp.append((line[i]+line[i+1]).strip())
            #print(linehelp)
        for j in range(0,len(linehelp)) : 
            bkaart[kaartcount-1][count][j] = linehelp[j]
        #print(bkaart[kaartcount-1])
        count += 1


for a in bingo:
    #print(a)
    for b in range(0,len(bkaart)):
        for rij in range(0,5):
            for kol in range(0,5):
                if (int(a) == bkaart[b][rij][kol]):
                    bkaart2[b][rij][kol] = 1
                    #print(bkaart2[b])
                    if (checkBingo(bkaart2[b]) ):
                        
                        
                        stop(bkaart[b],bkaart2[b],a)
                        maakOngeldig(bkaart2[b],2)
                        maakOngeldig(bkaart[b],0)


f.close()
  