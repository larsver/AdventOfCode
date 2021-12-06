import numpy as np

with open("test.txt") as f:
  data = f.readlines()
  
vissen = []
  
#inlezen
for line in data:
    for i in line:
        if (i != "\x00" and i !="," and i !="\xff" and i !="\xfe"):
            vissen.append(int(i))
                   
print("initial state:",vissen)

for d in range(0,80):
    for v in range (0,len(vissen)):
        if (vissen[v] == 0):
            vissen[v] = 6
            vissen.append(8)
        else:  
            vissen[v] -=1
        
    #print(d+1,vissen)      

print(len(vissen))
