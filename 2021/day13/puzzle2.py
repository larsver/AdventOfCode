import numpy as np

with open("input.txt") as f:
  data = f.readlines()

folds = []
coordinaten = []
#inlezen
for line in data:
    if (line[0]=="f"):
        fold = line.split()
        fold = fold[2].split('=')
        #print(fold)
        folds.append(fold)
    else :
        #print(line)
        co = line.strip()
        co = co.split(',')
        #print(co)
        if (len(co) == 2):
            coordinaten.append(co)
grootsteX = 0
grootsteY = 0
for c in coordinaten:
    if(int(c[0])>grootsteX):
        grootsteX =int(c[0])
    if(int(c[1])>grootsteY):
        grootsteY=int(c[1])
        
#print(grootsteX)
#print(grootsteY)

matrix = np.empty((grootsteY+1, grootsteX+1), dtype=object)
#print(matrix)

#print(coordinaten)
#print(folds)

for c in coordinaten:
    matrix[int(c[1])][int(c[0])] = '#'
print(matrix)

#print(matrix)

for f in range(0,len(folds)):
    foldas = folds[f][0]
    foldline = int(folds[f][1] )
    if (foldas =="y"):
        new_matrix = np.empty((foldline, grootsteX+1), dtype=object)  
        print(new_matrix)
        for i in range(0,grootsteX+1):
            for j in range(0,foldline):
                if (matrix[j][i] == '#'):
                    new_matrix[j][i] ='#'
                if (matrix[grootsteY-j][i]=='#'):
                    new_matrix[j][i] ='#'
    elif (foldas =="x"):
        new_matrix = np.empty((grootsteY+1, foldline), dtype=object)  
        print(new_matrix)
        for i in range(0,foldline):
            for j in range(0,grootsteY+1):
                if (matrix[j][i] == '#'):
                    new_matrix[j][i] ='#'
                if (matrix[j][grootsteX-i]=='#'):
                    new_matrix[j][i] ='#'
    
    print (new_matrix)
    matrix = new_matrix
tel = 0
for a in new_matrix:
    for b in a:
        if b=='#':
            tel+=1
print(tel)