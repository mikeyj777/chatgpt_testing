import matplotlib.pyplot as plt

# Set the size of the image
width = 400
height = 400

# Create a 2D array of complex numbers representing the pixels in the image
X = [[complex(0,0) for x in range(width)] for y in range(height)]

# Set the range of values for the real and imaginary components of the complex numbers
rmin = -2.0
rmax = 1.0
imin = -1.5
imax = 1.5

# Populate the 2D array of complex numbers with values in the specified range
for y in range(height):
    for x in range(width):
        r = rmin + (rmax - rmin) * x / width
        i = imin + (imax - imin) * y / height
        X[y][x] = complex(r, i)

# Set the maximum number of iterations for the Mandelbrot calculation
max_iter = 100

# Create a 2D array to hold the results of the Mandelbrot calculation
M = [[0 for x in range(width)] for y in range(height)]

# Perform the Mandelbrot calculation for each pixel in the image
for y in range(height):
    for x in range(width):
        c = X[y][x]
        z = complex(0, 0)
        for i in range(max_iter):
            z = z**2 + c
            if abs(z) > 2:
                M[y][x] = i
                break

# Use matplotlib to visualize the Mandelbrot set
plt.imshow(M, cmap='binary')
plt.show()