# 최근접사이의 알고리즘
import math

def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dist = math.sqrt(dx**2 + dy**2)
    return dist

def closest_pair(p):
    n = len(p)
    mindist = float('inf')

    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(p[i], p[j])
            if dist < mindist:
                mindist = dist

    return mindist

p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(f"최근접 거리: {closest_pair(p)}")
