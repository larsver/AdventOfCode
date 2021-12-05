import numpy as np

with open("input.txt") as f:
  data = f.readlines()
  
xCo1 = []
yCo1 = []
xCo2 = []
yCo2 = []
  
#inlezen
for line in data:
    #print(line)
    Co = line.split("->")
    help = Co[0].split(",")
    xCo1.append(int(help[0].strip()))
    yCo1.append(int(help[1].strip()))
    #print(xCo1[len(xCo1)-1])
    #print(yCo1[len(yCo1)-1])
    help = Co[1].split(",")
    xCo2.append(int(help[0].strip()))
    yCo2.append(int(help[1].strip()))
    #print(xCo2[len(xCo2)-1])
    #print(yCo2[len(yCo2)-1])

grootsteX = 0
grootsteY = 0
for i in range(0,len(data)):
    if (int(xCo1[i]) > grootsteX):
        grootsteX = int(xCo1[i])
    if (int(yCo1[i]) > grootsteY):
        grootsteY = int(yCo1[i])
    if (int(xCo2[i]) > grootsteX):
        grootsteX = int(xCo2[i])
    if (int(yCo2[i]) > grootsteY):
        grootsteY = int(yCo2[i])
print(grootsteX)
print(grootsteY)

veld = np.zeros( (grootsteY+1, grootsteX+1) )
print(veld)
"""
for j in range(0,len(xCo1)-1):
    if (xCo1[j] == xCo2[j]) :
        if (yCo1[j] < yCo2[j]):
            for y in range(yCo1[j],yCo2[j]+1):
                veld[xCo1[j]][y] += 1
        else:
            for y in range(yCo2[j],yCo1[j]+1):
                veld[xCo1[j]][y] += 1
    elif (yCo1[j] == yCo2[j]) :
        if (xCo1[j] < xCo2[j]):
            for x in range(xCo1[j],xCo2[j]+1):
                veld[x][yCo1[j]] += 1
        else:
            for x in range(xCo2[j],xCo1[j]+1):
                veld[x][yCo1[j]] += 1
 """
for j in range(0,len(xCo1)):
    if (xCo1[j] == xCo2[j]) :
        if (yCo1[j] < yCo2[j]):
            for y in range(yCo1[j],yCo2[j]+1):
                veld[y][xCo1[j]] += 1
        else:
            for y in range(yCo2[j],yCo1[j]+1):
                veld[y][xCo1[j]] += 1
    elif (yCo1[j] == yCo2[j]) :
        if (xCo1[j] < xCo2[j]):
            for x in range(xCo1[j],xCo2[j]+1):
                veld[yCo1[j]][x] += 1
        else:
            for x in range(xCo2[j],xCo1[j]+1):
                veld[yCo1[j]][x] += 1


opl = 0
for a in veld:
    for b in a:
        if (b>=2):
            opl +=1
print(veld)  
print(opl)
    
    