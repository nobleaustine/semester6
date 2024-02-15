import math

data = [(3,7),(4,6),(5,5)] 

def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

m = [euclidean_distance(p1,p2) ]

