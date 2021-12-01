
f = open("input.txt")
vorige = 0 ;
huidige = 0 ;
teller = 0 ;
for diepte in f:
  huidige = int(diepte) ;
      
  if ((huidige > vorige) and (vorige!=0)):
    teller = teller + 1 
  
  vorige = huidige
print "teller =",teller

f.close()