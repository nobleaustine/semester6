from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt

iris = load_iris()

X = iris.data
Y = iris.target


def distance(p1,p2):
     square_diff = [(x-y)**2 for x,y in zip(p1,p2)]
     s = sum(square_diff)
     return s**0.5

def cluster(cen,X):

    l0 = []
    l1 = []
    l2 = []
     
    for x in X:
         
         x = x.tolist()
         dis = [distance(x,c) for c in cen]
         label = dis.index(min(dis))
        
         if label == 0:
              l0.append(x)
         elif label == 1:
              l1.append(x)
         else:
              l2.append(x)

    return l0,l1,l2

cen = [X[0],X[50],X[100]]
l0,l1,l2 = cluster(cen,X)
cen[0] = [sum(x)/len(l0) for x in zip(*l0)]
cen[1] = [sum(y)/len(l1) for y in zip(*l1)]
cen[2] = [sum(z)/len(l2) for z in zip(*l2)]

l0,l1,l2 = cluster(cen,X)

pca = PCA(n_components=2)
data = pca.fit_transform(X)

