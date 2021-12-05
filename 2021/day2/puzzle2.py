with open("input.txt") as f:
  data = f.readlines()
  
horizontaal = 0
diepte = 0
aim = 0 

for i in range(0,len(data)):

    help = data[i].split(" ")
    if (help[0] == "forward"):
        horizontaal = horizontaal + int(help[1].strip())
        diepte = diepte +  int(help[1].strip())*aim
    elif (help[0] == "down"):
        aim = aim + int(help[1].strip())
    elif (help[0] == "up"):
        aim = aim - int(help[1].strip())

print(horizontaal*diepte)
f.close()