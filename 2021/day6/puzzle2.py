with open("test.txt") as f:
  data = f.readlines()
  
vissen = []

#inlezen
for line in data:
    for i in line:
        if (i != "\x00" and i !="," and i !="\xff" and i !="\xfe"):
            vissen.append(int(i))
                   
print("initial state:",vissen)

for d in range(0,256):
    for v in range (0,len(vissen)):
        if (vissen[v] == 0):
            vissen[v] = 6
            vissen.append(8)
        else:  
            vissen[v] -=1   
            
print(len(vissen))

"""
som =0 
helpvis = []
for line in data:
    for i in line:
        if (i != "\x00" and i !="," and i !="\xff" and i !="\xfe"):
            vissen.append(int(i))
            getal = int(i)
            helpvis = []
            for d in range(0,256):
                if (getal == 0):
                    getal = 6
                    helpvis.append(8)
                else:  
                    getal -=1   
                for n in range (0,len(helpvis)):
                    if (helpvis[n] == 0):
                        helpvis[n] = 6
                        helpvis.append(8)
                    else:  
                       helpvis[n] -=1 
            som += 1 + len(helpvis)
            
print(len(vissen))
print(som)

""""



"""
def telVissen(vishelp):
    helpvis = []
    for v in range(0,len(vishelp)):
        for d in range(0,vishelp[v][1]):
            if (vissen[v] == 0):
                vissen[v] = 6
                tup = (8,d)
                helpvis.append(tup)
            else:  
                vissen[v] -=1 
    return helpvis

vishelp = []
for v in range(0,len(vissen)):
    for d in range(0,256):
        if (vissen[v] == 0):
            vissen[v] = 6
            tup = (8,d)
            vishelp.append(tup)
        else:  
            vissen[v] -=1  

vistest = vishelp
results = []
results.append(vissen)
while (vistest):
    results.append(vistest)
    vistest = telVissen(vistest)
            
            
som = 0
for a in results:
    som += len(a)
    
print(som)
"""