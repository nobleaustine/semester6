import numpy as np
import pandas as pd


class cluster:

    def __init__(self, name, l) -> None:
        self.name = name
        self.elements = [l]

    def add(self, e):
        self.l.append(e)

    def extend(self, c):
        self.name = self.name + c.name
        self.elements.extend(c.elements)


def dist(ci, cj, type="avg"):
    distances = []
    for x in ci.elements:
        row = []
        for y in cj.elements:
            row.append(round(((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5, 2))
        distances.append(row)

    matrix = np.array(distances)
    if type == "single":
        distance = np.min(matrix)
    elif type == "complete":
        distance = np.max(matrix)
    else:
        distance = np.mean(matrix)

    return distance


clusters = []
names = ["A", "B", "C", "D", "E", "F", "G"]
data = np.array([[10, 5], [1, 4], [5, 8], [9, 2], [12, 10], [15, 8], [7, 7]])

for i in range(7):
    c = cluster(names[i], data[i])
    clusters.append(c)


while len(clusters) > 1:

    proxi = []
    for i, ci in enumerate(clusters):
        row = []
        for j, cj in enumerate(clusters):
            if i > j:
                row.append(dist(ci, cj))
            else:
                row.append(float(999))
        proxi.append(row)
    proxi = np.array(proxi)
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
