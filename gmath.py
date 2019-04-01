import math
from display import *

def normalize(vector):
    magnitude = math.sqrt(
        (vector[0] ** 2) + (vector[1] ** 2) + (vector[2] ** 2))
    return [vector[0] / magnitude, vector[1] / magnitude, vector[2] / magnitude]

def dot_product(a, b):
    return (a[0] * b[0]) + (a[1] * b[1]) + (a[2] * b[2])

def cross_product(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]

def calculate_normal(polygons, i):
    vector1 = [polygons[i + 1][0] - polygons[i][0], polygons[i + 1]
            [1] - polygons[i][1], polygons[i + 1][2] - polygons[i][2]]
    vector2 = [polygons[i + 2][0] - polygons[i][0], polygons[i + 2]
            [1] - polygons[i][1], polygons[i + 2][2] - polygons[i][2]]
    return cross_product(vector1, vector2)