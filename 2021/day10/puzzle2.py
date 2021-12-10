import numpy

with open("input.txt") as f:
  data = f.readlines()

results = []
for i in range(0,len(data)):
    #print(data[i])
    line = data[i].strip()
    open = ["(","[","{","<"]
    openlijst = [] ;
    fout = 0
    for j in range(0,len(line)):
        #print(data[i][j])
        h = data[i][j]
        if (h in open):
            #print ("open")
            openlijst.append(h)
        else:
            #print("close")
            if (h == ")" and openlijst[-1]!="("):
                print("nok")
                fout = 1
                break; 
            elif (h == "]" and openlijst[-1]!="["):
                print("nok")
                fout = 1
                break;
            elif (h == "}" and openlijst[-1]!="{"):
                print("nok")
                fout = 1
                break;
            elif (h == ">" and openlijst[-1]!="<"):
                print("nok")
                fout = 1
                break;
            else:
                openlijst.pop()
    if (fout == 0):
        points = 0
        print(openlijst)
        for a in reversed(openlijst):
            points *=5
            if (a == "("):
                points +=1
            if (a == "["):
                points +=2
            if (a == "{"):
                points +=3
            if (a == "<"):
                points +=4
        print(points)
        results.append(points)

median = numpy.median(results)
print(median)

