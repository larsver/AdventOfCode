with open("input.txt") as f:
  data = f.readlines()
  
gamma = [] 
epsilong = []

count = []

for i in range(0,len(data)):
    #print(data[i])
    
    if not count:
        length = len(data[i])
        count = [0] * (length-1)
        epsilong = [0] * (length-1)
        gamma = [0] * (length-1)
    
    for j in range (0,len(data[i])):
        if (data[i][j] == "1"):
            count[j] += 1
    print(count)

for a in range(0,length-1):
    if (count[a] > len(data)/2):
        gamma[a] = 1
        epsilong[a] = 0
    else   : 
        gamma[a] = 0
        epsilong[a] = 1
        
strGamma = ''.join(map(str,gamma))
strEpsilong = ''.join(map(str,epsilong))


print(gamma)
print(epsilong)
print(strGamma)
print(strEpsilong)


print(int(strGamma, 2)) #to decimaal
print(int(strEpsilong, 2)) #todecimaal
solution = int(strGamma, 2) * int(strEpsilong, 2)
print(solution)

f.close()