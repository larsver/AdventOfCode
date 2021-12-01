
with open("input.txt") as f:
  data = f.readlines()
  
#f = open("input.txt")
teller = 0
vorige = 0 
huidige = 0 

for i in range(0,len(data)-2):
    
    huidige = int(data[i]) + int(data[i+1]) + int(data[i+2])  
    
    if ((huidige > vorige) and (vorige!=0)):
        teller = teller + 1 
  
    vorige = huidige
  
print "teller =",teller
f.close()

