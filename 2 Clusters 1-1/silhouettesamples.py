from beta_value_generation import betaValue as beta
home = os.getcwd()
datasetFolder = os.path.join(home,"datasets")

for i in range(600):
    fileName = os.path.join(datasetFolder, str(i)+ ".txt")
    file = open(fileName, 'r')
    X = []
    y = []

    for i in dataset:
        i = i.strip("\n")
        i = i.split(",")
        temp= []
        for j in range(len(i)):
            if j == 2:
                y.append(int(i[j]))
            else:
                temp.append(int(i[j]))
        X.append(temp)


print(sklearn.metrics.silhouette_samples(X, y))
