from sklearn.linear_model import LinearRegression

scores = []

file = open('silhouetteScores.txt','r')
for i in file:
    i = i.strip("\n")
    i = float(i)
    if len(str(i)) > 0:
        scores.append(i)
file.close()



complexity_file = "complexity"
m = 600 #datasets


measures = {"overlapping.F1":[0 for i in range(m)],
            "overlapping.F1v":[0 for i in range(m)],
            "overlapping.F2":[0 for i in range(m)],
            "overlapping.F3": [0 for i in range(m)],
            "overlapping.F4":[0 for i in range(m)],
            "neighborhood.N1":[0 for i in range(m)],
            "neighborhood.N2":[0 for i in range(m)],
            "neighborhood.N3":[0 for i in range(m)],
            "neighborhood.N4":[0 for i in range(m)],
            "neighborhood.T1":[0 for i in range(m)],
            "neighborhood.LSC":[0 for i in range(m)],
            "linearity.class.L1":[0 for i in range(m)],
            "linearity.class.L2":[0 for i in range(m)],
            "linearity.class.L3":[0 for i in range(m)],
            "dimensionality.T2":[0 for i in range(m)],
            "dimensionality.T3":[0 for i in range(m)],
            "dimensionality.T4":[0 for i in range(m)],
            "balance.C1":[0 for i in range(m)],
            "balance.C2":[0 for i in range(m)],
            "network.Density":[0 for i in range(m)],
            "network.ClsCoef":[0 for i in range(m)],
            "network.Hubs":[0 for i in range(m)]}




file = open(complexity_file + ".txt").read().split("\n")
count = 0

for i in file:
    if i == "":
        continue
    if i =='"x"':
        continue
    if count == 23:
        count = 0
    i = i.split(",")
    if count == 0:
        temp = i[1].split("\"")
        index = int(temp[1].strip(".txt"))
        count+=1
    else:
        temp = i[0].split("\"")
        if i[1] == "NA":
            value = "None"
        else:
            value = [float(i[1])]
        measure = measures[temp[1]]
        measure[index] = value
        count += 1

temp = []
temp_measure = []
file = open('complexityRegModels.txt','w')
y = scores
for i in measures.keys():
    x = measures[i] 
    try:
        reg = LinearRegression().fit(x, y)
        regScore = reg.score(x,y)
        file.write(str(i) + ": " + str(regScore)+"\n")
        temp.append(regScore)
        temp_measure.append(i)
    except:
        file.write(str(i) + ": " + "None"+"\n")
        temp.append("None")
        temp_measure.append(i)
file.close()

print(max(temp))
print(temp_measure[temp.index(max(temp))])
