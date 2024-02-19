import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

# creating points with in the range
data = np.arange(-100,100,1)

# creating concurret curves
D1 = [[x,y] for x in data for y in data if ((x-10)**2 + (y-10)**2)**0.5 < 5]
D2 = [[x,y] for x in data for y in data if ((x-10)**2 + (y-10)**2)**0.5 < 12 and ((x-10)**2 + (y-10)**2)**0.5 > 8]
D3 = [[x,y] for x in data for y in data if ((x-10)**2 + (y-10)**2)**0.5 < 18 and ((x-10)**2 + (y-10)**2)**0.5 > 15]
X = D1 + D2 + D3
X = np.array(X)

# clustering DB scan
dbscan = DBSCAN(eps=3, min_samples=2)

# fit the model and predict clusters
clusters = dbscan.fit_predict(X)

# Plot the clusters
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('DBSCAN Clustering')
plt.show()
