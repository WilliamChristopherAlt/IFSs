import numpy as np
import random
import goodies

sierspinkyTriangle = {
    'IFS_matrix':[
        [0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1/3],
        [0.5, 0.0, 0.0, 0.5, 0.5, 0.0, 1/3],
        [0.5, 0.0, 0.0, 0.5, 0.25, np.sqrt(3)/4, 1/3]
    ],
    'range': [1, 0, 1, -0.1]                    
}

sierspinkyCarpet = {
    'IFS_matrix':[
        [1/3, 0, 0, 1/3, 0, 0, 1/8],
        [1/3, 0, 0, 1/3, 0, 1/3, 1/8],
        [1/3, 0, 0, 1/3, 0, 2/3, 1/8],
        [1/3, 0, 0, 1/3, 1/3, 0, 1/8],
        [1/3, 0, 0, 1/3, 1/3, 2/3, 1/8],
        [1/3, 0, 0, 1/3, 2/3, 0, 1/8],
        [1/3, 0, 0, 1/3, 2/3, 1/3, 1/8],
        [1/3, 0, 0, 1/3, 2/3, 2/3, 1/8]
    ],
    'range': [1, 0, 1, 0]
}

sqrt3 = np.sqrt(3)
kockSnowflake = {
    'IFS_matrix': [
        [0.5, -(sqrt3/6), (sqrt3/6), 0.5, 0, 0, 1/2],
        [1/3, 0, 0, 1/3, (sqrt3/3), 1/3, 1/12],
        [1/3, 0, 0, 1/3, 0, 2/3, 1/12],
        [1/3, 0, 0, 1/3, -(sqrt3/3), 1/3, 1/12],
        [1/3, 0, 0, 1/3, -(sqrt3/3), -1/3, 1/12],
        [1/3, 0, 0, 1/3, 0, -2/3, 1/12],
        [1/3, 0, 0, 1/3, (sqrt3/3), -1/3, 1/12],
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

mapleLeaf = {
    'IFS_matrix':[
        [0.14, 0.01, 0.0, 0.51, -0.08, -1.31, 0.1],
        [0.43, 0.52, -0.45, 0.50, 1.49, -0.75, 0.35],
        [0.45, -0.49, 0.47, 0.47, -1.62, -0.74, 0.35],
        [0.49, 0.00, 0.00, 0.51, 0.02, 1.62, 0.2]
    ],
    'range': [4, -4, 4, -4]
}

barnsley = {
    'IFS_matrix': [
        [0.00, 0.00, 0.00, 0.16, 0.00, 0.00, 0.01],
        [0.85, 0.04, -0.04, 0.85, 0.0, 1.60, 0.85],
        [0.20, -0.26, 0.23, 0.22, 0.0, 1.60, 0.07],
        [-0.15, 0.28, 0.26, 0.24, 0.0, 0.44, 0.07]
    ],
    'range': [3, -3, 11, 0]
}

vicsek = {
    'IFS_matrix': [
        [0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1/3],
        [0.5, 0.0, 0.0, 0.5, 1.0, 0.0, 1/6],
        [0.5, 0.0, 0.0, 0.5, 0.0, 1.0, 1/6],
        [0.5, 0.0, 0.0, 0.5, -1.0, 0.0, 1/6],
        [0.5, 0.0, 0.0, 0.5, 0.0, -1.0, 1/6]
    ],
    'range': [2, -2, 2, -2]
}


ink = {
    'IFS_matrix':[
        [0.5, 0.0, 0.0, 0.5, 0.0, 0.0, 1/3],
        [0.25, -0.25, 0.25, 0.25, 0.5, 0.5, 1/6],
        [0.25, -0.25, 0.25, 0.25, -0.5, -0.5, 1/6],
        [0.25, 0.25, -0.25, 0.25, 0.5, -0.5, 1/6],
        [0.25, 0.25, -0.25, 0.25, -0.5, 0.5, 1/6]
    ],
    'range': [1, -1, 1, -1]                    
}
    
inkblotTheSecond = {
    'IFS_matrix': [
        [0.5, 0, 0, 0.5, 0.0, 0.0, 1/3],
        [0.0, -2/3, 2/3, 0.0, -0.5, 0.5, 1/3],
        [0.0, -2/3, 2/3, 0.0, 0.5, -0.5, 1/3]
],
    'range': [2, -2, 2, -2]                    
}

inkblotTheFirst = {
    'IFS_matrix': [
        [0.5, 0, 0, 0.5, 0.0, 0.0, 1/3],
        [0.0, -3/4, 3/4, 0.0, -0.5, -0.5, 1/3],
        [0.0, -3/4, 3/4, 0.0, 0.5, 0.5, 1/3]
    ],
    'range': [2, -2, 2, -2]                    
}

class IFS:
    def __init__(self, ifs_matrix):
        self.cumulative_probs = np.cumsum([row[-1] for row in ifs_matrix])

        self.funcs = [
            lambda x, y, a=a, b=b, c=c, d=d, e=e, f=f: (a*x + b*y + e, c*x + d*y + f)
            for row in ifs_matrix
            for a, b, c, d, e, f in [row[:6]]
        ]

    def __call__(self, x, y):
        return self.funcs[np.searchsorted(self.cumulative_probs, random.random())](x, y)

def searchAllPoints(no_of_points, ifs_matrix):
    ifs = IFS(ifs_matrix)

    xs = np.empty(no_of_points)
    ys = np.empty(no_of_points)
    xs[0] = 0.0
    ys[0] = 0.0

    for i in range(1, no_of_points):
        xs[i], ys[i] = ifs(xs[i-1], ys[i-1])

    return xs[10:], ys[10:]

def main():
    iterations = 10000
    density = 100

    fractal = inkblotTheSecond
    displayMode = 'binary'

    xs, ys = searchAllPoints(iterations, fractal['IFS_matrix'])

    data = goodies.coorsToDataMatrix(xs, ys, density, fractal['range'], pixelCounting=(displayMode != 'binary'))
    goodies.draw(data, colorMode=displayMode)

    # goodies.save_image(data, r"C:\Users\PC\Desktop\Programming\Python\Fractals\pictures\test1.png", colorMode=displayMode)
    

main()    