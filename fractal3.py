import matplotlib.pyplot as plt
from random import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a new figure for the plot
fig = plt.figure()

# Create a 3D axes object for the plot
ax = fig.add_subplot(111, projection='3d')

# FRACTAL_R = random() # 0.3 is interesting
# FRACTAL_C = random() # 0.5 is interesting

points = []

# slope of seed numbers
m = (0.99 - 0.01) / (10 - 1)

#starting seed number
x = 0.01 - m

while x <= 1:

    x += m

    FRACTAL_R = x
    FRACTAL_C = 1 - x

    # Set the size of the image
    width = 400
    height = 400

    # Set the range of values for the real and imaginary components of the complex numbers
    rmin = -1.5
    rmax = 1.5
    imin = -1.5
    imax = 1.5

    # Create a 2D array of complex numbers representing the pixels in the image
    X = [[complex(0,0) for x in range(width)] for y in range(height)]

    # Populate the 2D array of complex numbers with values in the specified range
    for y in range(height):
        for x in range(width):
            r = rmin + (rmax - rmin) * x / width
            i = imin + (imax - imin) * y / height
            X[y][x] = complex(r, i)

    # Set the maximum number of iterations for the fractal calculation
    max_iter = 50

   # Define the complex function for the fractal calculation

    def f(z):
        return z**2 + complex(FRACTAL_R, FRACTAL_C)

    # Perform the fractal calculation for each pixel in the image
    for y in range(height):
        for x in range(width):
            z = X[y][x]
            for i in range(max_iter+1):
                z = f(z)
                if abs(z) > 2:
                    break
            if i >= max_iter:
                points.append([x, z.real, z.imag])


points = np.asarray(points)
# Use matplotlib to visualize the fractal
ax.scatter([points[:,0], points[:,1], points[:,2]])
plt.show()