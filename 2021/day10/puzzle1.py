import numpy as np

with open("input.txt") as f:
  data = f.readlines()



fout1 = 0
fout2 = 0 
fout3 = 0 
fout4 = 0
for i in range(0,len(data)):
    #print(data[i])
    
    open = ["(","[","{","<"]
    openlijst = [] ;
    for j in range(0,len(data[i])):
        #print(data[i][j])
        h = data[i][j]
        if (h in open):
            #print ("open")
            openlijst.append(h)
        else:
            #print("close")
            if (h == ")" and openlijst[-1]!="("):
                print("nok")
                fout1 += 1
                break; 
            elif (h == "]" and openlijst[-1]!="["):
                print("nok")
                fout2 += 1
                break;
            elif (h == "}" and openlijst[-1]!="{"):
                print("nok")
                fout3 += 1
                break;
            elif (h == ">" and openlijst[-1]!="<"):
                print("nok")
                fout4 += 1
                break;
            else:
                openlijst.pop()
                
print(fout1)
print(fout2)
print(fout3)
print(fout4)
result = fout1*3 + fout2*57 +fout3*1197+fout4*25137
print(result)