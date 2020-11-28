"""
separation value from 240 to -50 (30 stages)
stepsize = 10
20 datasets for each stage
Total: 600 datasets
999 instances in the dataset
"""

import random
import sklearn.metrics
import matplotlib.pyplot as plt
import numpy as np
from beta_value_generation import betaValue as beta
from math import sin
from math import cos

#initialisation
radius = 25
centroidDistance = 290
stepsize = 10

#imbalance
points = [333,333,333]

noDatasets = 20 #no of datasets in each stage
datasetNumber = 0

file = open('betaValues.txt','w')
file.close()

file = open('silhouetteScores.txt','w')
file.close()

while centroidDistance >= 0:
    for z in range(noDatasets):
        print(datasetNumber)

        

        #assuming centroid at 0,0
        centres = [[0,-centroidDistance],\
                   [centroidDistance * sin(1.0472),centroidDistance * cos(1.0472)],\
                   [-centroidDistance * sin(1.0472),centroidDistance * cos(1.0472)]]
        
        features = []
        labels = []

        for centreIndex in range(len(centres)):
            if centreIndex > 0:
                label = 1
            else:
                label = 0
                
            centre = centres[centreIndex]
            instanceCount = 0
            while instanceCount != points[centreIndex]:
                x = random.randint(int(centre[0] - radius) \
                                   ,int(centre[0] + radius))
                
                y = random.randint(int(centre[1] - radius) \
                                   ,int(centre[1] + radius))

                if ((x-centre[0])**2 + (y-centre[1])**2)**0.5 <= radius:
                    instanceCount += 1
                    features.append([x,y])
                    labels.append(label)

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
        
    centroidDistance -= stepsize
    

        
            
        







