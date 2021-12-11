import numpy as np

def flash(matrix,aantRij,aantKol):
    """
    matrix[i-1][j-1] +=1
    matrix[i-1][j] +=1
    matrix[i-1][j+1] +=1
    matrix[i+1][j-1] +=1
    matrix[i+1][j] +=1
    matrix[i+1][j+1] +=1
    matrix[i][j11] +=1
    matrix[i][j+1] +=1
    """
    aantFlashes = 0
    for i in range(0,aantRij):
        for j in range(0,aantKol):
             if (matrix[i][j] > 9):
                matrix[i][j] = 0
                aantFlashes += 1
                
                if (i==0):
                    if (j==0):
                        if (matrix[i+1][j]!=0):
                            matrix[i+1][j] += 1
                        if (matrix[i+1][j+1]!=0):
                            matrix[i+1][j+1] += 1
                        if (matrix[i][j+1]!=0):
                            matrix[i][j+1] += 1
                    elif (j==aantKol-1):
                        if (matrix[i+1][j]!=0):
                            matrix[i+1][j] += 1
                        if (matrix[i+1][j-1]!=0):
                            matrix[i+1][j-1] += 1
                        if (matrix[i][j-1]!=0):
                            matrix[i][j-1] += 1
                    else:
                        if (matrix[i+1][j]!=0):
                            matrix[i+1][j] += 1
                        if (matrix[i+1][j-1]!=0):
                            matrix[i+1][j-1] += 1
                        if (matrix[i+1][j+1]!=0):
                            matrix[i+1][j+1] += 1
                        if (matrix[i][j-1]!=0):
                            matrix[i][j-1] += 1
                        if (matrix[i][j+1]!=0):
                            matrix[i][j+1] += 1 

                elif (i==aantRij-1):
                    if (j==0):
                        if (matrix[i-1][j]!=0):
                            matrix[i-1][j] += 1
                        if (matrix[i-1][j+1]!=0):
                            matrix[i-1][j+1] += 1
                        if (matrix[i][j+1]!=0):
                            matrix[i][j+1] += 1
                    elif (j==aantKol-1):
                        if (matrix[i-1][j]!=0):
                            matrix[i-1][j] += 1
                        if (matrix[i-1][j-1]!=0):
                            matrix[i-1][j-1] += 1
                        if (matrix[i][j-1]!=0):
                            matrix[i][j-1] += 1
                    else:
                        if (matrix[i-1][j]!=0):
                            matrix[i-1][j] += 1
                        if (matrix[i-1][j-1]!=0):
                            matrix[i-1][j-1] += 1
                        if (matrix[i-1][j+1]!=0):
                            matrix[i-1][j+1] += 1
                        if (matrix[i][j-1]!=0):
                            matrix[i][j-1] += 1
                        if (matrix[i][j+1]!=0):
                            matrix[i][j+1] += 1 
                            
                else :
                    if (j==0):
                        if (matrix[i-1][j]!=0):
                            matrix[i-1][j] += 1
                        if (matrix[i-1][j+1]!=0):
                            matrix[i-1][j+1] += 1
                        if (matrix[i][j+1]!=0):
                            matrix[i][j+1] += 1
                        if (matrix[i+1][j]!=0):
                            matrix[i+1][j] += 1
                        if (matrix[i+1][j+1]!=0):
                            matrix[i+1][j+1] += 1
                    elif (j==aantKol-1):
                        if (matrix[i-1][j]!=0):
                            matrix[i-1][j] += 1
                        if (matrix[i-1][j-1]!=0):
                            matrix[i-1][j-1] += 1
                        if (matrix[i][j-1]!=0):
                            matrix[i][j-1] += 1
                        if (matrix[i+1][j]!=0):
                            matrix[i+1][j] += 1
                        if (matrix[i+1][j-1]!=0):
                            matrix[i+1][j-1] += 1
                    else:
                        if (matrix[i-1][j-1]!=0):
                            matrix[i-1][j-1] +=1
                        if (matrix[i-1][j]!=0):
                            matrix[i-1][j] += 1
                        if (matrix[i-1][j+1]!=0):
                            matrix[i-1][j+1] += 1   
                        if (matrix[i+1][j-1]!=0):
                            matrix[i+1][j-1] += 1
                        if (matrix[i+1][j]!=0):
                            matrix[i+1][j] += 1
                        if (matrix[i+1][j+1]!=0):
                            matrix[i+1][j+1] += 1
                        if (matrix[i][j+1]!=0):
                            matrix[i][j+1] += 1
                        if (matrix[i][j-1]!=0):
                            matrix[i][j-1] += 1
             
    print(aantFlashes)
    if (aantFlashes == 0):
        return 0
    else:
        aantFlashes += flash(matrix,aantRij,aantKol)
        return aantFlashes

def checkSyn(matrix):
    for i in range(0,aantRij):
        for j in range(0,aantKol):
            if (matrix[i][j] !=0):
                return False ;
    return True


with open("input.txt") as f:
  data = f.readlines()


matrix = np.zeros((len(data[0])-1, len(data)))
print(matrix)

aantRij = len(data)
aantKol = len(data[0])-1
for i in range(0,aantRij):
    print(data[i])
    for j in range(0,aantKol):
        matrix[i][j] = int(data[i][j])
print(matrix)

aantFlashes = 0
for stap in range(0,500):
    print("stap",stap+1)
    # the energy level of each octopus increases by 1
    for i in range(0,aantRij):
        for j in range(0,aantKol):
            matrix[i][j] += 1
           
    aantFlashes += flash(matrix,aantRij,aantKol)
    print(matrix)
    if (checkSyn(matrix)):
        print("stap syn =",stap+1)
        break
print(aantFlashes)

