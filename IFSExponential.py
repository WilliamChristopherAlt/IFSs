import numpy as np
import goodies

sierspinkyTriangle = {
    'IFS_matrix':[
        [0.5, 0.0, 0.0, 0.5, 0.0, 0.0],
        [0.5, 0.0, 0.0, 0.5, 0.5, 0.0],
        [0.5, 0.0, 0.0, 0.5, 0.25, np.sqrt(3)/4]
    ],
    'range': [1, 0, 1, -0.1]                    
}

sierspinkyCarpet = {
    'IFS_matrix':[
        [1/3, 0, 0, 1/3, 0, 0],
        [1/3, 0, 0, 1/3, 0, 1/3],
        [1/3, 0, 0, 1/3, 0, 2/3],
        [1/3, 0, 0, 1/3, 1/3, 0],
        [1/3, 0, 0, 1/3, 1/3, 2/3],
        [1/3, 0, 0, 1/3, 2/3, 0],
        [1/3, 0, 0, 1/3, 2/3, 1/3],
        [1/3, 0, 0, 1/3, 2/3, 2/3]
    ],
    'range': [1, 0, 1, 0]
}

sqrt3 = np.sqrt(3)
kockSnowflake = {
    'IFS_matrix': [
        [0.5, -(sqrt3/6), (sqrt3/6), 0.5, 0, 0],
        [1/3, 0, 0, 1/3, (sqrt3/3), 1/3],
        [1/3, 0, 0, 1/3, 0, 2/3],
        [1/3, 0, 0, 1/3, -(sqrt3/3), 1/3],
        [1/3, 0, 0, 1/3, -(sqrt3/3), -1/3],
        [1/3, 0, 0, 1/3, 0, -2/3],
        [1/3, 0, 0, 1/3, (sqrt3/3), -1/3],
    ],
    'range': [1, -1, 1, -1]
}

PI = np.pi
cos = np.cos; sin = np.sin
cos1 = cos(2*PI/5); sin1 = sin(2*PI/5)
cos2 = cos(PI/5); sin2 = sin(PI/5)
r = 1 / (2*cos(2*PI/5) + 2)
cos3 = cos(PI/5)
sin3 = sin(PI/5)
pentagonFractal = {
    'IFS_matrix':[
        [0.5*cos3, -0.5*sin3, 0.5*sin3, 0.5*cos3, 0.0, 0.0],
        [r, 0.0, 0.0, r, 0.5, 0.0],
        [r, 0.0, 0.0, r, cos1/2, sin1/2],
        [r, 0.0, 0.0, r, -cos2/2, sin2/2],
        [r, 0.0, 0.0, r, -cos2/2, -sin2/2],
        [r, 0.0, 0.0, r, cos1/2, -sin1/2],
    ],
    'range': [1, -1, 1, -1]                    
}

vicsek = {
    'IFS_matrix': [
        [1/3, 0.0, 0.0, 1/3, 0.0, 0.0],
        [1/3, 0.0, 0.0, 1/3, 0.0, 2/3],
        [1/3, 0.0, 0.0, 1/3, 0.0, -2/3],
        [1/3, 0.0, 0.0, 1/3, 2/3, 0.0],
        [1/3, 0.0, 0.0, 1/3, -2/3, 0.0]
    ],
    'range': [1, -1, 1, -1]
}

mapleLeaf = {
    'IFS_matrix': [
        [0.8, 0.0, 0.0, 0.8, 0.1, 0.04],
        [0.5, 0.0, 0.0, 0.5, 0.25, 0.4],
        [0.355, -0.355, 0.355, 0.35, 0.266, 0.078],
        [0.355, 0.355, -0.355, 0.355, 0.378, 0.434]
    ],
    'range': [1, 0, 1, 0]
}

inkblotTheFirst = {
    'IFS_matrix': [
        [0.5, 0, 0, 0.5, 0.0, 0.0],
        [0.0, -3/4, 3/4, 0.0, -0.5, -0.5],
        [0.0, -3/4, 3/4, 0.0, 0.5, 0.5]
    ],
    'range': [2, -2, 2, -2]                    
}

inkblotTheSecond = {
    'IFS_matrix': [
        [0.5, 0, 0, 0.5, 0.0, 0.0],
        [0.0, -2/3, 2/3, 0.0, -0.5, 0.5],
        [0.0, -2/3, 2/3, 0.0, 0.5, -0.5]
],
    'range': [2, -2, 2, -2]                    
}

class IFS:
    def __init__(self, ifs_matrix):
        self.NoOfFuncs = len(ifs_matrix)

        self.funcs = [
            lambda x, y, a=a, b=b, c=c, d=d, e=e, f=f: (a*x + b*y + e, c*x + d*y + f)
            for row in ifs_matrix
            for a, b, c, d, e, f in [row]
        ]

    def __call__(self, x, y):
        return [func(x, y) for func in self.funcs]

def searchAllPoints(order, ifs_matrix, startPoint):
    ifs = IFS(ifs_matrix)
    
    points = [startPoint]
    for _ in range(order):
        new_points = []
        for point in points:
            new_points += ifs(*point)
        # points += new_points
        points = new_points

    return points


def main():
    order = 12
    density = 500

    fractal = inkblotTheSecond
    startPoint = (0.0, 0.0)
    displayMode = 'binary'

    points = searchAllPoints(order, fractal['IFS_matrix'], startPoint)
    xs, ys = list(zip(*points))

    data = goodies.coorsToDataMatrix(xs, ys, density, fractal['range'], pixelCounting=(displayMode!='binary'))
    # data = np.load(r"C:\Users\PC\Desktop\Programming\Python\Fractals\pictures\mapleLeafs\datas\o10d1000.npy")
    goodies.draw(data, colorMode=displayMode)

    # goodies.save_image(data, r"C:\Users\PC\Desktop\Programming\Python\Fractals\pictures\test.png",
    #                     colorMode=displayMode)
    

main()    