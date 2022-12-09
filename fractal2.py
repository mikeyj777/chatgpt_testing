import matplotlib.pyplot as plt
from random import random

# FRACTAL_R = random() # 0.3 is interesting
# FRACTAL_C = random() # 0.5 is interesting

FRACTAL_R = 0.3
FRACTAL_C = 0.5

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
max_iter = 100

# Create a 2D array to hold the results of the fractal calculation
F = [[0 for x in range(width)] for y in range(height)]

# Define the complex function for the fractal calculation

def f(z):
    return z**2 + complex(FRACTAL_R, FRACTAL_C)

# Perform the fractal calculation for each pixel in the image
for y in range(height):
    for x in range(width):
        z = X[y][x]
        for i in range(max_iter):
            z = f(z)
            if abs(z) > 2:
                F[y][x] = i
                break

# Use matplotlib to visualize the fractal
plt.imshow(F, cmap='binary')
plt.show()