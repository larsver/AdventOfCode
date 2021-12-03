with open("input.txt") as f:
  data = f.readlines()
  

getal1 = 0
getal2 = 0

for i in data:
    for j in data:
        if ((int(i)+int(j)) == 2020):
            getal1 = i
            getal2 = j
            print(getal1)
            print(getal2)
   
print(getal1)
print(getal2)
print(int(getal1)*int(getal2))
f.close()