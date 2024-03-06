import numpy as np


l = [0,1,2,3,4,5,6,7,8,9]
proxi = [ci-cj for ci in l for cj in l]
d = np.array(proxi)
n = d.reshape(10,10)
print(n)