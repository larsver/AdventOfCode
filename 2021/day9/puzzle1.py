import numpy as np

with open("input.txt") as f:
  data = f.readlines()




matrix = np.zeros((len(data[0]), len(data)))
print(matrix)

aantRij = len(data)
aantKol = len(data[0])-1
for i in range(0,aantRij):
    print(data[i])
    for j in range(0,aantKol):
        matrix[i][j] = int(data[i][j])

print(matrix)

risk_points = []
def check(list, val):
    for x in list:
        if val>= x:
            return False 
    return True


for i in range(0,aantRij):
    for j in range(0,aantKol):
        buren = []
        if (i==0):
            if (j==0):
                buren.append(matrix[i+1][j])
                buren.append(matrix[i][j+1])
            elif (j==aantKol-1):
                buren.append(matrix[i+1][j])
                buren.append(matrix[i][j-1])
            else:
                buren.append(matrix[i+1][j])
                buren.append(matrix[i][j-1])
                buren.append(matrix[i][j+1])    
            #print(buren)
        elif (i==aantRij-1):
            if (j==0):
                buren.append(matrix[i-1][j])
                buren.append(matrix[i][j+1])
            elif (j==aantKol-1):
                buren.append(matrix[i-1][j])
                buren.append(matrix[i][j-1])
            else:
                buren.append(matrix[i-1][j])
                buren.append(matrix[i][j-1])
                buren.append(matrix[i][j+1])
            print(buren)
        else :
            if (j==0):
                buren.append(matrix[i-1][j])
                buren.append(matrix[i+1][j])
                buren.append(matrix[i][j+1])
            elif (j==aantKol-1):
                buren.append(matrix[i-1][j])
                buren.append(matrix[i+1][j])
                buren.append(matrix[i][j-1])
            else:
                buren.append(matrix[i-1][j])
                buren.append(matrix[i+1][j])
                buren.append(matrix[i][j-1])
                buren.append(matrix[i][j+1])
        #print(buren)
        #if ( all(int(i) > matrix[i][j] for i in buren)):
        if (check(buren,matrix[i][j])):
            risk_points.append(matrix[i][j])

print(risk_points)

result = 0
for r in risk_points:
    result += (r+1)
    
print(result)