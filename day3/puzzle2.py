import copy 

with open("input.txt") as f:
  data = f.readlines()
  
lijst = []
for i in range(0,len(data)):
    lijst.append(data[i].strip())
lijst2 = copy.deepcopy(lijst)    
length = len(lijst[0])  

plaats = 0
while (len(lijst) > 1) and (plaats<length):
    count0 = 0
    count1 = 0
    for getal in lijst:
        if (getal[plaats] =="1"):
            count1 +=1
        else :
            count0 +=1
    helplijst = copy.deepcopy(lijst) 
    for get in lijst:
        if (count1 >= count0):
            if (get[plaats] == '0'):
                helplijst.remove(get)
        else:
            if (get[plaats] == '1'):
                helplijst.remove(get)
    lijst = helplijst
    plaats +=1


plaats = 0
while (len(lijst2) > 1) and (plaats<length):
    count0 = 0
    count1 = 0
    for getal in lijst2:
        if (getal[plaats] =="1"):
            count1 +=1
        else :
            count0 +=1
    helplijst2 = copy.deepcopy(lijst2) 
    for get in lijst2:
        if (count0 <= count1):
            if (get[plaats] == '1'):
                 helplijst2.remove(get)
        else:
            if (get[plaats] == '0'):
                helplijst2.remove(get)

    lijst2 = helplijst2
    plaats += 1
    
print(lijst[0])   
oxygenRat = int(lijst[0], 2)
print(oxygenRat)
print(lijst2[0])   
CO2Rat = int(lijst2[0], 2)
print(CO2Rat)
solution = CO2Rat * oxygenRat 
print(solution)

f.close()