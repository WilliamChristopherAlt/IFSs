import numpy as np
import random
from matplotlib import pyplot as plt
from PIL import Image
import goodies

fern = {
    'IFS_matrix':[
        [0, 0, 0, 0.172, 0.496, -0.091],
        [0.076, 0.312, -0.257, 0.204, 0.494, 0.133],
        [0.821, -0.028, 0.03, 0.845, 0.088, 0.176],
        [-0.024, -0.356, -0.323, 0.074, 0.47, 0.26]
    ],
    'range': [1, 0, 1, -0.2]
}

vkoch = {
    'IFS_matrix': [
        [0.3333, 0, 0, 0.3333, 0, 0],
        [0.3333, 0, 0, 0.3333, 0.6666, 0],
        [0.1666, -0.2886, 0.2886, 0.1666, 0.3333, 0],
        [-0.1666, 0.2886, 0.28867, 0.1666, 0.6666, 0]
    ],
    'range': [1, 0, 0.5, -0.1]
}

sierspinkyTriangle = {
    'IFS_matrix':[
        [0.5, 0.0, 0.0, 0.5, 0.0, 0.0],
        [0.5, 0.0, 0.0, 0.5, 0.5, 0.0],
        [0.5, 0.0, 0.0, 0.5, 0.25, np.sqrt(3)/4]
    ],
    'range': [1, -1, 1, -1]                    
}

sierspinkyCarpet = {
    'IFS_matirx':[
        [1/3, 0, 0, 1/3, 0, 0],
        [1/3, 0, 0, 1/3, 0, 1/3],
        [1/3, 0, 0, 1/3, 0, 2/3],
        [1/3, 0, 0, 1/3, 1/3, 0],
        [1/3, 0, 0, 1/3, 1/3, 2/3],
        [1/3, 0, 0, 1/3, 2/3, 0],
        [1/3, 0, 0, 1/3, 2/3, 1/3],
        [1/3, 0, 0, 1/3, 2/3, 2/3]
    ],
    'range': [1, -1, 1, -1]
}

PI = np.pi
cos = np.cos; sin = np.sin
cos1 = cos(2*PI/5); sin1 = sin(2*PI/5)
cos2 = cos(PI/5); sin2 = sin(PI/5)
r = 1 / (2*cos(2*PI/5) + 2)
pentagonFractal = {
    'IFS_matrix':[
        [r, 0.0, 0.0, r, 0.5, 0.0],
        [r, 0.0, 0.0, r, cos1/2, sin1/2],
        [r, 0.0, 0.0, r, -cos2/2, sin2/2],
        [r, 0.0, 0.0, r, -cos2/2, -sin2/2],
        [r, 0.0, 0.0, r, cos1/2, -sin1/2],
    ],
    'range': [1, -1, 1, -1]                    
}

pentagonFractal1 = {
    'IFS_matrix':[
        [r, 0.0, 0.0, r, 0.5, 0.0],
        [r, 0.0, 0.0, r, cos1/2, sin1/2],
        [r, 0.0, 0.0, r, -cos2/2, sin2/2],
        [r, 0.0, 0.0, r, -cos2/2, -sin2/2],
        [r, 0.0, 0.0, r, cos1/2, -sin1/2],
    ],
    'range': [1, -1, 1, -1]                    
}

sqrt3 = np.sqrt(3)
kockSnowflake = {
    'IFS_matrix': [
        # [0.5, -(sqrt3/6), (sqrt3/6), 0.5, 0, 0],
        [1/3, 0, 0, 1/3, (sqrt3/3), 1/3],
        [1/3, 0, 0, 1/3, 0, 2/3],
        [1/3, 0, 0, 1/3, -(sqrt3/3), 1/3],
        [1/3, 0, 0, 1/3, -(sqrt3/3), -1/3],
        [1/3, 0, 0, 1/3, 0, -2/3],
        [1/3, 0, 0, 1/3, (sqrt3/3), -1/3],
    ],
    'range': [1, -1, 1, -1]
}


tree2= {
    'IFS_matrix': [
        [0.195, -0.488, 0.344, 0.443, 0.4431, 0.2452],
        [0.462, 0.414, -0.252, 0.361, 0.2511, 0.5692],
        [-0.058, -0.07, 0.453, -0.111, 0.5976, 0.097],
        [-0.035, 0.7, -0.469, -0.022, 0.4884, 0.507],
        [-0.637, 0, 0, 0.501, 0.8562, 0.2513]
    ],
    'range': [4, -4, 4, -4]
}
shield= {
    'IFS_matrix': [
        [0.382, 0, 0, 0.382, 0.3072, 0.619],
        [0.382, 0, 0, 0.382, 0.6033, 0.4044],
        [0.382, 0, 0, 0.382, 0.0139, 0.4044],
        [0.382, 0, 0, 0.382, 0.1253, 0.595],
        [0.382, 0, 0, 0.382, 0.492, 0.0595]
    ],
    'range': [4, -4, 4, -4]
}
wind= {
    'IFS_matrix': [
        [0.3333, 0, 0, 0.3333, 0, 0],
        [0.1666, -0.2886, 0.2886, 0.1666, 3.3333, 0],
        [0.1666, 0.2886, -0.2886, 0.1666, 5, 2.8867],
        [0.3333, 0, 0, 0.3333, 0.6666, 0]
    ],
    'range': [7, 0, 3, -1]
}
fir= {
    'IFS_matrix': [
        [0.65, -0.013, 0.013, 0.65, 0.175, 0],
        [0.65, -0.026, 0.026, 0.65, 0.165, 0.325],
        [0.318, -0.318, 0.318, 0.318, 0.2, 0],
        [-0.1666, 0.2886, 0.2886, 0.1666, 0.6666, 0]
    ],
    'range': [1, 0, 1, -0.2]
}
tree1= {
    'IFS_matrix': [
        [0, 0, 0, 0.5, 0, 0],
        [0.42, -0.42, 0.42, 0.42, 0, 0.2],
        [0.42, 0.42, -0.42, 0.42, 0, 0.2],
        [0.1, 0, 0, 0.1, 0, 0.2]
    ],
    'range': [1, 0, 1, -0.2]
}
vkoch= {
    'IFS_matrix': [
        [0.3333, 0, 0, 0.3333, 0, 0],
        [0.3333, 0, 0, 0.3333, 0.6666, 0],
        [0.1666, -0.2886, 0.2886, 0.1666, 0.3333, 0],
        [-0.1666, 0.2886, 0.28867, 0.1666, 0.6666, 0]
    ],
    'range': [1, 0, 1, -0.2]
}
mayan= {
    'IFS_matrix': [
        [0.5, 0, 0, 0.5, -2.5634, -0.000003],
        [0.5, 0, 0, 0.5, 2.4365, -0.000003],
        [0, -0.5, 0.5, 0, 4.8730, 7.5635]
    ],
    'range': [1, 0, 1, -0.2]
}
carpet1= {
    'IFS_matrix': [
        [0.333, 0, 0, 0.333, 0.333, 0.666],
        [0, 0.333, 1, 0, 0.666, 0],
        [0, -0.333, 1, 0, 0.333, 0]
    ],
    'range': [1, 0, 1, -0.2]
}
carpet2= {
    'IFS_matrix': [
        [0, -0.5, 0.5, 0, -1.7323, 3.3661],
        [0.5, 0, 0, 0.5, -0.0278, 5.0148],
        [0, 0.5, -0.5, 0, 1.6208, 3.3104]
    ],
    'range': [1, 0, 1, -0.2]
}
triangle= {
    'IFS_matrix': [
        [0.5, 0, 0, 0.5, 0, 0],
        [0.5, 0, 0, 0.5, 0, 0],
        [0.5, 0, 0, 0.5, 1, 1]
    ],
    'range': [1, 0, 1, -0.2]
}
xmas= {
    'IFS_matrix': [
        [0, -0.5, 0.5, 0, 0.5, 0],
        [0, 0.5, -0.5, 0, 0.5, 0.5],
        [0.5, 0, 0, 0.5, 0.25, 0.5]
    ],
    'range': [1, 0, 1, -0.2]
}
storm= {
    'IFS_matrix': [
        [0, 0.577, -0.577, 0, 0.0951, 0.5893],
        [0, 0.577, -0.577, 0, 0.4413, 0.7893],
        [0, 0.577, -0.577, 0, 0.0952, 0.9893]
    ],
    'range': [1, 0, 1, -0.2]
}
twig= {
    'IFS_matrix': [
        [0.387, 0.43, 0.43, -0.387, 0.256, 0.522],
        [0.441, -0.091, -0.009, -0.322, 0.4219, 0.5059],
        [-0.468, 0.2, -0.113, 0.15, 0.4, 0.4]
    ],
    'range': [4, -4, 4, -4]
}
coral= {
    'IFS_matrix': [
        [0.3076, -0.5314, -0.4615, -0.2937, 5.402, 8.6551],
        [0.3076, -0.077, 0.1538, -0.4475, -1.2952, 4.153],
        [0, 0.5454, 0.6923, -0.1958, -4.8936, 7.2697]
    ],
    'range': [4, -4, 4, -4]
}
spiral= {
    'IFS_matrix': [
        [0.7878, -0.4242, 0.2424, 0.8598, 1.7586, 1.408],
        [-0.1212, 0.2575, 0.1515, 0.053, -6.7216, 1.3772],
        [0.1818, -0.1363, 0.091, 0.1818, 6.0861, 1.568]
    ],
    'range': [4, -4, 4, -4]
}
dragon= {
    'IFS_matrix': [
        [0.824, 0.2814, -0.2123, 0.8641, -1.8823, -0.1106],
        [0.0882, 0.521, -0.4638, -0.3777, 0.7853, 8.0957]
    ],
    'range': [4, -4, 4, -4]
}
crystal= {
    'IFS_matrix': [
        [0.6969, -0.481, -0.394, -0.6628, 2.147, 10.3102],
        [0.091, -0.4431, 0.5151, -0.0946, 4.2865, 2.9257]
    ],
    'range': [4, -4, 4, -4]
}
snow= {
    'IFS_matrix': [
        [0.255, 0, 0, 0.255, 0.3726, 0.6714],
        [0.255, 0, 0, 0.255, 0.1146, 0.2232],
        [0.255, 0, 0, 0.255, 0.6306, 0.2232],
        [0.37, -0.642, 0.642, 0.37, 0.6356, -0.0061]
    ],
    'range': [1, 0, 1, 0]
}
zigzag= {
    'IFS_matrix': [
        [-0.6324, -0.6148, -0.5453, 0.6592, 3.8408, 1.2823],
        [-0.0361, 0.4444, 0.2101, 0.037, 2.071, 8.3305]
    ],
    'range': [4, -4, 4, -3]
}
firework= {
    'IFS_matrix': [
        [0.7454, -0.4591, 0.406, 0.8871, 1.4602, 0.691],
        [-0.4242, -0.0651, -0.1757, -0.2181, 3.8095, 6.7414]
    ],
    'range': [8, -8, 10, -1]
}

class IFS:
    def __init__(self, ifs_matrix):
        self.funcs = [
            lambda x, y, a=a, b=b, c=c, d=d, e=e, f=f: (a*x + b*y + e, c*x + d*y + f)
            for row in ifs_matrix
            for a, b, c, d, e, f in [row]
        ]

    def __call__(self, x, y):
        return random.choice(self.funcs)(x, y)

def searchAllPoints(no_of_points, ifs_matrix):
    ifs = IFS(ifs_matrix)

    xs = np.empty(no_of_points)
    ys = np.empty(no_of_points)
    xs[0] = 0.0
    ys[0] = 0.0

    for i in range(1, no_of_points):
        xs[i], ys[i] = ifs(xs[i-1], ys[i-1])

    return xs[20:], ys[20:]

def main():
    iterations = 500000
    density = 1000

    fractal = kockSnowflake
    displayMode = 'binary'

    xs, ys = searchAllPoints(iterations, fractal['IFS_matrix'])

    data = goodies.coorsToDataMatrix(xs, ys, density, fractal['range'], (displayMode!='binary'))
    goodies.draw(data, colorMode=displayMode)

    # goodies.save_image(data, r"C:\Users\PC\Desktop\Programming\Python\Fractals\pictures\snowflakeIFSeven.png")
    

main()    