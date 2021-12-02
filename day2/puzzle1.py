with open("input.txt") as f:
  data = f.readlines()
  
horizontaal = 0
diepte = 0

for i in range(0,len(data)):
    #print(data[i])
    #print(data[i].split(" "))
    help = data[i].split(" ")
    if (help[0] == "forward"):
        horizontaal = horizontaal + int(help[1].strip())
        #print(help[1].strip())
    elif (help[0] == "down"):
        diepte = diepte + int(help[1].strip())
    elif (help[0] == "up"):
        diepte = diepte - int(help[1].strip())

print(horizontaal*diepte)
f.close()