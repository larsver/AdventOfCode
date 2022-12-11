def checkIt(string):
    for a in range(len(string)):
            for b in range(a + 1,len(string)):
                if(string[a] == string[b]):
                    return False
    return True

file = open("input.txt")

oplossing = 0
lines = file.readlines()
print(lines)


print(lines[0][0:5])

checkstring = ""
helpstring = ""

lijn = lines[0]

for i in range(0,len(lijn)):
    if len(checkstring)==4:
        helpstring = checkstring+lijn[i]
        checkstring = helpstring[1:5]
    else :
        checkstring = checkstring+lijn[i]
    
    print("char",lijn[i])
    print(checkstring)

    if len(checkstring)==4:
        if checkIt(checkstring):
            oplossing = i+1
            break

print(oplossing)

file.close()