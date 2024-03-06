import numpy as np
import pandas as pd

# class to create a cluster with name and number of elements
# where we can add new elements
class cluster:

    def __init__(self, name, e) -> None:

        self.name = name
        if len([e]) == 1 :
            self.elements = [e]
        else:
            self.elements = e

    def extend(self, c):
        self.name = self.name + c.name
        self.elements.extend(c.elements)

    def __add__(self,c2):
        if isinstance(c2,cluster):
            name = self.name + c2.name
            elements = self.elements + c2.elements

            return cluster(name,elements)

def dist(ci, cj, type="avg"):

    distances = [ round(((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5, 2)
            for x in ci.elements
            for y in cj.elements]
   
    matrix = np.array(distances)
    if type == "single":
        distance = np.min(matrix)
    elif type == "complete":
        distance = np.max(matrix)
    else:
        distance = np.mean(matrix)

    return distance

names = ["A", "B", "C", "D", "E", "F", "G"]
data = np.array([[10, 5], [1, 4], [5, 8], [9, 2], [12, 10], [15, 8], [7, 7]])

clusters = [cluster(name, dp) for name,dp in zip(names,data)]

while len(clusters) > 1:

    proxi = [dist(ci,cj) if i >j else 999
            for i,ci in enumerate(clusters) 
            for j,cj in enumerate(clusters)]
    # for i, ci in enumerate(clusters):
    #     row = []
    #     for j, cj in enumerate(clusters):
    #         if i > j:
    #             row.append(dist(ci, cj))
    #         else:
    #             row.append(float(999))
    #     proxi.append(row)
    proxi = np.array(proxi).reshape(len(clusters),len(clusters))
    minvalue = np.min(proxi)

    df = pd.DataFrame(proxi, index=names, columns=names)
    print(df)
    indices = np.where(proxi == minvalue)

    if len(indices) == 2:
        rows = indices[0][0]
        cols = indices[1][0]

    cmin1 = clusters.pop(rows)
    cmin2 = clusters.pop(cols)
    cmin1.extend(cmin2)
    clusters.append(cmin1)
    names = []

    for c in clusters:
        names.append(c.name)

print(df)
