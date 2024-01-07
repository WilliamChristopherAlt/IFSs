import numpy as np
import goodies
import time

inkblot = {
    'IFS_matrix1': [
        [0, 2/3, 2/3, 0, 0.0, 0.0],
        [0.0, -2/3, 2/3, 0.0, -0.25, 0.25],
        [0.0, -2/3, 2/3, 0.0, 0.25, -0.25]
],
    'IFS_matrix2': [
        [0, 3/4, 3/4, 0, 0.0, 0.0],
        [0.0, -3/4, 3/4, 0.0, -0.25, -0.25],
        [0.0, -3/4, 3/4, 0.0, 0.25, 0.25]
    ],
    'range': [1, -1, 1, -1]                    
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

def searchAllPoints(order, ifs_matrix1, ifs_matrix2, startPoint):
    ifs1 = IFS(ifs_matrix1)
    ifs2 = IFS(ifs_matrix2)
    
    start = time.time()

    points = [startPoint]
    for i in range(order):
        newPoints = []
        if i % 2:
            for point in points:
                newPoints += ifs1(*point)
        else:
            for point in points:
                newPoints += ifs2(*point)
        points = newPoints
    
    end = time.time() - start
    print(end)

    return points


def main():
    order = 15
    density = 400

    fractal = inkblot
    startPoint = (0.0, 0.0)
    displayMode = 'grey'

    points = searchAllPoints(order, fractal['IFS_matrix1'], fractal['IFS_matrix2'], startPoint)
    xs, ys = list(zip(*points))

    start = time.time()
    data = goodies.coorsToDataMatrix(xs, ys, density, fractal['range'], pixelCounting=(displayMode!='binary'))
    print(time.time() - start)

    start = time.time()
    goodies.draw(data, colorMode=displayMode)
    print(time.time() - start)

    # goodies.save_image(data, r"C:\Users\PC\Desktop\Programming\Python\Fractals\pictures\inkblot.png",
    #                     colorMode=displayMode)
    

main()    