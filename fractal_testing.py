import numpy as np

max_iter = 50

minval = -10
maxval = 10
step = 0.01

r = minval - step

points = []

def f(z):
    return z**2 + complex(0, 0)


while r <= maxval:
    r += step
    c = minval - step
    while c <= maxval:
        c += step
        z = complex(r,c)
        for i in range(max_iter+1):
            z = f(z)
            if abs(z) > 2:
                break
        if i >= max_iter:
            points.append([i, r, c])

points = np.asarray(points)

points = points[points[:,0].argsort()]

print(points)