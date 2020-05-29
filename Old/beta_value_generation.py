"""
S(yi) = {(Xj,yj) in S where yj = yi} // set of points with label yi
SNN((Xi,yi)) = {(Xj,yj) in S where | (Xj, yj) is among the |S(yi)| - 1 closest instances to (Xi, yi) and yj = yi}
// set of nearest neighbours to (Xi, yi) that have the same label yi; where there are |S(yi)| - 1 nearest neighbours
SNND((Xi,yi)) = Sum over each (Xj, yj) in SNN((Xi,yi)): 1 / (1 + Dist((Xi,yi),(Xj,yj))
ANND((Xi,yi)) = Sum over each (Xj, yj) in S \ {(Xi, yi)}: 1 / (1 + Dist((Xi,yi),(Xj,yj))
Beta((Xi,yi)) = SNND((Xi,yi)) / ANND((Xi,yi))

dont forget to exclude the point itself
"""

def distance(a,b): #euclidean
    squaredDistance = 0
    for i in range(len(a)):
        squaredDistance += (a[i]-b[i])**2
    return squaredDistance ** 0.5
    

def betaValue(features,labels):#features [[X1,X2,...,Xi]] n sized; labels [y] n sized
    betaAll = []
    for i in range(len(features)):
        SNND = 0
        ANND = 0
        for j in range(len(features)):
            if i == j:
                continue
            dist = distance(features[i],features[j])
            if labels[i] == labels[j]:
                SNND += (1/(1+dist))
            ANND += (1/(1+dist))

        betaEach = SNND/ANND
        betaAll.append(betaEach)
    return betaAll
                

