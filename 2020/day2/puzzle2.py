with open("input.txt") as f:
  data = f.readlines()

total = len(data)
valid = 0

for i in range(0,len(data)):
    help = data[i].split(":")
    passw = help[1].strip()
    help2 = help[0].split(" ")
    letter = help2[1]
    help3 = help2[0].split("-")
    amin = int(help3[0])
    amax = int(help3[1])
    print(passw)
    print(letter)
    print(amin)
    print(amax)
    
    if (passw[amin-1]==letter):
        if (passw[amax-1]!=letter):
            valid += 1
        else:
            valid = valid
    else:
        if (passw[amax-1]==letter):
            valid +=1
        else:
            valid = valid

print(valid)
f.close()