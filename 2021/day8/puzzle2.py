with open("input.txt") as f:
  data = f.readlines()

#print(data)
linkerdelen = []
rechterdelen = []
for line in data:
    #print(line)
    help = line.split("|")
    #print(help)
    linkerdeel = help[0].split()
    #print(linkerdeel)
    rechterdeel = help[1].split()
    #print(rechterdeel)
    
    linkerdelen.append(linkerdeel)
    rechterdelen.append(rechterdeel)


def bereken(linkerdeel,rechterdeel):
    nul = ""
    een = ""
    twee =""
    drie =""
    vier =""
    vijf =""
    zes =""
    zeven = ""
    acht = ""
    negen = ""

    lenVijf = [] #voor 5 en 2 en 3
    lenZes = [] #voor 6 en 9 en 0

    for c in linkerdeel:
        if (len(c) == 2):
            een = c
        if (len(c) == 4):
            vier = c
        if (len(c) == 3):
            zeven = c
        if (len(c) == 7):
            acht = c
        if (len(c) == 5):
            lenVijf.append(c)
        if (len(c) == 6):
            lenZes.append(c)

    # getallen code bepalen        
    for z in lenZes:
        if ((een[0] in z) and (een[1] in z)):   # een zit in 0 of 9
            if ((vier[0] in z) and (vier[1] in z) and (vier[2] in z) and (vier[3] in z)):   #vier zit in 0
                negen = z
            else:   #vier niet in 0
                nul = z
        else:           #1 zit niet in 6
            zes = z
    for v in lenVijf:
        if ((zeven[0] in v) and (zeven[1] in v) and (zeven[2] in v)):   #zeven niet in drie
            drie = v
        else:   #zeven niet in 5 of 2
            if ((v[0] in zes) and (v[1] in zes) and (v[2] in zes) and (v[3] in zes) and (v[4] in zes)): #vijf zit in zes
                vijf = v
            else :
                twee = v
    """           
    print(nul)
    print(een)
    print(twee)
    print(drie)
    print(vier)
    print(vijf)
    print(zes)
    print(zeven)
    print(acht)
    print(negen)
    """
    output = ""
    for c in rechterdeel:
        if (sorted(c) == sorted(nul)):
            output +="0"
        if (sorted(c) == sorted(een)):
            output +="1"
        if (sorted(c) == sorted(twee)):
            output +="2"
        if (sorted(c) == sorted(drie)):
            output +="3"
        if (sorted(c) == sorted(vier)):
            output += "4"
        if (sorted(c) == sorted(vijf)):
            output += "5"
        if (sorted(c) == sorted(zes)):
            output += "6"
        if (sorted(c) == sorted(zeven)):
            output += "7"
        if (sorted(c) == sorted(acht)):
            output += "8"
        if (sorted(c) == sorted(negen)):
            output += "9"
    return output

resultaten = []
for i in range(0,len(linkerdelen)):
    resultaten.append(bereken(linkerdelen[i],rechterdelen[i]))

som = 0
for r in resultaten:
    som += int(r)
print("som",som)