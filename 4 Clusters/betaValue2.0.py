from beta_value_generation import betaValue as beta
import os

home = os.getcwd()
datasetFolder = os.path.join(home,"datasets")
betaFile = open("betaValues2.txt","w")

for i in range(600):
    print(i)
    fileName = os.path.join(datasetFolder, str(i)+ ".txt")
    file = open(fileName, 'r')
    X = []
    y = []
    classDistribution = [0,0]
    for i in file:
        i = i.strip("\n")
        i = i.split(",")
        temp= []
        for j in range(len(i)):
            if j == 2:
                y.append(int(i[j]))
                classDistribution[int(i[j])] += 1
            else:
                temp.append(int(i[j]))
        X.append(temp)
    file.close()

    betaValue = beta(X,y,classDistribution)
    
    for i in betaValue:
        betaFile.write(str(i) + ",")
    betaFile.write("\n")
betaFile.close()
    




