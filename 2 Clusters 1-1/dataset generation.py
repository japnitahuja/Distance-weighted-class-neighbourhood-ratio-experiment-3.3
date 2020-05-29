"""
separation value from 240 to -50 (30 stages)
stepsize = 10
20 datasets for each stage
Total: 600 datasets
1000 instances in the dataset
"""

import random
import sklearn.metrics
import matplotlib.pyplot as plt
import numpy as np
from beta_value_generation import betaValue as beta

#initialisation
radius = 25
separation = 240
stepsize = 10

#imbalance
points1 = 500
points2 = 500

noDatasets = 20 #no of datasets in each stage
datasetNumber = 0

file = open('betaValues.txt','w')
file.close()

file = open('silhouetteScores.txt','w')
file.close()

while separation >= (radius*(-2)):
    for z in range(noDatasets):
        print(datasetNumber)
        
        centroid1 = [radius,radius]
        centroid2 = [radius*3 + separation,radius]
        features = []
        labels = []

        instanceCount = 0
        while instanceCount != points1:
            x = random.randint(0,radius*2)
            y = random.randint(0,radius*2)

            if ((x-centroid1[0])**2 + (y-centroid1[1])**2)**0.5 <= 25:
                instanceCount += 1
                features.append([x,y])
                labels.append(0)

        instanceCount = 0
        while instanceCount != points2:
            x = random.randint(radius*2 + separation,radius*4 + separation)
            y = random.randint(0,radius*2)

            if ((x-centroid2[0])**2 + (y-centroid2[1])**2)**0.5 <= 25:
                instanceCount += 1
                features.append([x,y])
                labels.append(1)


        #Silhouette score
        score = sklearn.metrics.silhouette_score(features, labels)

        #Beta Values
        betaV = beta(features,labels)


        #Plotting

        for i in range(len(features)):
            if labels[i] == 0:
                plt.plot(features[i][0],features[i][1],'bo')
            else:
                plt.plot(features[i][0],features[i][1],'ro')

        #Saving
        name = str(datasetNumber)
        plt.savefig('plots/' + name + '.png')
        plt.clf()

        file = open('datasets/'+ name + '.txt','w')
        for i in range(len(features)):
            file.write(str(features[i][0]) + "," + str(features[i][1]) + "," \
                       + str(labels[i])+"\n")
        file.close()

        file = open('betaValues.txt','a')
        for i in betaV:
            file.write(str(i) + ",")
        file.write("\n")
        file.close()

        file = open('silhouetteScores.txt','a')
        file.write(str(score))
        file.write("\n")
        file.close()

        datasetNumber += 1
        
    separation -= stepsize

        
            
        







