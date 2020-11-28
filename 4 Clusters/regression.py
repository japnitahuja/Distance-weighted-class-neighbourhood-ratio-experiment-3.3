from sklearn.linear_model import LinearRegression

betaAll = []
scores = []
betaBins = []


file = open('betaValues.txt','r')
for i in file:
    i = i.strip("\n")
    i = i.split(",")
    temp = []
    
    if len(i) == 0:
        break
    
    for j in i[:-1]:
        temp.append(float(j))
    betaAll.append(temp)
file.close()

file = open('silhouetteScores.txt','r')
for i in file:
    i = i.strip("\n")
    i = float(i)
    if len(str(i)) > 0:
        scores.append(i)
file.close()

for i in betaAll:
    temp = [0 for x in range(10)]
    for j in i:
        #print(int(j*10))
        temp[int(j*10)] += 1
    betaBins.append(temp)


print("Sillhoutte Score(min): " + str(min(scores)))
print("Sillhoutte Score(max): " + str(max(scores)))


reg = LinearRegression().fit(betaBins,scores)
print(reg.score(betaBins, scores))


        




    
