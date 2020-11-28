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
centreDistance = 290
stepsize = 10
innerRadiusOne = radius
innerRadiusTwo = radius + radius


#imbalance
points = [500, 500]

noDatasets = 20 #no of datasets in each stage
datasetNumber = 0

file = open('betaValues.txt','w')
file.close()

file = open('silhouetteScores.txt','w')
file.close()

while centreDistance >= 0:
    for z in range(noDatasets):
        print(datasetNumber)

        #assuming centroid at 0,0
        outerRadiusOne = innerRadiusOne + centreDistance
        outerRadiusTwo = outerRadiusOne + radius
        radii = [[innerRadiusOne, innerRadiusTwo], \
                 [outerRadiusOne,outerRadiusTwo]]
                   
            
        features = []
        labels = []

        for index in range(len(radii)):
            if index%2 == 0:
                label = 1
            else:
                label = 0
                
            instanceCount = 0
            while instanceCount != points[index]:
                x = random.randint(int(-radii[index][1]) \
                                   ,int(radii[index][1]))
                
                y = random.randint(int(-radii[index][1]) \
                                   ,int(radii[index][1]))


                if (x**2 + y**2)**0.5 >= radii[index][0] and\
                   (x**2 + y**2)**0.5 <= radii[index][1]:
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
          
    centreDistance -= stepsize
    

        
            
        







