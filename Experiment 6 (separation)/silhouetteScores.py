import sklearn.metrics


file = open('silhouetteScores.txt','w')

for i in range(775):
    features = []
    labels = []
    name = str(i) + ".txt"
    dataset = open('datasets/'+name,'r')
    for j in dataset:
        j = j.strip("\n")
        j = j.split(",")
        if len(j) != 0:
            features.append([float(j[0]),float(j[1])])
            labels.append(float(j[2]))
    dataset.close()
    file.write(str(sklearn.metrics.silhouette_score(features, labels)))
    file.write("\n")
file.close()


