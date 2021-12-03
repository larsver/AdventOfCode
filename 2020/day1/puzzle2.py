with open("input.txt") as f:
  data = f.readlines()
  

getal1 = 0
getal2 = 0
getal3 = 0

for i in data:
    for j in data:
		for z in data:
			if ((int(i)+int(j)+int(z)) == 2020):
				getal1 = i
				getal2 = j
				getal3 = z
print(getal1)
print(getal2)
print(getal3)
print(int(getal1)*int(getal2)*int(getal3))
f.close()